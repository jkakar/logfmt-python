# -*- coding: utf-8 flake8:noqa -*-
from logfmt.parser import parse_line


def parse(stream):
    for line in stream:
        values = parse_line(line)
        if values:
            yield values
