[![Latest PyPI Release](https://img.shields.io/pypi/v/pygamemode.svg)](https://pypi.org/project/pygamemode/)
[![Build](https://github.com/aforren1/pygamemode/actions/workflows/build.yml/badge.svg)](https://github.com/aforren1/pygamemode/actions/workflows/build.yml)

A Python wrapper for the GameMode client API (https://github.com/FeralInteractive/gamemode).

To use this effectively, you'll need to install GameMode on your system. See either your system's package manager or the build instructions [here](https://github.com/FeralInteractive/gamemode/blob/master/README.md#development-).

Example usage:

```python
import gamemode as gm

if gm.request_start() != 0:
    msg = gm.error_string()
    raise ValueError('Failed to request gamemode start: {}...'.format(msg))

# ...do things here...

if gm.request_end() != 0:
    msg = gm.error_string()
    raise ValueError('Failed to request gamemode end: {}...'.format(msg))
```

See [test.py](https://github.com/aforren1/pygamemode/blob/master/test.py) for all available calls.
