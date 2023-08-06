# Maper

Maper (may-per, like paper with an 'm', as in **m**eta-p**aper**) is a minimal, easy to use, command line tool to download/manage scientific
papers in pdf-format by attaching a bibtex-file and updating its metadata using pikepdf.

## Install

Install from PyPI:
```shell
$ pip install maper
```

Additionally, `pandoc` needs to be installed and available.

## Run
Use either `python -m maper <command>` or if `PATH` is set correctly, `maper <command>`.

Currently available commands are:
- create
- show
- bibtex

### create
Create a PDF file with an attached bibtex file and metadata title and authors set:
```shell
$ maper create <bibtex> <pdf> [-o <output>]
```
where `<bibtex>` and `<pdf>` may be either local files or URLs, and output is a filename, or a directory.
If `<output>` is not a directory, the resulting pdf will be stored in that file.
If `<output>` is an existing directory, the file will be stored in
`<output>/<FirstAuthorFamilyName><Year><FirstTitleWord>.pdf`.
If `<output>` is omitted, the current directory is assumed.


### show
Show a summary of the attached bibtex of one or multiple pdfs:
```shell
maper show [<pdf> ...]
```

### bibttex
Show the bibtex of one or combined of multiple pdfs (e.g. to create a full bibtex file)
```shell
$ maper bibtex [<pdf> ...]
```

## Example
The following creates the pdf `Weizenbaum1966ELIZA.pdf`, shows a summary, and the full attached bibtex filed:
```shell
$ maper create 'https://dblp.uni-trier.de/rec/journals/cacm/Weizenbaum66.bib?param=1' 'https://cse.buffalo.edu/~rapaport/572/S02/weizenbaum.eliza.1966.pdf'
$ maper show Weizenbaum1966ELIZA.pdf
$ maper bibtex Weizenbaum1966ELIZA.pdf
```
