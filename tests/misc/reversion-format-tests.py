import unittest
import os
import sys

from fortranformat._output import output as _output
from fortranformat._lexer import lexer as _lexer
from fortranformat._parser import parser as _parser

class ReversionFormatTests(unittest.TestCase):

    def reversion_format_test_1(self):
        # Test case raised in issue 11
        inpt = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0]
        fmt = '(3F5.1)'
        eds, rev_eds = _parser(_lexer(fmt))
        result = '  1.0  2.0  3.0' + os.linesep + '  4.0  5.0  6.0' \
            + os.linesep + '  7.0'
        self.assertEqual(result, _output(eds, rev_eds, inpt))

    def reversion_format_test_2(self):
        # Test reversion which is not entire
        inpt = [1, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0]
        fmt = '(\'Header Lines=\',I4,/,(3F5.1))'
        eds, rev_eds = _parser(_lexer(fmt))
        result = 'Header Lines=   1' + os.linesep + '  1.0  2.0  3.0' \
            + os.linesep + '  4.0  5.0  6.0' + os.linesep + '  7.0'
        self.assertEqual(result, _output(eds, rev_eds, inpt))
