

import unittest

from fortranformat._output import output as _output
from fortranformat._lexer import lexer as _lexer
from fortranformat._parser import parser as _parser
import fortranformat.config as config
from fortranformat import FortranRecordWriter

class ReversionOutputTests(unittest.TestCase):

    def setUp(self):
        config.reset()

    def reversion_output_test_1(self):
        inpt = [1.0, 1.0, 1.0, 1.0, 1.0]
        fmt = "('[', 3F4.1, ']')"
        eds, rev_eds = _parser(_lexer(fmt))
        result = """[ 1.0 1.0 1.0]
[ 1.0 1.0"""
        self.assertEqual(result, _output(eds, rev_eds, inpt))

    def reversion_output_test_2(self):
        inpt = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
        fmt = "('[', 3F4.1, ']')"
        eds, rev_eds = _parser(_lexer(fmt))
        result = """[ 1.0 1.0 1.0]
[ 1.0 1.0 1.0]"""
        self.assertEqual(result, _output(eds, rev_eds, inpt))

    def reversion_output_test_3(self):
        inpt = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
        fmt = "('[', (3F4.1), ']')"
        eds, rev_eds = _parser(_lexer(fmt))
        result = """[ 1.0 1.0 1.0]
 1.0 1.0 1.0]"""
        self.assertEqual(result, _output(eds, rev_eds, inpt))

    def reversion_output_test_4(self):
        line = FortranRecordWriter("('[', 3F4.1, ']')")
        result = """[ 1.0 1.0 1.0]
[ 1.0 1.0 1.0]"""
        self.assertEqual(line.write([1.0, 1.0, 1.0, 1.0, 1.0, 1.0]), result)