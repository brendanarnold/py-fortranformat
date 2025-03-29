
import sys
import os
import unittest

# To change this, re-run 'build-unittests.py'

from fortranformat._input import input as _input
from fortranformat._lexer import lexer as _lexer
from fortranformat._parser import parser as _parser
import unittest

class LEditDescriptorBatch1TestCase(unittest.TestCase):

    def test_l_ed_input_1(self):
        inp = '''.TRUE.'''
        fmt = '''(L1)'''
        expected = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    def test_l_ed_input_2(self):
        inp = '''.FALSE.'''
        fmt = '''(L1)'''
        expected = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    def test_l_ed_input_3(self):
        inp = '''T'''
        fmt = '''(L1)'''
        expected = [True]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(expected, _input(eds, rev_eds, inp))

    def test_l_ed_input_4(self):
        inp = '''F'''
        fmt = '''(L1)'''
        expected = [False]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(expected, _input(eds, rev_eds, inp))

    def test_l_ed_input_5(self):
        inp = '''.TRUE.'''
        fmt = '''(L2)'''
        expected = [True]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(expected, _input(eds, rev_eds, inp))

    def test_l_ed_input_6(self):
        inp = '''.FALSE.'''
        fmt = '''(L2)'''
        expected = [False]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(expected, _input(eds, rev_eds, inp))

    def test_l_ed_input_7(self):
        inp = '''T'''
        fmt = '''(L2)'''
        expected = [True]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(expected, _input(eds, rev_eds, inp))

    def test_l_ed_input_8(self):
        inp = '''F'''
        fmt = '''(L2)'''
        expected = [False]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(expected, _input(eds, rev_eds, inp))

    def test_l_ed_input_9(self):
        inp = '''.TRUE.'''
        fmt = '''(L3)'''
        expected = [True]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(expected, _input(eds, rev_eds, inp))

    def test_l_ed_input_10(self):
        inp = '''.FALSE.'''
        fmt = '''(L3)'''
        expected = [False]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(expected, _input(eds, rev_eds, inp))


if __name__ == '__main__':
    unittest.main()