
import sys
import os
import unittest

# To change this, re-run 'build-unittests.py'

from fortranformat._output import output as _output
from fortranformat._lexer import lexer as _lexer
from fortranformat._parser import parser as _parser
import unittest

class X_LEditDescriptorBatchTestCase(unittest.TestCase):

    def test_x_l_ed_input_1(self):
        vals = [True]
        fmt = '''(1X, L1)'''
        result = ''' T'''
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _output(eds, rev_eds, vals))

    def test_x_l_ed_input_2(self):
        vals = [False]
        fmt = '''(1X, L1)'''
        result = ''' F'''
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _output(eds, rev_eds, vals))

    def test_x_l_ed_input_3(self):
        vals = [True]
        fmt = '''(1X, L2)'''
        result = '''  T'''
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _output(eds, rev_eds, vals))

    def test_x_l_ed_input_4(self):
        vals = [False]
        fmt = '''(1X, L2)'''
        result = '''  F'''
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _output(eds, rev_eds, vals))

    def test_x_l_ed_input_5(self):
        vals = [True]
        fmt = '''(1X, L3)'''
        result = '''   T'''
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _output(eds, rev_eds, vals))

    def test_x_l_ed_input_6(self):
        vals = [False]
        fmt = '''(1X, L3)'''
        result = '''   F'''
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _output(eds, rev_eds, vals))

    def test_x_l_ed_input_7(self):
        vals = [True]
        fmt = '''(1X, L4)'''
        result = '''    T'''
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _output(eds, rev_eds, vals))

    def test_x_l_ed_input_8(self):
        vals = [False]
        fmt = '''(1X, L4)'''
        result = '''    F'''
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _output(eds, rev_eds, vals))

    def test_x_l_ed_input_9(self):
        vals = [True]
        fmt = '''(1X, L5)'''
        result = '''     T'''
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _output(eds, rev_eds, vals))

    def test_x_l_ed_input_10(self):
        vals = [False]
        fmt = '''(1X, L5)'''
        result = '''     F'''
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _output(eds, rev_eds, vals))


if __name__ == '__main__':
    unittest.main()