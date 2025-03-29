
import sys
import os
import unittest

# To change this, re-run 'build-unittests.py'

from fortranformat._output import output as _output
from fortranformat._lexer import lexer as _lexer
from fortranformat._parser import parser as _parser
import unittest

class AEditDescriptorBatchTestCase(unittest.TestCase):

    def test_a_ed_input_1(self):
        vals = ['''The quick brown fox jumps the lazy dog.''']
        fmt = '''(A)'''
        result = '''The quick brown fox jumps the lazy dog.'''
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _output(eds, rev_eds, vals))

    def test_a_ed_input_2(self):
        vals = ['''"It doesn\'t matter anyway" - said Alice''']
        fmt = '''(A)'''
        result = '''"It doesn\'t matter anyway" - said Alice'''
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _output(eds, rev_eds, vals))

    def test_a_ed_input_3(self):
        vals = ['''\'\'''']
        fmt = '''(A)'''
        result = '''\'\''''
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _output(eds, rev_eds, vals))

    def test_a_ed_input_4(self):
        vals = ['''The quick brown fox jumps the lazy dog.''']
        fmt = '''(A1)'''
        result = '''T'''
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _output(eds, rev_eds, vals))

    def test_a_ed_input_5(self):
        vals = ['''"It doesn\'t matter anyway" - said Alice''']
        fmt = '''(A1)'''
        result = '''"'''
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _output(eds, rev_eds, vals))

    def test_a_ed_input_6(self):
        vals = ['''\'\'''']
        fmt = '''(A1)'''
        result = '''\''''
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _output(eds, rev_eds, vals))

    def test_a_ed_input_7(self):
        vals = ['''The quick brown fox jumps the lazy dog.''']
        fmt = '''(A2)'''
        result = '''Th'''
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _output(eds, rev_eds, vals))

    def test_a_ed_input_8(self):
        vals = ['''"It doesn\'t matter anyway" - said Alice''']
        fmt = '''(A2)'''
        result = '''"I'''
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _output(eds, rev_eds, vals))

    def test_a_ed_input_9(self):
        vals = ['''\'\'''']
        fmt = '''(A2)'''
        result = '''\'\''''
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _output(eds, rev_eds, vals))

    def test_a_ed_input_10(self):
        vals = ['''The quick brown fox jumps the lazy dog.''']
        fmt = '''(A3)'''
        result = '''The'''
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _output(eds, rev_eds, vals))


if __name__ == '__main__':
    unittest.main()