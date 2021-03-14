
import sys
import os
import unittest
from nose.plugins.attrib import attr

# To change this, re-run 'build-unittests.py'

from fortranformat._input import input as _input
from fortranformat._lexer import lexer as _lexer
from fortranformat._parser import parser as _parser
import unittest

class ENEditDescriptorBatch4TestCase(unittest.TestCase):

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_1(self):
        inp = '''3.'''
        fmt = '''(EN5.4E5)'''
        result = [3.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_2(self):
        inp = '''-3.'''
        fmt = '''(EN5.4E5)'''
        result = [-3.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_3(self):
        inp = '''10.'''
        fmt = '''(EN5.4E5)'''
        result = [1.0000000000000000e+01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_4(self):
        inp = '''-10.'''
        fmt = '''(EN5.4E5)'''
        result = [-1.0000000000000000e+01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_5(self):
        inp = '''100.'''
        fmt = '''(EN5.4E5)'''
        result = [1.0000000000000000e+02]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_6(self):
        inp = '''-100.'''
        fmt = '''(EN5.4E5)'''
        result = [-1.0000000000000000e+02]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_7(self):
        inp = '''1000.'''
        fmt = '''(EN5.4E5)'''
        result = [1.0000000000000000e+03]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_8(self):
        inp = '''-1000.'''
        fmt = '''(EN5.4E5)'''
        result = [-1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_9(self):
        inp = '''10000.'''
        fmt = '''(EN5.4E5)'''
        result = [1.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_10(self):
        inp = '''-10000.'''
        fmt = '''(EN5.4E5)'''
        result = [-1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_11(self):
        inp = '''100000.'''
        fmt = '''(EN5.4E5)'''
        result = [1.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_12(self):
        inp = '''-100000.'''
        fmt = '''(EN5.4E5)'''
        result = [-1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_13(self):
        inp = '''123456789.'''
        fmt = '''(EN5.4E5)'''
        result = [1.2344999999999999e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_14(self):
        inp = '''0.1'''
        fmt = '''(EN5.4E5)'''
        result = [1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_15(self):
        inp = '''-0.1'''
        fmt = '''(EN5.4E5)'''
        result = [-1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_16(self):
        inp = '''0.01'''
        fmt = '''(EN5.4E5)'''
        result = [1.0000000000000000e-02]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_17(self):
        inp = '''-0.01'''
        fmt = '''(EN5.4E5)'''
        result = [-1.0000000000000000e-02]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_18(self):
        inp = '''0.001'''
        fmt = '''(EN5.4E5)'''
        result = [1.0000000000000000e-03]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_19(self):
        inp = '''-0.001'''
        fmt = '''(EN5.4E5)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_20(self):
        inp = '''0.0001'''
        fmt = '''(EN5.4E5)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_21(self):
        inp = '''-0.0001'''
        fmt = '''(EN5.4E5)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_22(self):
        inp = '''-1.96e-16'''
        fmt = '''(EN5.4E5)'''
        result = [-1.9600000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_23(self):
        inp = '''3.14159'''
        fmt = '''(EN5.4E5)'''
        result = [3.1410000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_24(self):
        inp = '''-    1.0'''
        fmt = '''(EN5.4E5)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_25(self):
        inp = '''1e12'''
        fmt = '''(EN5.4E5)'''
        result = [1.0000000000000000e+08]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_26(self):
        inp = '''1E12'''
        fmt = '''(EN5.4E5)'''
        result = [1.0000000000000000e+08]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_27(self):
        inp = '''-1   e12'''
        fmt = '''(EN5.4E5)'''
        result = [-1.0000000000000000e-04]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_28(self):
        inp = '''.'''
        fmt = '''(EN5.4E5)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_29(self):
        inp = '''.1'''
        fmt = '''(EN5.4E5)'''
        result = [1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_30(self):
        inp = '''0.1D+200'''
        fmt = '''(EN5.4E5)'''
        result = [1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_31(self):
        inp = '''3.'''
        fmt = '''(EN10.4E5)'''
        result = [3.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_32(self):
        inp = '''-3.'''
        fmt = '''(EN10.4E5)'''
        result = [-3.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_33(self):
        inp = '''10.'''
        fmt = '''(EN10.4E5)'''
        result = [1.0000000000000000e+01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_34(self):
        inp = '''-10.'''
        fmt = '''(EN10.4E5)'''
        result = [-1.0000000000000000e+01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_35(self):
        inp = '''100.'''
        fmt = '''(EN10.4E5)'''
        result = [1.0000000000000000e+02]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_36(self):
        inp = '''-100.'''
        fmt = '''(EN10.4E5)'''
        result = [-1.0000000000000000e+02]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_37(self):
        inp = '''1000.'''
        fmt = '''(EN10.4E5)'''
        result = [1.0000000000000000e+03]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_38(self):
        inp = '''-1000.'''
        fmt = '''(EN10.4E5)'''
        result = [-1.0000000000000000e+03]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_39(self):
        inp = '''10000.'''
        fmt = '''(EN10.4E5)'''
        result = [1.0000000000000000e+04]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_40(self):
        inp = '''-10000.'''
        fmt = '''(EN10.4E5)'''
        result = [-1.0000000000000000e+04]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_41(self):
        inp = '''100000.'''
        fmt = '''(EN10.4E5)'''
        result = [1.0000000000000000e+05]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_42(self):
        inp = '''-100000.'''
        fmt = '''(EN10.4E5)'''
        result = [-1.0000000000000000e+05]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_43(self):
        inp = '''123456789.'''
        fmt = '''(EN10.4E5)'''
        result = [1.2345678900000000e+08]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_44(self):
        inp = '''0.1'''
        fmt = '''(EN10.4E5)'''
        result = [1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_45(self):
        inp = '''-0.1'''
        fmt = '''(EN10.4E5)'''
        result = [-1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_46(self):
        inp = '''0.01'''
        fmt = '''(EN10.4E5)'''
        result = [1.0000000000000000e-02]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_47(self):
        inp = '''-0.01'''
        fmt = '''(EN10.4E5)'''
        result = [-1.0000000000000000e-02]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_48(self):
        inp = '''0.001'''
        fmt = '''(EN10.4E5)'''
        result = [1.0000000000000000e-03]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_49(self):
        inp = '''-0.001'''
        fmt = '''(EN10.4E5)'''
        result = [-1.0000000000000000e-03]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_50(self):
        inp = '''0.0001'''
        fmt = '''(EN10.4E5)'''
        result = [1.0000000000000000e-04]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_51(self):
        inp = '''-0.0001'''
        fmt = '''(EN10.4E5)'''
        result = [-1.0000000000000000e-04]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_52(self):
        inp = '''-1.96e-16'''
        fmt = '''(EN10.4E5)'''
        result = [-1.9600000000000000e-16]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_53(self):
        inp = '''3.14159'''
        fmt = '''(EN10.4E5)'''
        result = [3.1415899999999999e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_54(self):
        inp = '''-    1.0'''
        fmt = '''(EN10.4E5)'''
        result = [-1.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_55(self):
        inp = '''1e12'''
        fmt = '''(EN10.4E5)'''
        result = [1.0000000000000000e+08]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_56(self):
        inp = '''1E12'''
        fmt = '''(EN10.4E5)'''
        result = [1.0000000000000000e+08]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_57(self):
        inp = '''-1   e12'''
        fmt = '''(EN10.4E5)'''
        result = [-1.0000000000000000e+08]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_58(self):
        inp = '''.'''
        fmt = '''(EN10.4E5)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_59(self):
        inp = '''.1'''
        fmt = '''(EN10.4E5)'''
        result = [1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_60(self):
        inp = '''0.1D+200'''
        fmt = '''(EN10.4E5)'''
        result = [1.0000000000000001e+199]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_61(self):
        inp = '''3.'''
        fmt = '''(EN5.5E5)'''
        result = [3.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_62(self):
        inp = '''-3.'''
        fmt = '''(EN5.5E5)'''
        result = [-3.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_63(self):
        inp = '''10.'''
        fmt = '''(EN5.5E5)'''
        result = [1.0000000000000000e+01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_64(self):
        inp = '''-10.'''
        fmt = '''(EN5.5E5)'''
        result = [-1.0000000000000000e+01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_65(self):
        inp = '''100.'''
        fmt = '''(EN5.5E5)'''
        result = [1.0000000000000000e+02]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_66(self):
        inp = '''-100.'''
        fmt = '''(EN5.5E5)'''
        result = [-1.0000000000000000e+02]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_67(self):
        inp = '''1000.'''
        fmt = '''(EN5.5E5)'''
        result = [1.0000000000000000e+03]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_68(self):
        inp = '''-1000.'''
        fmt = '''(EN5.5E5)'''
        result = [-1.0000000000000000e-02]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_69(self):
        inp = '''10000.'''
        fmt = '''(EN5.5E5)'''
        result = [1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_70(self):
        inp = '''-10000.'''
        fmt = '''(EN5.5E5)'''
        result = [-1.0000000000000000e-02]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_71(self):
        inp = '''100000.'''
        fmt = '''(EN5.5E5)'''
        result = [1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_72(self):
        inp = '''-100000.'''
        fmt = '''(EN5.5E5)'''
        result = [-1.0000000000000000e-02]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_73(self):
        inp = '''123456789.'''
        fmt = '''(EN5.5E5)'''
        result = [1.2345000000000000e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_74(self):
        inp = '''0.1'''
        fmt = '''(EN5.5E5)'''
        result = [1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_75(self):
        inp = '''-0.1'''
        fmt = '''(EN5.5E5)'''
        result = [-1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_76(self):
        inp = '''0.01'''
        fmt = '''(EN5.5E5)'''
        result = [1.0000000000000000e-02]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_77(self):
        inp = '''-0.01'''
        fmt = '''(EN5.5E5)'''
        result = [-1.0000000000000000e-02]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_78(self):
        inp = '''0.001'''
        fmt = '''(EN5.5E5)'''
        result = [1.0000000000000000e-03]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_79(self):
        inp = '''-0.001'''
        fmt = '''(EN5.5E5)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_80(self):
        inp = '''0.0001'''
        fmt = '''(EN5.5E5)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_81(self):
        inp = '''-0.0001'''
        fmt = '''(EN5.5E5)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_82(self):
        inp = '''-1.96e-16'''
        fmt = '''(EN5.5E5)'''
        result = [-1.9600000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_83(self):
        inp = '''3.14159'''
        fmt = '''(EN5.5E5)'''
        result = [3.1410000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_84(self):
        inp = '''-    1.0'''
        fmt = '''(EN5.5E5)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_85(self):
        inp = '''1e12'''
        fmt = '''(EN5.5E5)'''
        result = [1.0000000000000000e+07]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_86(self):
        inp = '''1E12'''
        fmt = '''(EN5.5E5)'''
        result = [1.0000000000000000e+07]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_87(self):
        inp = '''-1   e12'''
        fmt = '''(EN5.5E5)'''
        result = [-1.0000000000000001e-05]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_88(self):
        inp = '''.'''
        fmt = '''(EN5.5E5)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_89(self):
        inp = '''.1'''
        fmt = '''(EN5.5E5)'''
        result = [1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_90(self):
        inp = '''0.1D+200'''
        fmt = '''(EN5.5E5)'''
        result = [1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_91(self):
        inp = '''3.'''
        fmt = '''(EN10.5E5)'''
        result = [3.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_92(self):
        inp = '''-3.'''
        fmt = '''(EN10.5E5)'''
        result = [-3.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_93(self):
        inp = '''10.'''
        fmt = '''(EN10.5E5)'''
        result = [1.0000000000000000e+01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_94(self):
        inp = '''-10.'''
        fmt = '''(EN10.5E5)'''
        result = [-1.0000000000000000e+01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_95(self):
        inp = '''100.'''
        fmt = '''(EN10.5E5)'''
        result = [1.0000000000000000e+02]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_96(self):
        inp = '''-100.'''
        fmt = '''(EN10.5E5)'''
        result = [-1.0000000000000000e+02]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_97(self):
        inp = '''1000.'''
        fmt = '''(EN10.5E5)'''
        result = [1.0000000000000000e+03]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_98(self):
        inp = '''-1000.'''
        fmt = '''(EN10.5E5)'''
        result = [-1.0000000000000000e+03]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_99(self):
        inp = '''10000.'''
        fmt = '''(EN10.5E5)'''
        result = [1.0000000000000000e+04]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_100(self):
        inp = '''-10000.'''
        fmt = '''(EN10.5E5)'''
        result = [-1.0000000000000000e+04]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_101(self):
        inp = '''100000.'''
        fmt = '''(EN10.5E5)'''
        result = [1.0000000000000000e+05]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_102(self):
        inp = '''-100000.'''
        fmt = '''(EN10.5E5)'''
        result = [-1.0000000000000000e+05]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_103(self):
        inp = '''123456789.'''
        fmt = '''(EN10.5E5)'''
        result = [1.2345678900000000e+08]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_104(self):
        inp = '''0.1'''
        fmt = '''(EN10.5E5)'''
        result = [1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_105(self):
        inp = '''-0.1'''
        fmt = '''(EN10.5E5)'''
        result = [-1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_106(self):
        inp = '''0.01'''
        fmt = '''(EN10.5E5)'''
        result = [1.0000000000000000e-02]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_107(self):
        inp = '''-0.01'''
        fmt = '''(EN10.5E5)'''
        result = [-1.0000000000000000e-02]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_108(self):
        inp = '''0.001'''
        fmt = '''(EN10.5E5)'''
        result = [1.0000000000000000e-03]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_109(self):
        inp = '''-0.001'''
        fmt = '''(EN10.5E5)'''
        result = [-1.0000000000000000e-03]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_110(self):
        inp = '''0.0001'''
        fmt = '''(EN10.5E5)'''
        result = [1.0000000000000000e-04]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_111(self):
        inp = '''-0.0001'''
        fmt = '''(EN10.5E5)'''
        result = [-1.0000000000000000e-04]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_112(self):
        inp = '''-1.96e-16'''
        fmt = '''(EN10.5E5)'''
        result = [-1.9600000000000000e-16]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_113(self):
        inp = '''3.14159'''
        fmt = '''(EN10.5E5)'''
        result = [3.1415899999999999e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_114(self):
        inp = '''-    1.0'''
        fmt = '''(EN10.5E5)'''
        result = [-1.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_115(self):
        inp = '''1e12'''
        fmt = '''(EN10.5E5)'''
        result = [1.0000000000000000e+07]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_116(self):
        inp = '''1E12'''
        fmt = '''(EN10.5E5)'''
        result = [1.0000000000000000e+07]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_117(self):
        inp = '''-1   e12'''
        fmt = '''(EN10.5E5)'''
        result = [-1.0000000000000000e+07]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_118(self):
        inp = '''.'''
        fmt = '''(EN10.5E5)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_119(self):
        inp = '''.1'''
        fmt = '''(EN10.5E5)'''
        result = [1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_120(self):
        inp = '''0.1D+200'''
        fmt = '''(EN10.5E5)'''
        result = [1.0000000000000001e+199]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_121(self):
        inp = '''3.'''
        fmt = '''(EN10.10E5)'''
        result = [3.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_122(self):
        inp = '''-3.'''
        fmt = '''(EN10.10E5)'''
        result = [-3.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_123(self):
        inp = '''10.'''
        fmt = '''(EN10.10E5)'''
        result = [1.0000000000000000e+01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_124(self):
        inp = '''-10.'''
        fmt = '''(EN10.10E5)'''
        result = [-1.0000000000000000e+01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_125(self):
        inp = '''100.'''
        fmt = '''(EN10.10E5)'''
        result = [1.0000000000000000e+02]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_126(self):
        inp = '''-100.'''
        fmt = '''(EN10.10E5)'''
        result = [-1.0000000000000000e+02]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_127(self):
        inp = '''1000.'''
        fmt = '''(EN10.10E5)'''
        result = [1.0000000000000000e+03]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_128(self):
        inp = '''-1000.'''
        fmt = '''(EN10.10E5)'''
        result = [-1.0000000000000000e+03]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_129(self):
        inp = '''10000.'''
        fmt = '''(EN10.10E5)'''
        result = [1.0000000000000000e+04]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_130(self):
        inp = '''-10000.'''
        fmt = '''(EN10.10E5)'''
        result = [-1.0000000000000000e+04]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_131(self):
        inp = '''100000.'''
        fmt = '''(EN10.10E5)'''
        result = [1.0000000000000000e+05]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_132(self):
        inp = '''-100000.'''
        fmt = '''(EN10.10E5)'''
        result = [-1.0000000000000000e+05]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_133(self):
        inp = '''123456789.'''
        fmt = '''(EN10.10E5)'''
        result = [1.2345678900000000e+08]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_134(self):
        inp = '''0.1'''
        fmt = '''(EN10.10E5)'''
        result = [1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_135(self):
        inp = '''-0.1'''
        fmt = '''(EN10.10E5)'''
        result = [-1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_136(self):
        inp = '''0.01'''
        fmt = '''(EN10.10E5)'''
        result = [1.0000000000000000e-02]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_137(self):
        inp = '''-0.01'''
        fmt = '''(EN10.10E5)'''
        result = [-1.0000000000000000e-02]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_138(self):
        inp = '''0.001'''
        fmt = '''(EN10.10E5)'''
        result = [1.0000000000000000e-03]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_139(self):
        inp = '''-0.001'''
        fmt = '''(EN10.10E5)'''
        result = [-1.0000000000000000e-03]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_140(self):
        inp = '''0.0001'''
        fmt = '''(EN10.10E5)'''
        result = [1.0000000000000000e-04]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_141(self):
        inp = '''-0.0001'''
        fmt = '''(EN10.10E5)'''
        result = [-1.0000000000000000e-04]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_142(self):
        inp = '''-1.96e-16'''
        fmt = '''(EN10.10E5)'''
        result = [-1.9600000000000000e-16]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_143(self):
        inp = '''3.14159'''
        fmt = '''(EN10.10E5)'''
        result = [3.1415899999999999e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_144(self):
        inp = '''-    1.0'''
        fmt = '''(EN10.10E5)'''
        result = [-1.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_145(self):
        inp = '''1e12'''
        fmt = '''(EN10.10E5)'''
        result = [1.0000000000000000e+02]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_146(self):
        inp = '''1E12'''
        fmt = '''(EN10.10E5)'''
        result = [1.0000000000000000e+02]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_147(self):
        inp = '''-1   e12'''
        fmt = '''(EN10.10E5)'''
        result = [-1.0000000000000000e+02]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_148(self):
        inp = '''.'''
        fmt = '''(EN10.10E5)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='EN')
    def test_en_ed_input_149(self):
        inp = '''.1'''
        fmt = '''(EN10.10E5)'''
        result = [1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))


if __name__ == '__main__':
    unittest.main()