# pywgetb3
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pywgetb3)
[![PyPI version](https://badge.fury.io/py/pywgetb3.svg)](https://badge.fury.io/py/pywgetb3)
[![Coverage Status](https://coveralls.io/repos/github/andreroggeri/pywgetb3/badge.svg?branch=master)](https://coveralls.io/github/andreroggeri/pywgetb3?branch=master)
[![Maintainability](https://api.codeclimate.com/v1/badges/e550387e85d315a212af/maintainability)](https://codeclimate.com/github/andreroggeri/pywgetb3/maintainability) [![Join the chat at https://gitter.im/pywgetb3/pywgetb3](https://badges.gitter.im/pywgetb3/pywgetb3.svg)](https://gitter.im/pywgetb3/pywgetb3?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

Acesse seus extratos do Banco do Brasil pelo Python

## Instalação
Disponível via pip

`pip install pywgetb3`

## Aquisitando dados
```python
import pywgetb3

pywgetb3.anual(year=2021, destiny='.\\downloads\\anual\\')
pywgetb3.monthly(year=2021, month=8,  destiny='.\\downloads\\monthly\\')
pywgetb3.daily(year=2021, month=8, day=1, destiny='.\\downloads\\daily\\')
```

## Contribuindo

Envie seu PR para melhorar esse projeto ! 😋