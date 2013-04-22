# Logfmt for Python

Python package for parsing log lines in the `logfmt` style.  See the
original project by Blake Mizerany and Keith Rarick for information
about `logfmt` conventions and use:

  https://github.com/kr/logfmt

## Setting up a development environment

Install dependencies and run the test suite:

    virtualenv .
    . bin/activate
    make

Or create the virtualenv with `virtualenvwrapper`:

    mkvirtualenv logfmt
    make

And then easily switch to it in the future:

    workon logfmt

Run tests:

    make check

## Using logfmt

Easily process lines from `logfmt` formatted input:

```python
from cStringIO import StringIO
from logfmt import parse

input = StringIO('\n'.join(['key1=value1', 'key2=value2']))
for result in parse(input):
    print result
```

This program produces this output:

```
{'key1': 'value1'}
{'key2': 'value2'}
```

## License

Copyright (C) 2013 Jamshed Kakar.

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
