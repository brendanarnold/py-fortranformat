
from math import nan
import unittest

from fortranformat._output import output as _output
from fortranformat._lexer import lexer as _lexer
from fortranformat._parser import parser as _parser
import fortranformat.config as config


class FEdTests(unittest.TestCase):

    def setUp(self):
        config.reset()

    def test_1(self):
        '''Output an appropriate value if the value is NaN'''
        inpt = [float('nan')]
        fmt = '(F5.0)'
        eds, rev_eds = _parser(_lexer(fmt))
        result = '  NaN'
        self.assertEqual(result, _output(eds, rev_eds, inpt))

    def test_2(self):
        '''Output an appropriate value if the value is Infinity'''
        inpt = [float('Inf')]
        fmt = '(F5.0)'
        eds, rev_eds = _parser(_lexer(fmt))
        result = ' +Inf'
        self.assertEqual(result, _output(eds, rev_eds, inpt))

    def test_3(self):
        '''Output an appropriate value if the value is -Infinity'''
        inpt = [float('-Inf')]
        fmt = '(F5.0)'
        eds, rev_eds = _parser(_lexer(fmt))
        result = ' -Inf'
        self.assertEqual(result, _output(eds, rev_eds, inpt))
