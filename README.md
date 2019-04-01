# flake8-breakpoint

[![pypi](https://badge.fury.io/py/flake8-breakpoint.svg)](https://pypi.org/project/flake8-breakpoint)
[![Python: 3.6+](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://pypi.org/project/flake8-breakpoint)
[![Downloads](https://img.shields.io/pypi/dm/flake8-breakpoint.svg)](https://pypistats.org/packages/flake8-breakpoint)
[![Build Status](https://travis-ci.org/Afonasev/flake8-breakpoint.svg?branch=master)](https://travis-ci.org/Afonasev/flake8-breakpoint)
[![Code coverage](https://codecov.io/gh/afonasev/flake8-breakpoint/branch/master/graph/badge.svg)](https://codecov.io/gh/afonasev/flake8-breakpoint)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://en.wikipedia.org/wiki/MIT_License)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

Flake8 plugin that check forgotten breakpoints.

## Installation

```bash
pip install flake8-breakpoint
```

## Errors

* B601 builtin function "breakpoint" found

```python
def function():
    breakpoint()  # error!
```

* B602 import debug module found

```python
def function():
    import pdb  # error! or ipdb/pudb
```

## License

MIT

## Change Log

### 1.0.0 - 2019-04-02

* initial
