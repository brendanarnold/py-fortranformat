

import unittest
import os
import sys

from fortranformat._output import output as _output
from fortranformat._lexer import lexer as _lexer
from fortranformat._parser import parser as _parser
import fortranformat.config as config

class EOutputTests(unittest.TestCase):

    def setUp(self):
        config.reset()

    def e_output_test_1(self):
        '''Test where exponent is zero - note that GFortran actually crashes in this case'''
        inpt = [1.0]
        fmt = '(E10.0)'
        eds, rev_eds = _parser(_lexer(fmt))
        result = "**********"
        self.assertEqual(result, _output(eds, rev_eds, inpt))

    def e_output_test_1a(self):
        '''Test where exponent is zero - note that GFortran actually crashes in this case'''
        inpt = [0.0]
        fmt = '(E10.0)'
        eds, rev_eds = _parser(_lexer(fmt))
        result = "**********"
        self.assertEqual(result, _output(eds, rev_eds, inpt))

    def e_output_test_1b(self):
        '''Test where exponent is zero - note that GFortran actually crashes in this case'''
        inpt = [0.01]
        fmt = '(E10.0)'
        eds, rev_eds = _parser(_lexer(fmt))
        result = "**********"
        self.assertEqual(result, _output(eds, rev_eds, inpt))

    def e_output_test_2(self):
        inpt = [1.0]
        fmt = '(E10.1)'
        eds, rev_eds = _parser(_lexer(fmt))
        result = "   0.1E+01"
        self.assertEqual(result, _output(eds, rev_eds, inpt))

    def e_output_test_2(self):
        '''Test where exponent is zero - note that GFortran actually crashes in this case'''
        inpt = [1.0]
        fmt = '(E14.0)'
        eds, rev_eds = _parser(_lexer(fmt))
        result = "**************"
        self.assertEqual(result, _output(eds, rev_eds, inpt))

    def e_output_test_2a(self):
        '''Test where exponent is zero - note that GFortran actually crashes in this case'''
        inpt = [0.0]
        fmt = '(E14.0)'
        eds, rev_eds = _parser(_lexer(fmt))
        result = "**************"
        self.assertEqual(result, _output(eds, rev_eds, inpt))

    def e_output_test_2b(self):
        '''Test where exponent is zero - note that GFortran actually crashes in this case'''
        inpt = [0.01]
        fmt = '(E14.0)'
        eds, rev_eds = _parser(_lexer(fmt))
        result = "**************"
        self.assertEqual(result, _output(eds, rev_eds, inpt))