#!/usr/bin/env python3
import logging
import re
import os
from io import BytesIO
from urllib.parse import urlparse

import click
import pikepdf
import requests

from .util import json2bib, bib2json
from .main import main


LOGGER = logging.getLogger(__name__)


@main.command()
@click.argument('bibtex-uri')
@click.argument('pdf-uri')
@click.option('-o', '--output', type=click.Path(exists=False, writable=True))
def create(bibtex_uri, pdf_uri, output):
    urls = {
        'bib': urlparse(bibtex_uri),
        'pdf': urlparse(pdf_uri),
    }
    bufs = {}

    for key, urlobj in urls.items():
        bufs[key] = BytesIO()
        if urlobj.scheme in ('http', 'https'):
            LOGGER.info(f'Downloading {key} from \'{urlobj.geturl()}\'')
            response = requests.get(urlobj.geturl(), stream=True)
            for chunk in response.iter_content(chunk_size=256):
                bufs[key].write(chunk)
        elif urlobj.scheme in ('', 'file'):
            LOGGER.info(f'Using local {key} from \'{urlobj.path}\'')
            with open(urlobj.path, 'rb') as fd:
                bufs[key].write(fd.read())
        else:
            raise RuntimeError(f'Protocol not supported: \'{urlobj.scheme}\'')
        bufs[key].seek(0)

    bibtex = bufs['bib'].read()
    bib = bib2json(bibtex)[0]
    authors = [f"{name['family']}, {name['given']}" for name in bib['author']]

    LOGGER.info(f"Identified \"{'; '.join(authors)}: '{bib['title']}', {bib['issued']['date-parts'][0][0]}.\"")

    identifier = '{:s}{:d}{:s}'.format(
        bib['author'][0]['family'],
        bib['issued']['date-parts'][0][0],
        re.match('[a-zA-Z]+', bib['title'])[0]
    )
    bib['id'] = identifier
    bibtex = json2bib([bib])

    if output is None:
        output = '.'
    if os.path.isdir(output):
        output = os.path.join(output, f'{identifier}.pdf')

    with pikepdf.open(bufs['pdf']) as pdf:
        with pdf.open_metadata() as meta:
            meta['dc:title'] = bib['title']
            meta['dc:creator'] = authors

        filespec = pikepdf.AttachedFileSpec(pdf, bibtex.encode('utf-8'))
        pdf.attachments['bibtex.bib'] = filespec

        pdf.save(output)
    LOGGER.info(f'Wrote pdf to \'{output}\'')
