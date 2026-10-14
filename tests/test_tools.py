import unittest


class SyntheticToolsTests(unittest.TestCase):
    def test_echo_lookup_and_unknown_key(self):
        from agents_mcp_server.tools import echo, lookup
        self.assertEqual(echo('synthetic'),{'text':'synthetic','source':'synthetic'})
        self.assertEqual(lookup('sample.discount')['expected_total'],90)
        with self.assertRaises(ValueError):
            lookup('../../credentials')
