Python package for parsing log lines in the `logfmt` style.

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
