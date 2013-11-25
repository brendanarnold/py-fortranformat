

import unittest
import os
import sys

# sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from fortranformat._output import output as _output
from fortranformat._lexer import lexer as _lexer
from fortranformat._parser import parser as _parser
import fortranformat.config as config

class HEdOutputTests(unittest.TestCase):

    def setUp(self):
        config.reset()

    def h_output_test_1(self):
        inpt = [] 
        fmt = '(3Hsdf)'
        eds, rev_eds = _parser(_lexer(fmt))
        result = 'sdf'
        self.assertEqual(result, _output(eds, rev_eds, inpt))

    def h_output_test_2(self):
        inpt = [12] 
        fmt = '(1Hs)'
        eds, rev_eds = _parser(_lexer(fmt))
        result = 's'
        self.assertEqual(result, _output(eds, rev_eds, inpt))

    def h_output_test_3(self):
        inpt = [3]
        fmt = '(1Hs,F3.1)'
        eds, rev_eds = _parser(_lexer(fmt))
        result = 's3.0'
        self.assertEqual(result, _output(eds, rev_eds, inpt))

    def h_output_test_4(self):
        inpt = []
        fmt = '(6Hs)'
        eds, rev_eds = _parser(_lexer(fmt))
        result = 's'
        self.assertEqual(result, _output(eds, rev_eds, inpt))

    def h_output_test_4(self):
        inpt = []
        fmt = '(6Hs,F3.1)'
        eds, rev_eds = _parser(_lexer(fmt))
        result = 's,F3.1'
        self.assertEqual(result, _output(eds, rev_eds, inpt))
