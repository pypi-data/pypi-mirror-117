#!/usr/bin/env python3
import logging

import click
import pikepdf

from .util import bib2json
from .main import main


LOGGER = logging.getLogger(__name__)


@main.command()
@click.argument('pdf_files', nargs=-1, type=click.Path(exists=True))
def show(pdf_files):
    file_infos = []

    for fname in pdf_files:
        with pikepdf.open(fname) as pdf:
            try:
                attachment = pdf.attachments['bibtex.bib']
            except KeyError:
                LOGGER.warning(f'No attached bibtex found in \'{fname}\'')
                continue
            bibtex = attachment.get_file().read_bytes()
        bib = bib2json(bibtex)[0]
        file_infos.append((fname, bib))

    output = ''
    for fname, bib in file_infos:
        authors = '; '.join([f"{name['family']}, {name['given']}" for name in bib['author']])
        output = '\n'.join([
            f'{fname}:\n'
            f'  Type: {bib["type"]}\n'
            f'  Identifier: {bib["id"]}\n'
            f'  Authors: {authors}\n'
            f'  Title: {bib["title"]}\n'
            f'  Year: {bib["issued"]["date-parts"][0][0]}\n'
            f'  Published: {bib["container-title"]}\n'
            for fname, bib in file_infos
        ])

    print(output, end='')
