#!/usr/bin/env python3

"""
Bonito training.
"""

import os
import csv
from functools import partial
from datetime import datetime
from collections import OrderedDict
from argparse import ArgumentParser
from argparse import ArgumentDefaultsHelpFormatter

from bonito.io import CSVLogger
from bonito.util import __models__, default_config, default_data
from bonito.util import load_data, load_model, load_symbol, init, half_supported
from bonito.training import ChunkDataSet, load_state, train, test, func_scheduler, cosine_decay_schedule

import toml
import torch
import numpy as np
from torch.optim import AdamW
from torch.cuda.amp import GradScaler
from torch.utils.data import DataLoader


def main(args):

    workdir = os.path.expanduser(args.training_directory)

    if os.path.exists(workdir) and not args.force:
        print("[error] %s exists, use -f to force continue training." % workdir)
        exit(1)

    init(args.seed, args.device)
    device = torch.device(args.device)

    print("[loading data]")
    train_data = load_data(limit=args.chunks, directory=args.directory)
    if os.path.exists(os.path.join(args.directory, 'validation')):
        valid_data = load_data(directory=os.path.join(args.directory, 'validation'))
    else:
        print("[validation set not found: splitting training set]")
        split = np.floor(len(train_data[0]) * 0.97).astype(np.int32)
        valid_data = [x[split:] for x in train_data]
        train_data = [x[:split] for x in train_data]

    train_loader = DataLoader(ChunkDataSet(*train_data), batch_size=args.batch, shuffle=True, num_workers=4, pin_memory=True)
    valid_loader = DataLoader(ChunkDataSet(*valid_data), batch_size=args.batch, num_workers=4, pin_memory=True)

    if args.pretrained:
        dirname = args.pretrained
        if not os.path.isdir(dirname) and os.path.isdir(os.path.join(__models__, dirname)):
            dirname = os.path.join(__models__, dirname)
        config_file = os.path.join(dirname, 'config.toml')
    else:
        config_file = args.config

    config = toml.load(config_file)

    argsdict = dict(training=vars(args))

    os.makedirs(workdir, exist_ok=True)
    toml.dump({**config, **argsdict}, open(os.path.join(workdir, 'config.toml'), 'w'))

    print("[loading model]")
    if args.pretrained:
        print("[using pretrained model {}]".format(args.pretrained))
        model = load_model(args.pretrained, device, half=False)
    else:
        model = load_symbol(config, 'Model')(config)

    optimizer = AdamW(model.parameters(), amsgrad=False, lr=args.lr)

    scaler = GradScaler(enabled=half_supported() and not args.no_amp)

    last_epoch = load_state(workdir, args.device, model, optimizer, use_amp=not args.no_amp)

    lr_scheduler = func_scheduler(
        optimizer, cosine_decay_schedule(1.0, 0.1), args.epochs * len(train_loader),
        warmup_steps=500, start_step=last_epoch*len(train_loader)
    )

    if args.multi_gpu:
        from torch.nn import DataParallel
        model = DataParallel(model)
        model.decode = model.module.decode
        model.alphabet = model.module.alphabet

    if hasattr(model, 'seqdist'):
        criterion = model.seqdist.ctc_loss
    else:
        criterion = None

    for epoch in range(1 + last_epoch, args.epochs + 1 + last_epoch):

        try:
            with CSVLogger(os.path.join(workdir, 'losses_{}.csv'.format(epoch))) as loss_log:
                train_loss, duration = train(
                    model, device, train_loader, optimizer, criterion=criterion,
                    use_amp=half_supported() and not args.no_amp, scaler=scaler, lr_scheduler=lr_scheduler,
                    loss_log = loss_log
                )

            model_state = model.state_dict() if not args.multi_gpu else model.module.state_dict()
            torch.save(model_state, os.path.join(workdir, "weights_%s.tar" % epoch))

            val_loss, val_mean, val_median = test(
                model, device, valid_loader, criterion=criterion
            )
        except KeyboardInterrupt:
            break

        print("[epoch {}] directory={} loss={:.4f} mean_acc={:.3f}% median_acc={:.3f}%".format(
            epoch, workdir, val_loss, val_mean, val_median
        ))

        with CSVLogger(os.path.join(workdir, 'training.csv')) as training_log:
            training_log.append(OrderedDict([
                ('time', datetime.today()),
                ('duration', int(duration)),
                ('epoch', epoch),
                ('train_loss', train_loss),
                ('validation_loss', val_loss),
                ('validation_mean', val_mean),
                ('validation_median', val_median)
            ]))

def argparser():
    parser = ArgumentParser(
        formatter_class=ArgumentDefaultsHelpFormatter,
        add_help=False
    )
    parser.add_argument("training_directory")
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--config', default=default_config)
    group.add_argument('--pretrained', default="")
    parser.add_argument("--directory", default=default_data)
    parser.add_argument("--device", default="cuda")
    parser.add_argument("--lr", default=2e-3, type=float)
    parser.add_argument("--seed", default=25, type=int)
    parser.add_argument("--epochs", default=5, type=int)
    parser.add_argument("--batch", default=64, type=int)
    parser.add_argument("--chunks", default=0, type=int)
    parser.add_argument("--no-amp", action="store_true", default=False)
    parser.add_argument("--multi-gpu", action="store_true", default=False)
    parser.add_argument("-f", "--force", action="store_true", default=False)
    return parser
