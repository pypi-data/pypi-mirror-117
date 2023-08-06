#!/usr/bin/env python3
import logging

import click
import pikepdf

from .main import main


LOGGER = logging.getLogger(__name__)


@main.command()
@click.argument('pdf_files', nargs=-1, type=click.Path(exists=True))
def bibtex(pdf_files):
    full_bibtex = ''

    for fname in pdf_files:
        with pikepdf.open(fname) as pdf:
            try:
                attachment = pdf.attachments['bibtex.bib']
            except KeyError:
                LOGGER.warning(f'No attached bibtex found in \'{fname}\'')
                continue
            bibtex = attachment.get_file().read_bytes()
        full_bibtex += bibtex.decode('utf-8') + '\n'

    print(full_bibtex, end='')
