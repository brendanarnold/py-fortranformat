import unittest

import fortranformat as ff
from fortranformat._output import output as _output
from fortranformat._lexer import lexer as _lexer
from fortranformat._parser import parser as _parser
import fortranformat.config as config


class ConfigTests(unittest.TestCase):

    def setUp(self):
        config.reset()

    def test_1(self):
        config.PROC_MAXINT = 2**31
        eds, rev_eds = _parser(_lexer('(1Z10)'))
        result = _output(eds, rev_eds, [-1])
        self.assertEqual(result, '  FFFFFFFF')

    def test_2(self):
        config.PROC_MAXINT = 2**31
        eds, rev_eds = _parser(_lexer('(1Z10)'))
        result = _output(eds, rev_eds, [-3])
        self.assertEqual(result, '  FFFFFFFD')

    def test_3(self):
        config.PROC_MAXINT = None
        eds, rev_eds = _parser(_lexer('(1Z10)'))
        result = _output(eds, rev_eds, [-1])
        self.assertEqual(result, '        -1')

    def test_4(self):
        config.PROC_MAXINT = None
        eds, rev_eds = _parser(_lexer('(1Z10)'))
        result = _output(eds, rev_eds, [-3])
        self.assertEqual(result, '        -3')

    def test_5(self):
        config.PROC_MAXINT = None
        eds, rev_eds = _parser(_lexer('(1Z10)'))
        result = _output(eds, rev_eds, [-12])
        self.assertEqual(result, '        -C')


if __name__ == '__main__':
    unittest.main()
