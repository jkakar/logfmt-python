# -*- coding: utf-8 flake8:noqa -*-
from logfmt.parser import parse_line
from logfmt.formatter import format_line

def parse(stream):
    for line in stream:
        values = parse_line(line)
        if values:
            yield values

# Will take in a list of hashes. Each call will generate a string for the next argument
def format(*args):
   for hash in args:
       output = format_line(hash)
       if output:
           yield output

