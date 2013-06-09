# -*- coding: utf-8 -*-
from logfmt import parse_line
from unittest import TestCase


class ParserTestCase(TestCase):
    def test_empty_log_line(self):
        data = parse_line("")
        self.assertEqual(data, {})

    def test_whitespace_only_log_line(self):
        data = parse_line("\t")
        self.assertEqual(data, {})

    def test_key_without_value(self):
        data = parse_line("key")
        self.assertEqual(data, {'key': True})

    def test_key_without_value_and_whitespace(self):
        data = parse_line("  key  ")
        self.assertEqual(data, {'key': True})

    def test_multiple_single_keys(self):
        data = parse_line("key1 key2")
        self.assertEqual(data, {'key1': True, 'key2': True})

    def test_unquoted_value(self):
        data = parse_line("key=value")
        self.assertEqual(data, {'key': "value"})

    def test_pairs(self):
        data = parse_line("key1=value1 key2=value2")
        self.assertEqual(data, {'key1': "value1", 'key2': "value2"})

    def test_mixed_single_or_non_single_pairs(self):
        data = parse_line("key1=value1 key2")
        self.assertEqual(data, {'key1': "value1", 'key2': True})

    def test_mixed_pairs_whatever_the_order(self):
        data = parse_line("key1 key2=value2")
        self.assertEqual(data, {'key1': True, 'key2': "value2"})

    def test_quoted_value(self):
        data = parse_line('key="quoted value"')
        self.assertEqual(data, {'key': "quoted value"})

    def test_escaped_quote_value(self):
        data = parse_line('key="quoted \\" value" r="esc\t"')
        self.assertEqual(data, {'key': 'quoted \" value', 'r': "esc\t"})

    def test_mixed_pairs(self):
        data = parse_line('key1="quoted \\" value" key2 key3=value3')
        self.assertEqual(data, {
            'key1': 'quoted \" value', 'key2': True, 'key3': "value3"
        })

    def test_mixed_characters_pairs(self):
        data = parse_line('foo=bar a=14 baz="hello kitty" ƒ=2h3s cool%story=bro f %^asdf')
        self.assertEqual(data, {
            'foo': "bar", 'a': "14", 'baz': "hello kitty", 'ƒ': "2h3s",
            "cool%story": "bro", 'f': True, "%^asdf": True
        })

    def test_pair_with_empty_quote(self):
        data = parse_line('key=""')
        self.assertEqual(data, {'key': ""})
