def parse(stream):
    """Generator yields C{dict}s from logfmt-styled lines read from the stream.

    @param stream: A file-like object to read lines from.
    @return: Yields a C{dict} for each line in the stream.
    """
    for line in stream:
        result = parse_line(line)
        if result:
            yield result


SCAN_KEY = 1
SCAN_EQUAL = 2
SCAN_VALUE = 3

def parse_line(line):
    """Parse a line from the log stream.

    @param line: A line that contains logfmt-styled key/value pairs.
    @return: A C{dict} containing key/value pairs from the line.
    """
    result = {}
    state = SCAN_KEY
    last_character = None
    key = []
    value = []
    quoted_value = False
    for character in line:
        if state is SCAN_KEY:
            if character == '=':
                state = SCAN_VALUE
            elif character == '"':
                pass
            elif ord(character) > ord(' '):
                key.append(character)
            elif character == ' ' and key:
                state = SCAN_EQUAL
        elif state is SCAN_EQUAL:
            if character == '=':
                state = SCAN_VALUE
            elif character != ' ':
                result[''.join(key).strip()] = None
                key = []
                key.append(character)
                state = SCAN_KEY
        elif state is SCAN_VALUE:
            if character == ' ' and not quoted_value:
                if value:
                    state = SCAN_KEY
                    result[''.join(key).strip()] = ''.join(value).strip()
                    key = []
                    value = []
                    quoted_value = False
            elif quoted_value and character == '\\':
                pass
            elif character == '"':
                if quoted_value:
                    if last_character == '\\':
                        value.append(character)
                    else:
                        state = SCAN_KEY
                        result[''.join(key).strip()] = ''.join(value).strip()
                        key = []
                        value = []
                        quoted_value = False
                else:
                    quoted_value = True
            else:
                value.append(character)
        last_character = character

    if key and not value:
        result[''.join(key).strip()] = None
    elif value:
        result[''.join(key).strip()] = ''.join(value).strip()
    return result
