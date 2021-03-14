
import sys
import os
import unittest
from nose.plugins.attrib import attr

# To change this, re-run 'build-unittests.py'

from fortranformat._output import output as _output
from fortranformat._lexer import lexer as _lexer
from fortranformat._parser import parser as _parser
import unittest

class AEditDescriptorBatchTestCase(unittest.TestCase):

    @attr(platform='9-1_linux_intel')
    @attr('output')
    @attr(ed='A')
    def test_a_ed_input_1(self):
        vals = ['''The quick brown fox jumps the lazy dog.''']
        fmt = '''(A)'''
        result = '''The quick brown fox jumps the lazy dog.'''
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _output(eds, rev_eds, vals))

    @attr(platform='9-1_linux_intel')
    @attr('output')
    @attr(ed='A')
    def test_a_ed_input_2(self):
        vals = ['''"It doesn\'t matter anyway" - said Alice''']
        fmt = '''(A)'''
        result = '''"It doesn\'t matter anyway" - said Alice'''
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _output(eds, rev_eds, vals))

    @attr(platform='9-1_linux_intel')
    @attr('output')
    @attr(ed='A')
    def test_a_ed_input_3(self):
        vals = ['''\'\'''']
        fmt = '''(A)'''
        result = '''\'\''''
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _output(eds, rev_eds, vals))

    @attr(platform='9-1_linux_intel')
    @attr('output')
    @attr(ed='A')
    def test_a_ed_input_4(self):
        vals = ['''The quick brown fox jumps the lazy dog.''']
        fmt = '''(A1)'''
        result = '''T'''
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _output(eds, rev_eds, vals))

    @attr(platform='9-1_linux_intel')
    @attr('output')
    @attr(ed='A')
    def test_a_ed_input_5(self):
        vals = ['''"It doesn\'t matter anyway" - said Alice''']
        fmt = '''(A1)'''
        result = '''"'''
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _output(eds, rev_eds, vals))

    @attr(platform='9-1_linux_intel')
    @attr('output')
    @attr(ed='A')
    def test_a_ed_input_6(self):
        vals = ['''\'\'''']
        fmt = '''(A1)'''
        result = '''\''''
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _output(eds, rev_eds, vals))

    @attr(platform='9-1_linux_intel')
    @attr('output')
    @attr(ed='A')
    def test_a_ed_input_7(self):
        vals = ['''The quick brown fox jumps the lazy dog.''']
        fmt = '''(A2)'''
        result = '''Th'''
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _output(eds, rev_eds, vals))

    @attr(platform='9-1_linux_intel')
    @attr('output')
    @attr(ed='A')
    def test_a_ed_input_8(self):
        vals = ['''"It doesn\'t matter anyway" - said Alice''']
        fmt = '''(A2)'''
        result = '''"I'''
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _output(eds, rev_eds, vals))

    @attr(platform='9-1_linux_intel')
    @attr('output')
    @attr(ed='A')
    def test_a_ed_input_9(self):
        vals = ['''\'\'''']
        fmt = '''(A2)'''
        result = '''\'\''''
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _output(eds, rev_eds, vals))

    @attr(platform='9-1_linux_intel')
    @attr('output')
    @attr(ed='A')
    def test_a_ed_input_10(self):
        vals = ['''The quick brown fox jumps the lazy dog.''']
        fmt = '''(A3)'''
        result = '''The'''
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _output(eds, rev_eds, vals))

    @attr(platform='9-1_linux_intel')
    @attr('output')
    @attr(ed='A')
    def test_a_ed_input_11(self):
        vals = ['''"It doesn\'t matter anyway" - said Alice''']
        fmt = '''(A3)'''
        result = '''"It'''
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _output(eds, rev_eds, vals))

    @attr(platform='9-1_linux_intel')
    @attr('output')
    @attr(ed='A')
    def test_a_ed_input_12(self):
        vals = ['''\'\'''']
        fmt = '''(A3)'''
        result = ''' \'\''''
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _output(eds, rev_eds, vals))

    @attr(platform='9-1_linux_intel')
    @attr('output')
    @attr(ed='A')
    def test_a_ed_input_13(self):
        vals = ['''The quick brown fox jumps the lazy dog.''']
        fmt = '''(A4)'''
        result = '''The '''
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _output(eds, rev_eds, vals))

    @attr(platform='9-1_linux_intel')
    @attr('output')
    @attr(ed='A')
    def test_a_ed_input_14(self):
        vals = ['''"It doesn\'t matter anyway" - said Alice''']
        fmt = '''(A4)'''
        result = '''"It '''
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _output(eds, rev_eds, vals))

    @attr(platform='9-1_linux_intel')
    @attr('output')
    @attr(ed='A')
    def test_a_ed_input_15(self):
        vals = ['''\'\'''']
        fmt = '''(A4)'''
        result = '''  \'\''''
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _output(eds, rev_eds, vals))

    @attr(platform='9-1_linux_intel')
    @attr('output')
    @attr(ed='A')
    def test_a_ed_input_16(self):
        vals = ['''The quick brown fox jumps the lazy dog.''']
        fmt = '''(A5)'''
        result = '''The q'''
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _output(eds, rev_eds, vals))

    @attr(platform='9-1_linux_intel')
    @attr('output')
    @attr(ed='A')
    def test_a_ed_input_17(self):
        vals = ['''"It doesn\'t matter anyway" - said Alice''']
        fmt = '''(A5)'''
        result = '''"It d'''
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _output(eds, rev_eds, vals))

    @attr(platform='9-1_linux_intel')
    @attr('output')
    @attr(ed='A')
    def test_a_ed_input_18(self):
        vals = ['''\'\'''']
        fmt = '''(A5)'''
        result = '''   \'\''''
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _output(eds, rev_eds, vals))

    @attr(platform='9-1_linux_intel')
    @attr('output')
    @attr(ed='A')
    def test_a_ed_input_19(self):
        vals = ['''The quick brown fox jumps the lazy dog.''']
        fmt = '''(A6)'''
        result = '''The qu'''
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _output(eds, rev_eds, vals))

    @attr(platform='9-1_linux_intel')
    @attr('output')
    @attr(ed='A')
    def test_a_ed_input_20(self):
        vals = ['''"It doesn\'t matter anyway" - said Alice''']
        fmt = '''(A6)'''
        result = '''"It do'''
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _output(eds, rev_eds, vals))

    @attr(platform='9-1_linux_intel')
    @attr('output')
    @attr(ed='A')
    def test_a_ed_input_21(self):
        vals = ['''\'\'''']
        fmt = '''(A6)'''
        result = '''    \'\''''
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _output(eds, rev_eds, vals))

    @attr(platform='9-1_linux_intel')
    @attr('output')
    @attr(ed='A')
    def test_a_ed_input_22(self):
        vals = ['''The quick brown fox jumps the lazy dog.''']
        fmt = '''(A7)'''
        result = '''The qui'''
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _output(eds, rev_eds, vals))

    @attr(platform='9-1_linux_intel')
    @attr('output')
    @attr(ed='A')
    def test_a_ed_input_23(self):
        vals = ['''"It doesn\'t matter anyway" - said Alice''']
        fmt = '''(A7)'''
        result = '''"It doe'''
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _output(eds, rev_eds, vals))

    @attr(platform='9-1_linux_intel')
    @attr('output')
    @attr(ed='A')
    def test_a_ed_input_24(self):
        vals = ['''\'\'''']
        fmt = '''(A7)'''
        result = '''     \'\''''
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _output(eds, rev_eds, vals))

    @attr(platform='9-1_linux_intel')
    @attr('output')
    @attr(ed='A')
    def test_a_ed_input_25(self):
        vals = ['''The quick brown fox jumps the lazy dog.''']
        fmt = '''(A8)'''
        result = '''The quic'''
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _output(eds, rev_eds, vals))

    @attr(platform='9-1_linux_intel')
    @attr('output')
    @attr(ed='A')
    def test_a_ed_input_26(self):
        vals = ['''"It doesn\'t matter anyway" - said Alice''']
        fmt = '''(A8)'''
        result = '''"It does'''
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _output(eds, rev_eds, vals))

    @attr(platform='9-1_linux_intel')
    @attr('output')
    @attr(ed='A')
    def test_a_ed_input_27(self):
        vals = ['''\'\'''']
        fmt = '''(A8)'''
        result = '''      \'\''''
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _output(eds, rev_eds, vals))

    @attr(platform='9-1_linux_intel')
    @attr('output')
    @attr(ed='A')
    def test_a_ed_input_28(self):
        vals = ['''The quick brown fox jumps the lazy dog.''']
        fmt = '''(A9)'''
        result = '''The quick'''
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _output(eds, rev_eds, vals))

    @attr(platform='9-1_linux_intel')
    @attr('output')
    @attr(ed='A')
    def test_a_ed_input_29(self):
        vals = ['''"It doesn\'t matter anyway" - said Alice''']
        fmt = '''(A9)'''
        result = '''"It doesn'''
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _output(eds, rev_eds, vals))

    @attr(platform='9-1_linux_intel')
    @attr('output')
    @attr(ed='A')
    def test_a_ed_input_30(self):
        vals = ['''\'\'''']
        fmt = '''(A9)'''
        result = '''       \'\''''
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _output(eds, rev_eds, vals))

    @attr(platform='9-1_linux_intel')
    @attr('output')
    @attr(ed='A')
    def test_a_ed_input_31(self):
        vals = ['''The quick brown fox jumps the lazy dog.''']
        fmt = '''(A10)'''
        result = '''The quick '''
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _output(eds, rev_eds, vals))

    @attr(platform='9-1_linux_intel')
    @attr('output')
    @attr(ed='A')
    def test_a_ed_input_32(self):
        vals = ['''"It doesn\'t matter anyway" - said Alice''']
        fmt = '''(A10)'''
        result = '''"It doesn\''''
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _output(eds, rev_eds, vals))

    @attr(platform='9-1_linux_intel')
    @attr('output')
    @attr(ed='A')
    def test_a_ed_input_33(self):
        vals = ['''\'\'''']
        fmt = '''(A10)'''
        result = '''        \'\''''
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _output(eds, rev_eds, vals))

    @attr(platform='9-1_linux_intel')
    @attr('output')
    @attr(ed='A')
    def test_a_ed_input_34(self):
        vals = ['''The quick brown fox jumps the lazy dog.''']
        fmt = '''(A25)'''
        result = '''The quick brown fox jumps'''
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _output(eds, rev_eds, vals))

    @attr(platform='9-1_linux_intel')
    @attr('output')
    @attr(ed='A')
    def test_a_ed_input_35(self):
        vals = ['''"It doesn\'t matter anyway" - said Alice''']
        fmt = '''(A25)'''
        result = '''"It doesn\'t matter anyway'''
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _output(eds, rev_eds, vals))

    @attr(platform='9-1_linux_intel')
    @attr('output')
    @attr(ed='A')
    def test_a_ed_input_36(self):
        vals = ['''\'\'''']
        fmt = '''(A25)'''
        result = '''                       \'\''''
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _output(eds, rev_eds, vals))

    @attr(platform='9-1_linux_intel')
    @attr('output')
    @attr(ed='A')
    def test_a_ed_input_37(self):
        vals = ['''The quick brown fox jumps the lazy dog.''']
        fmt = '''(A50)'''
        result = '''           The quick brown fox jumps the lazy dog.'''
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _output(eds, rev_eds, vals))

    @attr(platform='9-1_linux_intel')
    @attr('output')
    @attr(ed='A')
    def test_a_ed_input_38(self):
        vals = ['''"It doesn\'t matter anyway" - said Alice''']
        fmt = '''(A50)'''
        result = '''           "It doesn\'t matter anyway" - said Alice'''
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _output(eds, rev_eds, vals))

    @attr(platform='9-1_linux_intel')
    @attr('output')
    @attr(ed='A')
    def test_a_ed_input_39(self):
        vals = ['''\'\'''']
        fmt = '''(A50)'''
        result = '''                                                \'\''''
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _output(eds, rev_eds, vals))

    @attr(platform='9-1_linux_intel')
    @attr('output')
    @attr(ed='A')
    def test_a_ed_input_40(self):
        vals = ['''The quick brown fox jumps the lazy dog.''']
        fmt = '''(A100)'''
        result = '''                                                             The quick brown fox jumps the lazy dog.'''
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _output(eds, rev_eds, vals))

    @attr(platform='9-1_linux_intel')
    @attr('output')
    @attr(ed='A')
    def test_a_ed_input_41(self):
        vals = ['''"It doesn\'t matter anyway" - said Alice''']
        fmt = '''(A100)'''
        result = '''                                                             "It doesn\'t matter anyway" - said Alice'''
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _output(eds, rev_eds, vals))


if __name__ == '__main__':
    unittest.main()
