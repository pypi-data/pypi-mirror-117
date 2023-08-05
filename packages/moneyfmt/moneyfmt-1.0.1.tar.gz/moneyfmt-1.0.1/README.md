# Moneyfmt

Converte tipo Decimal para uma string formatada como dinheiro


## Como usar

Instale com:

```bash
pip install moneyfmt
```

Use no seu código:

```python
from moneyfmt import moneyfmt
```

## Parâmetros
```text
places:  required number of places after the decimal point
curr:    optional currency symbol before the sign (may be blank)
sep:     optional grouping separator (comma, period, space, or blank)
dp:      decimal point indicator (comma or period)
         only specify as blank when places is zero
pos:     optional sign for positive numbers: '+', space or blank
neg:     optional sign for negative numbers: '-', '(', space or blank
trailneg:optional trailing minus indicator:  '-', ')', space or blank
```

## Como usar?
```python
from moneyfmt import moneyfmt

>>> d = Decimal('-1234567.8901')

>>> moneyfmt(d, curr='$')
'-$1,234,567.89'

>>> moneyfmt(d, places=0, sep='.', dp='', neg='', trailneg='-')
'1.234.568-'

>>> moneyfmt(d, curr='$', neg='(', trailneg=')')
'($1,234,567.89)'

>>> moneyfmt(Decimal(123456789), sep=' ')
'123 456 789.00'

>>> moneyfmt(Decimal('-0.02'), neg='<',

>>> trailneg='>')
'<0.02>'
```


Referência: https://docs.python.org/3/library/decimal.html


## Licença

Leia https://docs.python.org/pt-br/3.7/copyright.html

Copyright © 2001-2021 Python Software Foundation. All rights reserved.
