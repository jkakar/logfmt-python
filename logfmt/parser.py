# -*- coding: utf-8 -*-

GARBAGE = 0
KEY = 1
EQUAL = 2
IVALUE = 3
QVALUE = 4


def parse_line(line):
    output = {}
    key, value = (), ()
    escaped = False
    state = GARBAGE
    for i, c in enumerate(line):
        i += 1
        if state == GARBAGE:
            if c > ' ' and c != '"' and c != '=':
                key = (c,)
                state = KEY
            continue
        if state == KEY:
            if c > ' ' and c != '"' and c != '=':
                state = KEY
                key += (c,)
            elif c == '=':
                output["".join(key).strip()] = True
                state = EQUAL
            else:
                output["".join(key).strip()] = True
                state = GARBAGE
            if i >= len(line):
                output["".join(key).strip()] = True
            continue
        if state == EQUAL:
            if c > ' ' and c != '"' and c != '=':
                value = (c,)
                state = IVALUE
            elif c == '"':
                value = ()
                escaped = False
                state = QVALUE
            else:
                state = GARBAGE
            if i >= len(line):
                output["".join(key).strip()] = "".join(value) or True
            continue
        if state == IVALUE:
            if not (c > ' ' and c != '"' and c != '='):
                output["".join(key).strip()] = "".join(value)
                state = GARBAGE
            else:
                value += (c,)
            if i >= len(line):
                output["".join(key).strip()] = "".join(value)
            continue
        if state == QVALUE:
            if c == '\\':
                escaped = True
            elif c == '"':
                if escaped:
                    escaped = False
                    value += (c,)
                    continue
                output["".join(key).strip()] = "".join(value)
                state = GARBAGE
            else:
                value += (c,)
            continue
    return output
