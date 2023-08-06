# cnpjinfo

**cnpjinfo** is a library for obtaining cnpj information via scraping from the receitaws website.

## Features

- CNPJ information via receitaws website.

## Installation

- Run `pip install cnpjinfo`

## Exxemple

```python
from cnpjinfo import cnpjinfo

info = cnpjinfo('12345678901234')
nome = info.get('nome')
tel = info.get('telefone')

print (f'Nome: {nome}, Tel: {tel}'))
```

### console output

```bash
foo@bar:~$ ./myscript.py
Nome: COMPANY NAME., Tel: (11) 1111-1111
foo@bar:~$ 
```

## Upgrade

- Run `pip install cnpjinfo --upgrade`