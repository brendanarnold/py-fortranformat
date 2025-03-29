
import sys
import os
import unittest

# To change this, re-run 'build-unittests.py'

from fortranformat._output import output as _output
from fortranformat._lexer import lexer as _lexer
from fortranformat._parser import parser as _parser
import unittest

class BZ_BEditDescriptorBatchTestCase(unittest.TestCase):

    def test_bz_b_ed_input_1(self):
        vals = [0]
        fmt = '''(BZ, B1)'''
        result = '''0'''
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _output(eds, rev_eds, vals))

    def test_bz_b_ed_input_2(self):
        vals = [-0]
        fmt = '''(BZ, B1)'''
        result = '''0'''
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _output(eds, rev_eds, vals))

    def test_bz_b_ed_input_3(self):
        vals = [1]
        fmt = '''(BZ, B1)'''
        result = '''1'''
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _output(eds, rev_eds, vals))

    def test_bz_b_ed_input_4(self):
        vals = [-1]
        fmt = '''(BZ, B1)'''
        result = '''*'''
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _output(eds, rev_eds, vals))

    def test_bz_b_ed_input_5(self):
        vals = [3]
        fmt = '''(BZ, B1)'''
        result = '''*'''
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _output(eds, rev_eds, vals))

    def test_bz_b_ed_input_6(self):
        vals = [-3]
        fmt = '''(BZ, B1)'''
        result = '''*'''
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _output(eds, rev_eds, vals))

    def test_bz_b_ed_input_7(self):
        vals = [10]
        fmt = '''(BZ, B1)'''
        result = '''*'''
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _output(eds, rev_eds, vals))

    def test_bz_b_ed_input_8(self):
        vals = [-10]
        fmt = '''(BZ, B1)'''
        result = '''*'''
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _output(eds, rev_eds, vals))

    def test_bz_b_ed_input_9(self):
        vals = [100]
        fmt = '''(BZ, B1)'''
        result = '''*'''
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _output(eds, rev_eds, vals))

    def test_bz_b_ed_input_10(self):
        vals = [-100]
        fmt = '''(BZ, B1)'''
        result = '''*'''
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _output(eds, rev_eds, vals))


if __name__ == '__main__':
    unittest.main()