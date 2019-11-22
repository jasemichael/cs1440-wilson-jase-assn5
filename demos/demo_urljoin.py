#!/bin/env python3

from urllib.parse import urljoin
import sys


if len(sys.argv) < 2:
    base =  'http://unnovative.net'
    for relative in ['levels/level1.html',
            '?query0=param0&query1=param1',
            'levels/level2.html?query0=param0&query1=param1',
            '#fragment',
            'index.html#fragment',
            'http://unnovative.net/this_is_already_an_absolute_URL.jpg']:
        print(urljoin(base, relative))

else:
    base = sys.argv[1]
    for relative in sys.argv[2:]:
        print(urljoin(base, relative))
