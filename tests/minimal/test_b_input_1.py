
import sys
import os
import unittest

# To change this, re-run 'build-unittests.py'

from fortranformat._input import input as _input
from fortranformat._lexer import lexer as _lexer
from fortranformat._parser import parser as _parser
import unittest

class BEditDescriptorBatch1TestCase(unittest.TestCase):

    def test_b_ed_input_1(self):
        inp = '''0'''
        fmt = '''(B1)'''
        expected = [0]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(expected, _input(eds, rev_eds, inp))

    def test_b_ed_input_2(self):
        inp = '''-0'''
        fmt = '''(B1)'''
        expected = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    def test_b_ed_input_3(self):
        inp = '''1'''
        fmt = '''(B1)'''
        expected = [1]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(expected, _input(eds, rev_eds, inp))

    def test_b_ed_input_4(self):
        inp = '''-1'''
        fmt = '''(B1)'''
        expected = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    def test_b_ed_input_5(self):
        inp = '''2'''
        fmt = '''(B1)'''
        expected = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    def test_b_ed_input_6(self):
        inp = '''10'''
        fmt = '''(B1)'''
        expected = [1]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(expected, _input(eds, rev_eds, inp))

    def test_b_ed_input_7(self):
        inp = '''-10'''
        fmt = '''(B1)'''
        expected = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    def test_b_ed_input_8(self):
        inp = '''100'''
        fmt = '''(B1)'''
        expected = [1]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(expected, _input(eds, rev_eds, inp))

    def test_b_ed_input_9(self):
        inp = '''-100'''
        fmt = '''(B1)'''
        expected = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    def test_b_ed_input_10(self):
        inp = '''1000'''
        fmt = '''(B1)'''
        expected = [1]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(expected, _input(eds, rev_eds, inp))


if __name__ == '__main__':
    unittest.main()