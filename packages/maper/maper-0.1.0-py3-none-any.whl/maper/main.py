#!/usr/bin/env python3
import logging
from argparse import Namespace

import click


@click.group()
@click.option('-q', '--quiet', count=True)
@click.option('-v', '--verbose', count=True)
@click.pass_context
def main(ctx, quiet, verbose):
    ctx.ensure_object(Namespace)

    # critical 50, error 40, warning 30, info 20, debug 10
    ctx.obj.verbosity = (2 - verbose + quiet) * 10
    logging.basicConfig(
        format='%(asctime)s %(name)s %(levelname)s - %(message)s',
        level=ctx.obj.verbosity
    )
