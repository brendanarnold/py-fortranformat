

import unittest

from fortranformat._output import output as _output
from fortranformat._lexer import lexer as _lexer
from fortranformat._parser import parser as _parser
import fortranformat.config as config


class FEdTests(unittest.TestCase):

    def setUp(self):
        config.reset()

    def test_1(self):
        inpt = [3.1]
        fmt = '(F5.0)'
        eds, rev_eds = _parser(_lexer(fmt))
        result = '   3.'
        self.assertEqual(result, _output(eds, rev_eds, inpt))

    def test_2(self):
        inpt = [99999.01]
        fmt = '(F6.0)'
        eds, rev_eds = _parser(_lexer(fmt))
        result = '99999.'
        self.assertEqual(result, _output(eds, rev_eds, inpt))
