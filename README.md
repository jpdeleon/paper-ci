# paper-ci
[![Build Status](https://travis-ci.com/jpdeleon/chronos.svg?branch=master)](https://travis-ci.com/jpdeleon/paper-ci)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
[![License: GPL v3](https://img.shields.io/badge/license-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

basic paper with continuous integration

This was an example I learned from a [metaprogramming class](https://www.youtube.com/watch?v=_Ms1Z4xfqv4).

## Dependency
* python
* pdflatex

To install,
```shell
sudo apt-get install texlive-latex-base texlive-fonts-recommended texlive-fonts-extra texlive-latex-extra
```

## Build
```shell
make
xdg-open paper.pdf
```
## See alo
* [cortex](https://github.com/rodluger/corTeX)
