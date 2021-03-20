

import unittest
import os
import sys

from fortranformat._output import output as _output
from fortranformat._lexer import lexer as _lexer
from fortranformat._parser import parser as _parser
import fortranformat.config as config

class GOutputTests(unittest.TestCase):

    def setUp(self):
        config.reset()

    def g_output_test_1(self):
        inpt = [0.0]
        fmt = '(G10.2)'
        eds, rev_eds = _parser(_lexer(fmt))
        result = "  0.00E+00"
        self.assertEqual(result, _output(eds, rev_eds, inpt))

    def g_output_test_2(self):
        '''Test where exponent is zero - note that GFortran actually crashes in this case'''
        inpt = [0.0]
        fmt = '(G10.0)'
        eds, rev_eds = _parser(_lexer(fmt))
        result = "    0.E+00"
        self.assertEqual(result, _output(eds, rev_eds, inpt))

    # def g_output_test_3(self):
    #     '''This is an invalid format/value combination'''
    #     inpt = [1.1]
    #     fmt = '(G10.0)'
    #     eds, rev_eds = _parser(_lexer(fmt))
    #     result = "    0.E+00"
    #     self.assertEqual(result, _output(eds, rev_eds, inpt))

    def g_output_test_4(self):
        inpt = [1.1]
        fmt = '(G12.4)'
        eds, rev_eds = _parser(_lexer(fmt))
        result = "   1.100    "
        self.assertEqual(result, _output(eds, rev_eds, inpt))

    def g_output_test_5(self):
        inpt = [0.0]
        fmt = '(G10.2)'
        eds, rev_eds = _parser(_lexer(fmt))
        result = "  0.00E+00"
        self.assertEqual(result, _output(eds, rev_eds, inpt))

    def g_output_test_6(self):
        inpt = [30]
        fmt = '(8g10.3)'
        eds, rev_eds = _parser(_lexer(fmt))
        result = "  30.0    "
        self.assertEqual(result, _output(eds, rev_eds, inpt))

    
