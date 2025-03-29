
import sys
import os
import unittest

# To change this, re-run 'build-unittests.py'

from fortranformat._input import input as _input
from fortranformat._lexer import lexer as _lexer
from fortranformat._parser import parser as _parser
import unittest

class ESEditDescriptorBatch2TestCase(unittest.TestCase):

    def test_es_ed_input_1(self):
        inp = '''100000.'''
        fmt = '''(ES4.3E1)'''
        expected = [1.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(expected, _input(eds, rev_eds, inp))

    def test_es_ed_input_2(self):
        inp = '''-100000.'''
        fmt = '''(ES4.3E1)'''
        expected = [-1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(expected, _input(eds, rev_eds, inp))

    def test_es_ed_input_3(self):
        inp = '''123456789.'''
        fmt = '''(ES4.3E1)'''
        expected = [1.2340000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(expected, _input(eds, rev_eds, inp))

    def test_es_ed_input_4(self):
        inp = '''0.1'''
        fmt = '''(ES4.3E1)'''
        expected = [1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(expected, _input(eds, rev_eds, inp))

    def test_es_ed_input_5(self):
        inp = '''-0.1'''
        fmt = '''(ES4.3E1)'''
        expected = [-1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(expected, _input(eds, rev_eds, inp))

    def test_es_ed_input_6(self):
        inp = '''0.01'''
        fmt = '''(ES4.3E1)'''
        expected = [1.0000000000000000e-02]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(expected, _input(eds, rev_eds, inp))

    def test_es_ed_input_7(self):
        inp = '''-0.01'''
        fmt = '''(ES4.3E1)'''
        expected = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(expected, _input(eds, rev_eds, inp))

    def test_es_ed_input_8(self):
        inp = '''0.001'''
        fmt = '''(ES4.3E1)'''
        expected = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(expected, _input(eds, rev_eds, inp))

    def test_es_ed_input_9(self):
        inp = '''-0.001'''
        fmt = '''(ES4.3E1)'''
        expected = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(expected, _input(eds, rev_eds, inp))

    def test_es_ed_input_10(self):
        inp = '''0.0001'''
        fmt = '''(ES4.3E1)'''
        expected = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(expected, _input(eds, rev_eds, inp))


if __name__ == '__main__':
    unittest.main()