from cStringIO import StringIO
from unittest import TestCase

from logfmt import parse


class ParseTest(TestCase):
    """Tests for L{logfmt.parse}."""

    def test_parse_empty_stream(self):
        """L{parse} is a no-op if the specified stream is empty."""
        stream = StringIO()
        self.assertEqual([], list(parse(stream)))

    def test_parse_key_without_value(self):
        """L{parse} correctly parses a lone key without a value."""
        stream = StringIO('key')
        self.assertEqual([{'key': None}], list(parse(stream)))

    def test_parse_key_with_whitespace_and_without_value(self):
        """
        L{parse} correctly parses a lone key surrounded by whitespace without
        a value.
        """
        stream = StringIO('  key  ')
        self.assertEqual([{'key': None}], list(parse(stream)))

    def test_parse_multiple_single_keys(self):
        """L{parse} correctly parses a sequence of keys without values."""
        stream = StringIO('key1 key2')
        self.assertEqual([{'key1': None, 'key2': None}], list(parse(stream)))

    def test_parse_key_with_unquoted_value(self):
        """L{parse} correctly parses keys with unquoted values."""
        stream = StringIO('key=value')
        self.assertEqual([{'key': 'value'}], list(parse(stream)))

    def test_parse_multiple_key_value_pairs(self):
        """
        L{parse} correctly parses multiple key/value pairs on the same line.
        """
        stream = StringIO('key1=value1 key2=value2')
        self.assertEqual([{'key1': 'value1', 'key2': 'value2'}],
                         list(parse(stream)))

    def test_parse_mixed_single_key_and_key_value_pair(self):
        """
        L{parse} correctly parses mixed single keys and key/value pairs on the
        same line.
        """
        stream = StringIO('key1 key2=value2')
        self.assertEqual([{'key1': None, 'key2': 'value2'}],
                         list(parse(stream)))

    def test_parse_mixed_key_value_pair_and_single_key(self):
        """
        L{parse} correctly parses mixed single keys and key/value pairs on the
        same line.
        """
        stream = StringIO('key1=value1 key2')
        self.assertEqual([{'key1': 'value1', 'key2': None}],
                         list(parse(stream)))

    def test_parse_key_with_double_quoted_value(self):
        """
        L{parse} correctly parses values that are surrounded by double-quotes.
        """
        stream = StringIO('key="a double-quoted value"')
        self.assertEqual([{'key': 'a double-quoted value'}],
                         list(parse(stream)))

    def test_parse_key_with_double_quoted_value_and_double_quote(self):
        """
        L{parse} correctly parses values that are surrounded by double-quotes.
        An escape double-quote included in the value is considered to be part
        of it.
        """
        stream = StringIO('key="a double-quoted \\" value"')
        self.assertEqual([{'key': 'a double-quoted " value'}],
                         list(parse(stream)))

    def test_parse_mixed_key_value_pairs(self):
        """
        L{parse} correctly parses different kinds of keys and values on the
        same line.
        """
        stream = StringIO('key1="a double-quoted \\" value" key2 key3=value3')
        self.assertEqual([{'key1': 'a double-quoted " value',
                           'key2': None,
                           'key3': 'value3'}],
                         list(parse(stream)))
