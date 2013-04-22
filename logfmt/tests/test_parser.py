from cStringIO import StringIO
from unittest import TestCase

from logfmt import parse


class ParseTest(TestCase):
    def test_parse_empty_stream(self):
        """C{parse} is a no-op if the specified stream is empty."""
        stream = StringIO()
        self.assertEqual([], list(parse(stream)))
