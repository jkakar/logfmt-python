Logfmt
======

Python package for parsing log lines in the `logfmt` style.  See the
original project by Blake Mizerany and Keith Rarick for information
about `logfmt` conventions and use: https://github.com/kr/logfmt


Using logfmt
------------

Easily process lines from `logfmt` formatted input: ::

    from logfmt import parse

    input = StringIO('\n'.join(['key1=value1', 'key2=value2']))
    for values in parse(input):
        print values

This program produces this output: ::

    {'key1': 'value1'}
    {'key2': 'value2'}

Installation
------------

To install it, simply: ::

    pip install logfmt

