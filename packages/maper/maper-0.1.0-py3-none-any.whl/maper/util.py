#!/usr/bin/env python3
import json
from subprocess import run


def bib2json(string):
    proc = run(['pandoc', '-f', 'bibtex', '-t', 'csljson'], input=string, capture_output=True, check=True)
    obj = json.loads(proc.stdout.decode('utf-8'))
    return obj


def json2bib(obj):
    string = json.dumps(obj)
    proc = run(['pandoc', '-f', 'csljson', '-t', 'bibtex'], input=string, text=True, capture_output=True, check=True)
    return proc.stdout
