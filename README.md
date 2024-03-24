
# SNMP Simulation Data

[![PyPI](https://img.shields.io/pypi/v/snmpsim-data.svg?maxAge=2592000)](https://pypi.org/project/snmpsim-data/)
[![Python Versions](https://img.shields.io/pypi/pyversions/snmpsim-data.svg)](https://pypi.org/project/snmpsim-data/)
[![GitHub license](https://img.shields.io/badge/license-BSD-blue.svg)](https://raw.githubusercontent.com/lextudio/snmpsim-data/master/LICENSE.txt)

The `snmpsim-data-lextudio` package contains simulation data for
[snmpsim](https://www.pysnmp.com/snmpsim) - free and open-source SNMP agent simulator.

The package is distributed under 2-clause
[BSD license](https://www.pysnmp.com/snmpsim/license.html).

## Download

SNMP simulation data can be downloaded as a Python package from
[PyPI](https://pypi.org/project/snmpsim-data/).

## Installation

Just run:

```bash
$ pyenv local 3.12
$ pip install pipenv
$ pipenv install snmpsim-data-lextudio
$ pipenv run setup-snmpsim-data snmpsim-data/data
```

> This also install `snmpsim-lextudio` package as a dependency.

## How to use simulation data

Invoke `snmpsimd` and point it to a directory with simulation data:

``` bash
$ pipenv run snmpsimd --data-dir=snmpsim-data/data --agent-udpv4-endpoint=127.0.0.1:1024
```

Simulation data is stored in simple plain-text files having `OID|TYPE|VALUE`
format:

``` bash
$ cat public.snmprec
1.3.6.1.2.1.1.1.0|4|Linux 2.6.25.5-smp SMP Tue Jun 19 14:58:11 CDT 2007 i686
1.3.6.1.2.1.1.2.0|6|1.3.6.1.4.1.8072.3.2.10
1.3.6.1.2.1.1.3.0|67|233425120
1.3.6.1.2.1.2.2.1.6.2|4x|00127962f940
1.3.6.1.2.1.4.22.1.3.2.192.21.54.7|64x|c3dafe61
...
```

Simulator maps query parameters like SNMP community names, SNMPv3 contexts or
IP addresses onto data files paths relative to the `data` directory.

## Documentation

Detailed information on SNMP simulator usage could be found at
[snmpsim site](https://www.pysnmp.com/snmpsim/).

## Getting help

If you run into bad simulation data, feel free to
[open an issue](https://github.com/lextudio/pysnmp/issues) on GitHub.

## Contributions

If you have an SNMP-managed device, consider snmpwalk'ing it (or use `snmprec` tool
from `snmpsim` package) and submit a PR offering your data.

Copyright (c) 2019, [Ilya Etingof](mailto:etingof@gmail.com).
Copyright (c) 2024, [LeXtudio Inc.](mailto:support@lextudio.com).
All rights reserved.
