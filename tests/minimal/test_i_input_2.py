
import sys
import os
import unittest

# To change this, re-run 'build-unittests.py'

from fortranformat._input import input as _input
from fortranformat._lexer import lexer as _lexer
from fortranformat._parser import parser as _parser
import unittest

class IEditDescriptorBatch2TestCase(unittest.TestCase):

    def test_i_ed_input_1(self):
        inp = '''-10000'''
        fmt = '''(I5.5)'''
        expected = [-1000]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(expected, _input(eds, rev_eds, inp))

    def test_i_ed_input_2(self):
        inp = '''100000'''
        fmt = '''(I5.5)'''
        expected = [10000]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(expected, _input(eds, rev_eds, inp))

    def test_i_ed_input_3(self):
        inp = '''-100000'''
        fmt = '''(I5.5)'''
        expected = [-1000]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(expected, _input(eds, rev_eds, inp))

    def test_i_ed_input_4(self):
        inp = '''123456789'''
        fmt = '''(I5.5)'''
        expected = [12345]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(expected, _input(eds, rev_eds, inp))

    def test_i_ed_input_5(self):
        inp = ''' 0'''
        fmt = '''(I5.5)'''
        expected = [0]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(expected, _input(eds, rev_eds, inp))

    def test_i_ed_input_6(self):
        inp = '''- 0'''
        fmt = '''(I5.5)'''
        expected = [0]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(expected, _input(eds, rev_eds, inp))

    def test_i_ed_input_7(self):
        inp = '''-   001'''
        fmt = '''(I5.5)'''
        expected = [0]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(expected, _input(eds, rev_eds, inp))

    def test_i_ed_input_8(self):
        inp = '''12  012'''
        fmt = '''(I5.5)'''
        expected = [120]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(expected, _input(eds, rev_eds, inp))

    def test_i_ed_input_9(self):
        inp = '''0'''
        fmt = '''(I6.5)'''
        expected = [0]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(expected, _input(eds, rev_eds, inp))

    def test_i_ed_input_10(self):
        inp = '''-0'''
        fmt = '''(I6.5)'''
        expected = [0]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(expected, _input(eds, rev_eds, inp))


if __name__ == '__main__':
    unittest.main()