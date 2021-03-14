
import sys
import os
import unittest
from nose.plugins.attrib import attr

# To change this, re-run 'build-unittests.py'

from fortranformat._input import input as _input
from fortranformat._lexer import lexer as _lexer
from fortranformat._parser import parser as _parser
import unittest

class LEditDescriptorBatch1TestCase(unittest.TestCase):

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='L')
    def test_l_ed_input_1(self):
        inp = '''.TRUE.'''
        fmt = '''(L1)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='L')
    def test_l_ed_input_2(self):
        inp = '''.FALSE.'''
        fmt = '''(L1)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='L')
    def test_l_ed_input_3(self):
        inp = '''T'''
        fmt = '''(L1)'''
        result = [True]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='L')
    def test_l_ed_input_4(self):
        inp = '''F'''
        fmt = '''(L1)'''
        result = [False]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='L')
    def test_l_ed_input_5(self):
        inp = '''.TRUE.'''
        fmt = '''(L2)'''
        result = [True]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='L')
    def test_l_ed_input_6(self):
        inp = '''.FALSE.'''
        fmt = '''(L2)'''
        result = [False]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='L')
    def test_l_ed_input_7(self):
        inp = '''T'''
        fmt = '''(L2)'''
        result = [True]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='L')
    def test_l_ed_input_8(self):
        inp = '''F'''
        fmt = '''(L2)'''
        result = [False]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='L')
    def test_l_ed_input_9(self):
        inp = '''.TRUE.'''
        fmt = '''(L3)'''
        result = [True]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='L')
    def test_l_ed_input_10(self):
        inp = '''.FALSE.'''
        fmt = '''(L3)'''
        result = [False]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='L')
    def test_l_ed_input_11(self):
        inp = '''T'''
        fmt = '''(L3)'''
        result = [True]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='L')
    def test_l_ed_input_12(self):
        inp = '''F'''
        fmt = '''(L3)'''
        result = [False]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='L')
    def test_l_ed_input_13(self):
        inp = '''.TRUE.'''
        fmt = '''(L4)'''
        result = [True]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='L')
    def test_l_ed_input_14(self):
        inp = '''.FALSE.'''
        fmt = '''(L4)'''
        result = [False]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='L')
    def test_l_ed_input_15(self):
        inp = '''T'''
        fmt = '''(L4)'''
        result = [True]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='L')
    def test_l_ed_input_16(self):
        inp = '''F'''
        fmt = '''(L4)'''
        result = [False]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='L')
    def test_l_ed_input_17(self):
        inp = '''.TRUE.'''
        fmt = '''(L5)'''
        result = [True]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='L')
    def test_l_ed_input_18(self):
        inp = '''.FALSE.'''
        fmt = '''(L5)'''
        result = [False]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='L')
    def test_l_ed_input_19(self):
        inp = '''T'''
        fmt = '''(L5)'''
        result = [True]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='L')
    def test_l_ed_input_20(self):
        inp = '''F'''
        fmt = '''(L5)'''
        result = [False]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='L')
    def test_l_ed_input_21(self):
        inp = '''.TRUE.'''
        fmt = '''(L6)'''
        result = [True]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='L')
    def test_l_ed_input_22(self):
        inp = '''.FALSE.'''
        fmt = '''(L6)'''
        result = [False]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='L')
    def test_l_ed_input_23(self):
        inp = '''T'''
        fmt = '''(L6)'''
        result = [True]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='L')
    def test_l_ed_input_24(self):
        inp = '''F'''
        fmt = '''(L6)'''
        result = [False]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='L')
    def test_l_ed_input_25(self):
        inp = '''.TRUE.'''
        fmt = '''(L7)'''
        result = [True]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='L')
    def test_l_ed_input_26(self):
        inp = '''.FALSE.'''
        fmt = '''(L7)'''
        result = [False]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='L')
    def test_l_ed_input_27(self):
        inp = '''T'''
        fmt = '''(L7)'''
        result = [True]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='L')
    def test_l_ed_input_28(self):
        inp = '''F'''
        fmt = '''(L7)'''
        result = [False]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='L')
    def test_l_ed_input_29(self):
        inp = '''.TRUE.'''
        fmt = '''(L8)'''
        result = [True]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='L')
    def test_l_ed_input_30(self):
        inp = '''.FALSE.'''
        fmt = '''(L8)'''
        result = [False]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='L')
    def test_l_ed_input_31(self):
        inp = '''T'''
        fmt = '''(L8)'''
        result = [True]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='L')
    def test_l_ed_input_32(self):
        inp = '''F'''
        fmt = '''(L8)'''
        result = [False]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='L')
    def test_l_ed_input_33(self):
        inp = '''.TRUE.'''
        fmt = '''(L9)'''
        result = [True]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='L')
    def test_l_ed_input_34(self):
        inp = '''.FALSE.'''
        fmt = '''(L9)'''
        result = [False]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='L')
    def test_l_ed_input_35(self):
        inp = '''T'''
        fmt = '''(L9)'''
        result = [True]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='L')
    def test_l_ed_input_36(self):
        inp = '''F'''
        fmt = '''(L9)'''
        result = [False]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='L')
    def test_l_ed_input_37(self):
        inp = '''.TRUE.'''
        fmt = '''(L10)'''
        result = [True]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='L')
    def test_l_ed_input_38(self):
        inp = '''.FALSE.'''
        fmt = '''(L10)'''
        result = [False]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='L')
    def test_l_ed_input_39(self):
        inp = '''T'''
        fmt = '''(L10)'''
        result = [True]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))


if __name__ == '__main__':
    unittest.main()