
import sys
import os
import unittest

# To change this, re-run 'build-unittests.py'

from fortranformat._input import input as _input
from fortranformat._lexer import lexer as _lexer
from fortranformat._parser import parser as _parser
import unittest

class EEditDescriptorBatch3TestCase(unittest.TestCase):

    def test_e_ed_input_1(self):
        inp = '''-0.0001'''
        fmt = '''(E4.1E4)'''
        expected = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(expected, _input(eds, rev_eds, inp))

    def test_e_ed_input_2(self):
        inp = '''-1.96e-16'''
        fmt = '''(E4.1E4)'''
        expected = [-1.8999999999999999e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(expected, _input(eds, rev_eds, inp))

    def test_e_ed_input_3(self):
        inp = '''3.14159'''
        fmt = '''(E4.1E4)'''
        expected = [3.1400000000000001e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(expected, _input(eds, rev_eds, inp))

    def test_e_ed_input_4(self):
        inp = '''-    1.0'''
        fmt = '''(E4.1E4)'''
        expected = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(expected, _input(eds, rev_eds, inp))

    def test_e_ed_input_5(self):
        inp = '''1e12'''
        fmt = '''(E4.1E4)'''
        expected = [1.0000000000000000e+11]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(expected, _input(eds, rev_eds, inp))

    def test_e_ed_input_6(self):
        inp = '''1E12'''
        fmt = '''(E4.1E4)'''
        expected = [1.0000000000000000e+11]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(expected, _input(eds, rev_eds, inp))

    def test_e_ed_input_7(self):
        inp = '''-1   e12'''
        fmt = '''(E4.1E4)'''
        expected = [-1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(expected, _input(eds, rev_eds, inp))

    def test_e_ed_input_8(self):
        inp = '''.'''
        fmt = '''(E4.1E4)'''
        expected = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(expected, _input(eds, rev_eds, inp))

    def test_e_ed_input_9(self):
        inp = '''.1'''
        fmt = '''(E4.1E4)'''
        expected = [1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(expected, _input(eds, rev_eds, inp))

    def test_e_ed_input_10(self):
        inp = '''0.1D+200'''
        fmt = '''(E4.1E4)'''
        expected = [1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(expected, _input(eds, rev_eds, inp))


if __name__ == '__main__':
    unittest.main()