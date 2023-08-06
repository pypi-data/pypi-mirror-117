#!/usr/bin/env python3
from setuptools import setup, find_packages


with open('README.md', 'r', encoding='utf-8') as fd:
    long_description = fd.read()


setup(
    name='maper',
    use_scm_version=True,
    author='chrstphr',
    author_email='maper@j0d.de',
    description='CLI organize PDFs by attaching bibtex metadata',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/chr5tphr/maper',
    packages=find_packages(include=['maper*']),
    install_requires=[
        'click',
        'pikepdf>=3.0.0b3',
        'requests',
    ],
    setup_requires=[
        'setuptools_scm',
    ],
    python_requires='>=3.7',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    entry_points={
        'console_scripts': ['maper=maper.__main__:entry']
    }
)
