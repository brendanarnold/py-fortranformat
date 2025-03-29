
import sys
import os
import unittest

# To change this, re-run 'build-unittests.py'

from fortranformat._output import output as _output
from fortranformat._lexer import lexer as _lexer
from fortranformat._parser import parser as _parser
import unittest

class SS_AEditDescriptorBatchTestCase(unittest.TestCase):

    def test_ss_a_ed_input_1(self):
        vals = ['''The quick brown fox jumps the lazy dog.''']
        fmt = '''(SS, A)'''
        result = '''The quick brown fox jumps the lazy dog.'''
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _output(eds, rev_eds, vals))

    def test_ss_a_ed_input_2(self):
        vals = ['''"It doesn\'t matter anyway" - said Alice''']
        fmt = '''(SS, A)'''
        result = '''"It doesn\'t matter anyway" - said Alice'''
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _output(eds, rev_eds, vals))

    def test_ss_a_ed_input_3(self):
        vals = ['''\'\'''']
        fmt = '''(SS, A)'''
        result = '''\'\''''
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _output(eds, rev_eds, vals))

    def test_ss_a_ed_input_4(self):
        vals = ['''The quick brown fox jumps the lazy dog.''']
        fmt = '''(SS, A1)'''
        result = '''T'''
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _output(eds, rev_eds, vals))

    def test_ss_a_ed_input_5(self):
        vals = ['''"It doesn\'t matter anyway" - said Alice''']
        fmt = '''(SS, A1)'''
        result = '''"'''
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _output(eds, rev_eds, vals))

    def test_ss_a_ed_input_6(self):
        vals = ['''\'\'''']
        fmt = '''(SS, A1)'''
        result = '''\''''
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _output(eds, rev_eds, vals))

    def test_ss_a_ed_input_7(self):
        vals = ['''The quick brown fox jumps the lazy dog.''']
        fmt = '''(SS, A2)'''
        result = '''Th'''
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _output(eds, rev_eds, vals))

    def test_ss_a_ed_input_8(self):
        vals = ['''"It doesn\'t matter anyway" - said Alice''']
        fmt = '''(SS, A2)'''
        result = '''"I'''
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _output(eds, rev_eds, vals))

    def test_ss_a_ed_input_9(self):
        vals = ['''\'\'''']
        fmt = '''(SS, A2)'''
        result = '''\'\''''
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _output(eds, rev_eds, vals))

    def test_ss_a_ed_input_10(self):
        vals = ['''The quick brown fox jumps the lazy dog.''']
        fmt = '''(SS, A3)'''
        result = '''The'''
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _output(eds, rev_eds, vals))


if __name__ == '__main__':
    unittest.main()