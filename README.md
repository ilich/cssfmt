# cssfmt
Tool to apply CSS formatting guidelines to a file.

## Installation

1. Install Python 3
2. `pip install cssutils`

## Usage

```
usage: cssfmt.py [-h] [-v] [-t] [-i [SIZE]] FILE

Apply CSS formatting guidelines to a file

positional arguments:
  FILE        target CSS file

optional arguments:
  -h, --help  show this help message and exit
  -v          show program's version number and exit
  -t          use tabs instead of spaces for indentation
  -i [SIZE]   set indentation size. The option is ignored if -t switch is
              used.
```