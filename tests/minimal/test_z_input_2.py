
import sys
import os
import unittest

# To change this, re-run 'build-unittests.py'

from fortranformat._input import input as _input
from fortranformat._lexer import lexer as _lexer
from fortranformat._parser import parser as _parser
import unittest

class ZEditDescriptorBatch2TestCase(unittest.TestCase):

    def test_z_ed_input_1(self):
        inp = '''1000'''
        fmt = '''(Z9.3)'''
        expected = [4096]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(expected, _input(eds, rev_eds, inp))

    def test_z_ed_input_2(self):
        inp = '''-1000'''
        fmt = '''(Z9.3)'''
        expected = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    def test_z_ed_input_3(self):
        inp = '''10000'''
        fmt = '''(Z9.3)'''
        expected = [65536]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(expected, _input(eds, rev_eds, inp))

    def test_z_ed_input_4(self):
        inp = '''-10000'''
        fmt = '''(Z9.3)'''
        expected = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    def test_z_ed_input_5(self):
        inp = '''100000'''
        fmt = '''(Z9.3)'''
        expected = [1048576]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(expected, _input(eds, rev_eds, inp))

    def test_z_ed_input_6(self):
        inp = '''-100000'''
        fmt = '''(Z9.3)'''
        expected = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    def test_z_ed_input_7(self):
        inp = '''123456789'''
        fmt = '''(Z9.3)'''
        expected = [4886718345]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(expected, _input(eds, rev_eds, inp))

    def test_z_ed_input_8(self):
        inp = '''ff'''
        fmt = '''(Z9.3)'''
        expected = [255]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(expected, _input(eds, rev_eds, inp))

    def test_z_ed_input_9(self):
        inp = '''F'''
        fmt = '''(Z9.3)'''
        expected = [15]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(expected, _input(eds, rev_eds, inp))

    def test_z_ed_input_10(self):
        inp = ''' F F F'''
        fmt = '''(Z9.3)'''
        expected = [4095]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(expected, _input(eds, rev_eds, inp))


if __name__ == '__main__':
    unittest.main()