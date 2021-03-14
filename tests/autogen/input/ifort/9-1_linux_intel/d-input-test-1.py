
import sys
import os
import unittest
from nose.plugins.attrib import attr

# To change this, re-run 'build-unittests.py'

from fortranformat._input import input as _input
from fortranformat._lexer import lexer as _lexer
from fortranformat._parser import parser as _parser
import unittest

class DEditDescriptorBatch1TestCase(unittest.TestCase):

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_1(self):
        inp = '''3.'''
        fmt = '''(D1.1)'''
        result = [2.9999999999999999e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_2(self):
        inp = '''-3.'''
        fmt = '''(D1.1)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_3(self):
        inp = '''10.'''
        fmt = '''(D1.1)'''
        result = [1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_4(self):
        inp = '''-10.'''
        fmt = '''(D1.1)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_5(self):
        inp = '''100.'''
        fmt = '''(D1.1)'''
        result = [1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_6(self):
        inp = '''-100.'''
        fmt = '''(D1.1)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_7(self):
        inp = '''1000.'''
        fmt = '''(D1.1)'''
        result = [1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_8(self):
        inp = '''-1000.'''
        fmt = '''(D1.1)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_9(self):
        inp = '''10000.'''
        fmt = '''(D1.1)'''
        result = [1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_10(self):
        inp = '''-10000.'''
        fmt = '''(D1.1)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_11(self):
        inp = '''100000.'''
        fmt = '''(D1.1)'''
        result = [1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_12(self):
        inp = '''-100000.'''
        fmt = '''(D1.1)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_13(self):
        inp = '''123456789.'''
        fmt = '''(D1.1)'''
        result = [1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_14(self):
        inp = '''0.1'''
        fmt = '''(D1.1)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_15(self):
        inp = '''-0.1'''
        fmt = '''(D1.1)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_16(self):
        inp = '''0.01'''
        fmt = '''(D1.1)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_17(self):
        inp = '''-0.01'''
        fmt = '''(D1.1)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_18(self):
        inp = '''0.001'''
        fmt = '''(D1.1)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_19(self):
        inp = '''-0.001'''
        fmt = '''(D1.1)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_20(self):
        inp = '''0.0001'''
        fmt = '''(D1.1)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_21(self):
        inp = '''-0.0001'''
        fmt = '''(D1.1)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_22(self):
        inp = '''-1.96e-16'''
        fmt = '''(D1.1)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_23(self):
        inp = '''3.14159-    1.0'''
        fmt = '''(D1.1)'''
        result = [2.9999999999999999e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_24(self):
        inp = '''1d12'''
        fmt = '''(D1.1)'''
        result = [1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_25(self):
        inp = '''1D12'''
        fmt = '''(D1.1)'''
        result = [1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_26(self):
        inp = '''-1   d12'''
        fmt = '''(D1.1)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_27(self):
        inp = '''.'''
        fmt = '''(D1.1)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_28(self):
        inp = '''.1'''
        fmt = '''(D1.1)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_29(self):
        inp = '''0.1E+200'''
        fmt = '''(D1.1)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_30(self):
        inp = '''3.'''
        fmt = '''(D2.1)'''
        result = [3.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_31(self):
        inp = '''-3.'''
        fmt = '''(D2.1)'''
        result = [-2.9999999999999999e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_32(self):
        inp = '''10.'''
        fmt = '''(D2.1)'''
        result = [1.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_33(self):
        inp = '''-10.'''
        fmt = '''(D2.1)'''
        result = [-1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_34(self):
        inp = '''100.'''
        fmt = '''(D2.1)'''
        result = [1.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_35(self):
        inp = '''-100.'''
        fmt = '''(D2.1)'''
        result = [-1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_36(self):
        inp = '''1000.'''
        fmt = '''(D2.1)'''
        result = [1.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_37(self):
        inp = '''-1000.'''
        fmt = '''(D2.1)'''
        result = [-1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_38(self):
        inp = '''10000.'''
        fmt = '''(D2.1)'''
        result = [1.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_39(self):
        inp = '''-10000.'''
        fmt = '''(D2.1)'''
        result = [-1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_40(self):
        inp = '''100000.'''
        fmt = '''(D2.1)'''
        result = [1.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_41(self):
        inp = '''-100000.'''
        fmt = '''(D2.1)'''
        result = [-1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_42(self):
        inp = '''123456789.'''
        fmt = '''(D2.1)'''
        result = [1.2000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_43(self):
        inp = '''0.1'''
        fmt = '''(D2.1)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_44(self):
        inp = '''-0.1'''
        fmt = '''(D2.1)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_45(self):
        inp = '''0.01'''
        fmt = '''(D2.1)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_46(self):
        inp = '''-0.01'''
        fmt = '''(D2.1)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_47(self):
        inp = '''0.001'''
        fmt = '''(D2.1)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_48(self):
        inp = '''-0.001'''
        fmt = '''(D2.1)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_49(self):
        inp = '''0.0001'''
        fmt = '''(D2.1)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_50(self):
        inp = '''-0.0001'''
        fmt = '''(D2.1)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_51(self):
        inp = '''-1.96e-16'''
        fmt = '''(D2.1)'''
        result = [-1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_52(self):
        inp = '''3.14159-    1.0'''
        fmt = '''(D2.1)'''
        result = [3.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_53(self):
        inp = '''1d12'''
        fmt = '''(D2.1)'''
        result = [1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_54(self):
        inp = '''1D12'''
        fmt = '''(D2.1)'''
        result = [1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_55(self):
        inp = '''-1   d12'''
        fmt = '''(D2.1)'''
        result = [-1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_56(self):
        inp = '''.'''
        fmt = '''(D2.1)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_57(self):
        inp = '''.1'''
        fmt = '''(D2.1)'''
        result = [1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_58(self):
        inp = '''0.1E+200'''
        fmt = '''(D2.1)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_59(self):
        inp = '''3.'''
        fmt = '''(D3.1)'''
        result = [3.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_60(self):
        inp = '''-3.'''
        fmt = '''(D3.1)'''
        result = [-3.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_61(self):
        inp = '''10.'''
        fmt = '''(D3.1)'''
        result = [1.0000000000000000e+01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_62(self):
        inp = '''-10.'''
        fmt = '''(D3.1)'''
        result = [-1.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_63(self):
        inp = '''100.'''
        fmt = '''(D3.1)'''
        result = [1.0000000000000000e+01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_64(self):
        inp = '''-100.'''
        fmt = '''(D3.1)'''
        result = [-1.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_65(self):
        inp = '''1000.'''
        fmt = '''(D3.1)'''
        result = [1.0000000000000000e+01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_66(self):
        inp = '''-1000.'''
        fmt = '''(D3.1)'''
        result = [-1.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_67(self):
        inp = '''10000.'''
        fmt = '''(D3.1)'''
        result = [1.0000000000000000e+01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_68(self):
        inp = '''-10000.'''
        fmt = '''(D3.1)'''
        result = [-1.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_69(self):
        inp = '''100000.'''
        fmt = '''(D3.1)'''
        result = [1.0000000000000000e+01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_70(self):
        inp = '''-100000.'''
        fmt = '''(D3.1)'''
        result = [-1.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_71(self):
        inp = '''123456789.'''
        fmt = '''(D3.1)'''
        result = [1.2300000000000001e+01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_72(self):
        inp = '''0.1'''
        fmt = '''(D3.1)'''
        result = [1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_73(self):
        inp = '''-0.1'''
        fmt = '''(D3.1)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_74(self):
        inp = '''0.01'''
        fmt = '''(D3.1)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_75(self):
        inp = '''-0.01'''
        fmt = '''(D3.1)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_76(self):
        inp = '''0.001'''
        fmt = '''(D3.1)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_77(self):
        inp = '''-0.001'''
        fmt = '''(D3.1)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_78(self):
        inp = '''0.0001'''
        fmt = '''(D3.1)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_79(self):
        inp = '''-0.0001'''
        fmt = '''(D3.1)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_80(self):
        inp = '''-1.96e-16'''
        fmt = '''(D3.1)'''
        result = [-1.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_81(self):
        inp = '''3.14159-    1.0'''
        fmt = '''(D3.1)'''
        result = [3.1000000000000001e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_82(self):
        inp = '''1d12'''
        fmt = '''(D3.1)'''
        result = [1.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_83(self):
        inp = '''1D12'''
        fmt = '''(D3.1)'''
        result = [1.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_84(self):
        inp = '''-1   d12'''
        fmt = '''(D3.1)'''
        result = [-1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_85(self):
        inp = '''.'''
        fmt = '''(D3.1)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_86(self):
        inp = '''.1'''
        fmt = '''(D3.1)'''
        result = [1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_87(self):
        inp = '''0.1E+200'''
        fmt = '''(D3.1)'''
        result = [1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_88(self):
        inp = '''3.'''
        fmt = '''(D4.1)'''
        result = [3.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_89(self):
        inp = '''-3.'''
        fmt = '''(D4.1)'''
        result = [-3.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_90(self):
        inp = '''10.'''
        fmt = '''(D4.1)'''
        result = [1.0000000000000000e+01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_91(self):
        inp = '''-10.'''
        fmt = '''(D4.1)'''
        result = [-1.0000000000000000e+01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_92(self):
        inp = '''100.'''
        fmt = '''(D4.1)'''
        result = [1.0000000000000000e+02]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_93(self):
        inp = '''-100.'''
        fmt = '''(D4.1)'''
        result = [-1.0000000000000000e+01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_94(self):
        inp = '''1000.'''
        fmt = '''(D4.1)'''
        result = [1.0000000000000000e+02]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_95(self):
        inp = '''-1000.'''
        fmt = '''(D4.1)'''
        result = [-1.0000000000000000e+01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_96(self):
        inp = '''10000.'''
        fmt = '''(D4.1)'''
        result = [1.0000000000000000e+02]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_97(self):
        inp = '''-10000.'''
        fmt = '''(D4.1)'''
        result = [-1.0000000000000000e+01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_98(self):
        inp = '''100000.'''
        fmt = '''(D4.1)'''
        result = [1.0000000000000000e+02]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_99(self):
        inp = '''-100000.'''
        fmt = '''(D4.1)'''
        result = [-1.0000000000000000e+01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_100(self):
        inp = '''123456789.'''
        fmt = '''(D4.1)'''
        result = [1.2340000000000001e+02]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_101(self):
        inp = '''0.1'''
        fmt = '''(D4.1)'''
        result = [1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_102(self):
        inp = '''-0.1'''
        fmt = '''(D4.1)'''
        result = [-1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_103(self):
        inp = '''0.01'''
        fmt = '''(D4.1)'''
        result = [1.0000000000000000e-02]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_104(self):
        inp = '''-0.01'''
        fmt = '''(D4.1)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_105(self):
        inp = '''0.001'''
        fmt = '''(D4.1)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_106(self):
        inp = '''-0.001'''
        fmt = '''(D4.1)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_107(self):
        inp = '''0.0001'''
        fmt = '''(D4.1)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_108(self):
        inp = '''-0.0001'''
        fmt = '''(D4.1)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_109(self):
        inp = '''-1.96e-16'''
        fmt = '''(D4.1)'''
        result = [-1.8999999999999999e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_110(self):
        inp = '''3.14159-    1.0'''
        fmt = '''(D4.1)'''
        result = [3.1400000000000001e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_111(self):
        inp = '''1d12'''
        fmt = '''(D4.1)'''
        result = [1.0000000000000000e+11]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_112(self):
        inp = '''1D12'''
        fmt = '''(D4.1)'''
        result = [1.0000000000000000e+11]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_113(self):
        inp = '''-1   d12'''
        fmt = '''(D4.1)'''
        result = [-1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_114(self):
        inp = '''.'''
        fmt = '''(D4.1)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_115(self):
        inp = '''.1'''
        fmt = '''(D4.1)'''
        result = [1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_116(self):
        inp = '''0.1E+200'''
        fmt = '''(D4.1)'''
        result = [1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_117(self):
        inp = '''3.'''
        fmt = '''(D5.1)'''
        result = [3.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_118(self):
        inp = '''-3.'''
        fmt = '''(D5.1)'''
        result = [-3.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_119(self):
        inp = '''10.'''
        fmt = '''(D5.1)'''
        result = [1.0000000000000000e+01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_120(self):
        inp = '''-10.'''
        fmt = '''(D5.1)'''
        result = [-1.0000000000000000e+01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_121(self):
        inp = '''100.'''
        fmt = '''(D5.1)'''
        result = [1.0000000000000000e+02]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_122(self):
        inp = '''-100.'''
        fmt = '''(D5.1)'''
        result = [-1.0000000000000000e+02]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_123(self):
        inp = '''1000.'''
        fmt = '''(D5.1)'''
        result = [1.0000000000000000e+03]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_124(self):
        inp = '''-1000.'''
        fmt = '''(D5.1)'''
        result = [-1.0000000000000000e+02]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_125(self):
        inp = '''10000.'''
        fmt = '''(D5.1)'''
        result = [1.0000000000000000e+03]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_126(self):
        inp = '''-10000.'''
        fmt = '''(D5.1)'''
        result = [-1.0000000000000000e+02]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_127(self):
        inp = '''100000.'''
        fmt = '''(D5.1)'''
        result = [1.0000000000000000e+03]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_128(self):
        inp = '''-100000.'''
        fmt = '''(D5.1)'''
        result = [-1.0000000000000000e+02]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_129(self):
        inp = '''123456789.'''
        fmt = '''(D5.1)'''
        result = [1.2345000000000000e+03]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_130(self):
        inp = '''0.1'''
        fmt = '''(D5.1)'''
        result = [1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_131(self):
        inp = '''-0.1'''
        fmt = '''(D5.1)'''
        result = [-1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_132(self):
        inp = '''0.01'''
        fmt = '''(D5.1)'''
        result = [1.0000000000000000e-02]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_133(self):
        inp = '''-0.01'''
        fmt = '''(D5.1)'''
        result = [-1.0000000000000000e-02]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_134(self):
        inp = '''0.001'''
        fmt = '''(D5.1)'''
        result = [1.0000000000000000e-03]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_135(self):
        inp = '''-0.001'''
        fmt = '''(D5.1)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_136(self):
        inp = '''0.0001'''
        fmt = '''(D5.1)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_137(self):
        inp = '''-0.0001'''
        fmt = '''(D5.1)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_138(self):
        inp = '''-1.96e-16'''
        fmt = '''(D5.1)'''
        result = [-1.9600000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_139(self):
        inp = '''3.14159-    1.0'''
        fmt = '''(D5.1)'''
        result = [3.1410000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_140(self):
        inp = '''1d12'''
        fmt = '''(D5.1)'''
        result = [1.0000000000000000e+11]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_141(self):
        inp = '''1D12'''
        fmt = '''(D5.1)'''
        result = [1.0000000000000000e+11]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_142(self):
        inp = '''-1   d12'''
        fmt = '''(D5.1)'''
        result = [-1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_143(self):
        inp = '''.'''
        fmt = '''(D5.1)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_144(self):
        inp = '''.1'''
        fmt = '''(D5.1)'''
        result = [1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_145(self):
        inp = '''0.1E+200'''
        fmt = '''(D5.1)'''
        result = [1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_146(self):
        inp = '''3.'''
        fmt = '''(D10.1)'''
        result = [3.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_147(self):
        inp = '''-3.'''
        fmt = '''(D10.1)'''
        result = [-3.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_148(self):
        inp = '''10.'''
        fmt = '''(D10.1)'''
        result = [1.0000000000000000e+01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_149(self):
        inp = '''-10.'''
        fmt = '''(D10.1)'''
        result = [-1.0000000000000000e+01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_150(self):
        inp = '''100.'''
        fmt = '''(D10.1)'''
        result = [1.0000000000000000e+02]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_151(self):
        inp = '''-100.'''
        fmt = '''(D10.1)'''
        result = [-1.0000000000000000e+02]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_152(self):
        inp = '''1000.'''
        fmt = '''(D10.1)'''
        result = [1.0000000000000000e+03]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_153(self):
        inp = '''-1000.'''
        fmt = '''(D10.1)'''
        result = [-1.0000000000000000e+03]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_154(self):
        inp = '''10000.'''
        fmt = '''(D10.1)'''
        result = [1.0000000000000000e+04]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_155(self):
        inp = '''-10000.'''
        fmt = '''(D10.1)'''
        result = [-1.0000000000000000e+04]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_156(self):
        inp = '''100000.'''
        fmt = '''(D10.1)'''
        result = [1.0000000000000000e+05]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_157(self):
        inp = '''-100000.'''
        fmt = '''(D10.1)'''
        result = [-1.0000000000000000e+05]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_158(self):
        inp = '''123456789.'''
        fmt = '''(D10.1)'''
        result = [1.2345678900000000e+08]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_159(self):
        inp = '''0.1'''
        fmt = '''(D10.1)'''
        result = [1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_160(self):
        inp = '''-0.1'''
        fmt = '''(D10.1)'''
        result = [-1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_161(self):
        inp = '''0.01'''
        fmt = '''(D10.1)'''
        result = [1.0000000000000000e-02]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_162(self):
        inp = '''-0.01'''
        fmt = '''(D10.1)'''
        result = [-1.0000000000000000e-02]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_163(self):
        inp = '''0.001'''
        fmt = '''(D10.1)'''
        result = [1.0000000000000000e-03]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_164(self):
        inp = '''-0.001'''
        fmt = '''(D10.1)'''
        result = [-1.0000000000000000e-03]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_165(self):
        inp = '''0.0001'''
        fmt = '''(D10.1)'''
        result = [1.0000000000000000e-04]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_166(self):
        inp = '''-0.0001'''
        fmt = '''(D10.1)'''
        result = [-1.0000000000000000e-04]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_167(self):
        inp = '''-1.96e-16'''
        fmt = '''(D10.1)'''
        result = [-1.9600000000000000e-16]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_168(self):
        inp = '''3.14159-    1.0'''
        fmt = '''(D10.1)'''
        result = [3.1415899999999999e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_169(self):
        inp = '''1d12'''
        fmt = '''(D10.1)'''
        result = [1.0000000000000000e+11]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_170(self):
        inp = '''1D12'''
        fmt = '''(D10.1)'''
        result = [1.0000000000000000e+11]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_171(self):
        inp = '''-1   d12'''
        fmt = '''(D10.1)'''
        result = [-1.0000000000000000e+11]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_172(self):
        inp = '''.'''
        fmt = '''(D10.1)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_173(self):
        inp = '''.1'''
        fmt = '''(D10.1)'''
        result = [1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_174(self):
        inp = '''0.1E+200'''
        fmt = '''(D10.1)'''
        result = [1.0000000000000001e+199]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_175(self):
        inp = '''3.'''
        fmt = '''(D2.2)'''
        result = [3.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_176(self):
        inp = '''-3.'''
        fmt = '''(D2.2)'''
        result = [-2.9999999999999999e-02]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_177(self):
        inp = '''10.'''
        fmt = '''(D2.2)'''
        result = [1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_178(self):
        inp = '''-10.'''
        fmt = '''(D2.2)'''
        result = [-1.0000000000000000e-02]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_179(self):
        inp = '''100.'''
        fmt = '''(D2.2)'''
        result = [1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_180(self):
        inp = '''-100.'''
        fmt = '''(D2.2)'''
        result = [-1.0000000000000000e-02]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_181(self):
        inp = '''1000.'''
        fmt = '''(D2.2)'''
        result = [1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_182(self):
        inp = '''-1000.'''
        fmt = '''(D2.2)'''
        result = [-1.0000000000000000e-02]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_183(self):
        inp = '''10000.'''
        fmt = '''(D2.2)'''
        result = [1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_184(self):
        inp = '''-10000.'''
        fmt = '''(D2.2)'''
        result = [-1.0000000000000000e-02]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_185(self):
        inp = '''100000.'''
        fmt = '''(D2.2)'''
        result = [1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_186(self):
        inp = '''-100000.'''
        fmt = '''(D2.2)'''
        result = [-1.0000000000000000e-02]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_187(self):
        inp = '''123456789.'''
        fmt = '''(D2.2)'''
        result = [1.2000000000000000e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_188(self):
        inp = '''0.1'''
        fmt = '''(D2.2)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_189(self):
        inp = '''-0.1'''
        fmt = '''(D2.2)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_190(self):
        inp = '''0.01'''
        fmt = '''(D2.2)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_191(self):
        inp = '''-0.01'''
        fmt = '''(D2.2)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_192(self):
        inp = '''0.001'''
        fmt = '''(D2.2)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_193(self):
        inp = '''-0.001'''
        fmt = '''(D2.2)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_194(self):
        inp = '''0.0001'''
        fmt = '''(D2.2)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_195(self):
        inp = '''-0.0001'''
        fmt = '''(D2.2)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_196(self):
        inp = '''-1.96e-16'''
        fmt = '''(D2.2)'''
        result = [-1.0000000000000000e-02]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_197(self):
        inp = '''3.14159-    1.0'''
        fmt = '''(D2.2)'''
        result = [3.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_198(self):
        inp = '''1d12'''
        fmt = '''(D2.2)'''
        result = [1.0000000000000000e-02]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_199(self):
        inp = '''1D12'''
        fmt = '''(D2.2)'''
        result = [1.0000000000000000e-02]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_200(self):
        inp = '''-1   d12'''
        fmt = '''(D2.2)'''
        result = [-1.0000000000000000e-02]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_201(self):
        inp = '''.'''
        fmt = '''(D2.2)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_202(self):
        inp = '''.1'''
        fmt = '''(D2.2)'''
        result = [1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_203(self):
        inp = '''0.1E+200'''
        fmt = '''(D2.2)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_204(self):
        inp = '''3.'''
        fmt = '''(D3.2)'''
        result = [3.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_205(self):
        inp = '''-3.'''
        fmt = '''(D3.2)'''
        result = [-3.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_206(self):
        inp = '''10.'''
        fmt = '''(D3.2)'''
        result = [1.0000000000000000e+01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_207(self):
        inp = '''-10.'''
        fmt = '''(D3.2)'''
        result = [-1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_208(self):
        inp = '''100.'''
        fmt = '''(D3.2)'''
        result = [1.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_209(self):
        inp = '''-100.'''
        fmt = '''(D3.2)'''
        result = [-1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_210(self):
        inp = '''1000.'''
        fmt = '''(D3.2)'''
        result = [1.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_211(self):
        inp = '''-1000.'''
        fmt = '''(D3.2)'''
        result = [-1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_212(self):
        inp = '''10000.'''
        fmt = '''(D3.2)'''
        result = [1.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_213(self):
        inp = '''-10000.'''
        fmt = '''(D3.2)'''
        result = [-1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_214(self):
        inp = '''100000.'''
        fmt = '''(D3.2)'''
        result = [1.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_215(self):
        inp = '''-100000.'''
        fmt = '''(D3.2)'''
        result = [-1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_216(self):
        inp = '''123456789.'''
        fmt = '''(D3.2)'''
        result = [1.2300000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_217(self):
        inp = '''0.1'''
        fmt = '''(D3.2)'''
        result = [1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_218(self):
        inp = '''-0.1'''
        fmt = '''(D3.2)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_219(self):
        inp = '''0.01'''
        fmt = '''(D3.2)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_220(self):
        inp = '''-0.01'''
        fmt = '''(D3.2)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_221(self):
        inp = '''0.001'''
        fmt = '''(D3.2)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_222(self):
        inp = '''-0.001'''
        fmt = '''(D3.2)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_223(self):
        inp = '''0.0001'''
        fmt = '''(D3.2)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_224(self):
        inp = '''-0.0001'''
        fmt = '''(D3.2)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_225(self):
        inp = '''-1.96e-16'''
        fmt = '''(D3.2)'''
        result = [-1.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_226(self):
        inp = '''3.14159-    1.0'''
        fmt = '''(D3.2)'''
        result = [3.1000000000000001e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_227(self):
        inp = '''1d12'''
        fmt = '''(D3.2)'''
        result = [1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_228(self):
        inp = '''1D12'''
        fmt = '''(D3.2)'''
        result = [1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_229(self):
        inp = '''-1   d12'''
        fmt = '''(D3.2)'''
        result = [-1.0000000000000000e-02]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_230(self):
        inp = '''.'''
        fmt = '''(D3.2)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_231(self):
        inp = '''.1'''
        fmt = '''(D3.2)'''
        result = [1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_232(self):
        inp = '''0.1E+200'''
        fmt = '''(D3.2)'''
        result = [1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_233(self):
        inp = '''3.'''
        fmt = '''(D4.2)'''
        result = [3.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_234(self):
        inp = '''-3.'''
        fmt = '''(D4.2)'''
        result = [-3.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_235(self):
        inp = '''10.'''
        fmt = '''(D4.2)'''
        result = [1.0000000000000000e+01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_236(self):
        inp = '''-10.'''
        fmt = '''(D4.2)'''
        result = [-1.0000000000000000e+01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_237(self):
        inp = '''100.'''
        fmt = '''(D4.2)'''
        result = [1.0000000000000000e+02]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_238(self):
        inp = '''-100.'''
        fmt = '''(D4.2)'''
        result = [-1.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_239(self):
        inp = '''1000.'''
        fmt = '''(D4.2)'''
        result = [1.0000000000000000e+01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_240(self):
        inp = '''-1000.'''
        fmt = '''(D4.2)'''
        result = [-1.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_241(self):
        inp = '''10000.'''
        fmt = '''(D4.2)'''
        result = [1.0000000000000000e+01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_242(self):
        inp = '''-10000.'''
        fmt = '''(D4.2)'''
        result = [-1.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_243(self):
        inp = '''100000.'''
        fmt = '''(D4.2)'''
        result = [1.0000000000000000e+01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_244(self):
        inp = '''-100000.'''
        fmt = '''(D4.2)'''
        result = [-1.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_245(self):
        inp = '''123456789.'''
        fmt = '''(D4.2)'''
        result = [1.2340000000000000e+01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_246(self):
        inp = '''0.1'''
        fmt = '''(D4.2)'''
        result = [1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_247(self):
        inp = '''-0.1'''
        fmt = '''(D4.2)'''
        result = [-1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_248(self):
        inp = '''0.01'''
        fmt = '''(D4.2)'''
        result = [1.0000000000000000e-02]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_249(self):
        inp = '''-0.01'''
        fmt = '''(D4.2)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_250(self):
        inp = '''0.001'''
        fmt = '''(D4.2)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_251(self):
        inp = '''-0.001'''
        fmt = '''(D4.2)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_252(self):
        inp = '''0.0001'''
        fmt = '''(D4.2)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_253(self):
        inp = '''-0.0001'''
        fmt = '''(D4.2)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_254(self):
        inp = '''-1.96e-16'''
        fmt = '''(D4.2)'''
        result = [-1.8999999999999999e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_255(self):
        inp = '''3.14159-    1.0'''
        fmt = '''(D4.2)'''
        result = [3.1400000000000001e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_256(self):
        inp = '''1d12'''
        fmt = '''(D4.2)'''
        result = [1.0000000000000000e+10]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_257(self):
        inp = '''1D12'''
        fmt = '''(D4.2)'''
        result = [1.0000000000000000e+10]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_258(self):
        inp = '''-1   d12'''
        fmt = '''(D4.2)'''
        result = [-1.0000000000000000e-02]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_259(self):
        inp = '''.'''
        fmt = '''(D4.2)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_260(self):
        inp = '''.1'''
        fmt = '''(D4.2)'''
        result = [1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_261(self):
        inp = '''0.1E+200'''
        fmt = '''(D4.2)'''
        result = [1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_262(self):
        inp = '''3.'''
        fmt = '''(D5.2)'''
        result = [3.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_263(self):
        inp = '''-3.'''
        fmt = '''(D5.2)'''
        result = [-3.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_264(self):
        inp = '''10.'''
        fmt = '''(D5.2)'''
        result = [1.0000000000000000e+01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_265(self):
        inp = '''-10.'''
        fmt = '''(D5.2)'''
        result = [-1.0000000000000000e+01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_266(self):
        inp = '''100.'''
        fmt = '''(D5.2)'''
        result = [1.0000000000000000e+02]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_267(self):
        inp = '''-100.'''
        fmt = '''(D5.2)'''
        result = [-1.0000000000000000e+02]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_268(self):
        inp = '''1000.'''
        fmt = '''(D5.2)'''
        result = [1.0000000000000000e+03]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_269(self):
        inp = '''-1000.'''
        fmt = '''(D5.2)'''
        result = [-1.0000000000000000e+01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_270(self):
        inp = '''10000.'''
        fmt = '''(D5.2)'''
        result = [1.0000000000000000e+02]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_271(self):
        inp = '''-10000.'''
        fmt = '''(D5.2)'''
        result = [-1.0000000000000000e+01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_272(self):
        inp = '''100000.'''
        fmt = '''(D5.2)'''
        result = [1.0000000000000000e+02]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_273(self):
        inp = '''-100000.'''
        fmt = '''(D5.2)'''
        result = [-1.0000000000000000e+01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_274(self):
        inp = '''123456789.'''
        fmt = '''(D5.2)'''
        result = [1.2345000000000000e+02]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_275(self):
        inp = '''0.1'''
        fmt = '''(D5.2)'''
        result = [1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_276(self):
        inp = '''-0.1'''
        fmt = '''(D5.2)'''
        result = [-1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_277(self):
        inp = '''0.01'''
        fmt = '''(D5.2)'''
        result = [1.0000000000000000e-02]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_278(self):
        inp = '''-0.01'''
        fmt = '''(D5.2)'''
        result = [-1.0000000000000000e-02]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_279(self):
        inp = '''0.001'''
        fmt = '''(D5.2)'''
        result = [1.0000000000000000e-03]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_280(self):
        inp = '''-0.001'''
        fmt = '''(D5.2)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_281(self):
        inp = '''0.0001'''
        fmt = '''(D5.2)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_282(self):
        inp = '''-0.0001'''
        fmt = '''(D5.2)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_283(self):
        inp = '''-1.96e-16'''
        fmt = '''(D5.2)'''
        result = [-1.9600000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_284(self):
        inp = '''3.14159-    1.0'''
        fmt = '''(D5.2)'''
        result = [3.1410000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_285(self):
        inp = '''1d12'''
        fmt = '''(D5.2)'''
        result = [1.0000000000000000e+10]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_286(self):
        inp = '''1D12'''
        fmt = '''(D5.2)'''
        result = [1.0000000000000000e+10]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_287(self):
        inp = '''-1   d12'''
        fmt = '''(D5.2)'''
        result = [-1.0000000000000000e-02]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_288(self):
        inp = '''.'''
        fmt = '''(D5.2)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_289(self):
        inp = '''.1'''
        fmt = '''(D5.2)'''
        result = [1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_290(self):
        inp = '''0.1E+200'''
        fmt = '''(D5.2)'''
        result = [1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_291(self):
        inp = '''3.'''
        fmt = '''(D10.2)'''
        result = [3.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_292(self):
        inp = '''-3.'''
        fmt = '''(D10.2)'''
        result = [-3.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_293(self):
        inp = '''10.'''
        fmt = '''(D10.2)'''
        result = [1.0000000000000000e+01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_294(self):
        inp = '''-10.'''
        fmt = '''(D10.2)'''
        result = [-1.0000000000000000e+01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_295(self):
        inp = '''100.'''
        fmt = '''(D10.2)'''
        result = [1.0000000000000000e+02]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_296(self):
        inp = '''-100.'''
        fmt = '''(D10.2)'''
        result = [-1.0000000000000000e+02]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_297(self):
        inp = '''1000.'''
        fmt = '''(D10.2)'''
        result = [1.0000000000000000e+03]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_298(self):
        inp = '''-1000.'''
        fmt = '''(D10.2)'''
        result = [-1.0000000000000000e+03]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_299(self):
        inp = '''10000.'''
        fmt = '''(D10.2)'''
        result = [1.0000000000000000e+04]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_300(self):
        inp = '''-10000.'''
        fmt = '''(D10.2)'''
        result = [-1.0000000000000000e+04]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_301(self):
        inp = '''100000.'''
        fmt = '''(D10.2)'''
        result = [1.0000000000000000e+05]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_302(self):
        inp = '''-100000.'''
        fmt = '''(D10.2)'''
        result = [-1.0000000000000000e+05]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_303(self):
        inp = '''123456789.'''
        fmt = '''(D10.2)'''
        result = [1.2345678900000000e+08]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_304(self):
        inp = '''0.1'''
        fmt = '''(D10.2)'''
        result = [1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_305(self):
        inp = '''-0.1'''
        fmt = '''(D10.2)'''
        result = [-1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_306(self):
        inp = '''0.01'''
        fmt = '''(D10.2)'''
        result = [1.0000000000000000e-02]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_307(self):
        inp = '''-0.01'''
        fmt = '''(D10.2)'''
        result = [-1.0000000000000000e-02]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_308(self):
        inp = '''0.001'''
        fmt = '''(D10.2)'''
        result = [1.0000000000000000e-03]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_309(self):
        inp = '''-0.001'''
        fmt = '''(D10.2)'''
        result = [-1.0000000000000000e-03]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_310(self):
        inp = '''0.0001'''
        fmt = '''(D10.2)'''
        result = [1.0000000000000000e-04]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_311(self):
        inp = '''-0.0001'''
        fmt = '''(D10.2)'''
        result = [-1.0000000000000000e-04]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_312(self):
        inp = '''-1.96e-16'''
        fmt = '''(D10.2)'''
        result = [-1.9600000000000000e-16]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_313(self):
        inp = '''3.14159-    1.0'''
        fmt = '''(D10.2)'''
        result = [3.1415899999999999e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_314(self):
        inp = '''1d12'''
        fmt = '''(D10.2)'''
        result = [1.0000000000000000e+10]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_315(self):
        inp = '''1D12'''
        fmt = '''(D10.2)'''
        result = [1.0000000000000000e+10]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_316(self):
        inp = '''-1   d12'''
        fmt = '''(D10.2)'''
        result = [-1.0000000000000000e+10]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_317(self):
        inp = '''.'''
        fmt = '''(D10.2)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_318(self):
        inp = '''.1'''
        fmt = '''(D10.2)'''
        result = [1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_319(self):
        inp = '''0.1E+200'''
        fmt = '''(D10.2)'''
        result = [1.0000000000000001e+199]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_320(self):
        inp = '''3.'''
        fmt = '''(D3.3)'''
        result = [3.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_321(self):
        inp = '''-3.'''
        fmt = '''(D3.3)'''
        result = [-3.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_322(self):
        inp = '''10.'''
        fmt = '''(D3.3)'''
        result = [1.0000000000000000e+01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_323(self):
        inp = '''-10.'''
        fmt = '''(D3.3)'''
        result = [-1.0000000000000000e-02]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_324(self):
        inp = '''100.'''
        fmt = '''(D3.3)'''
        result = [1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_325(self):
        inp = '''-100.'''
        fmt = '''(D3.3)'''
        result = [-1.0000000000000000e-02]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_326(self):
        inp = '''1000.'''
        fmt = '''(D3.3)'''
        result = [1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_327(self):
        inp = '''-1000.'''
        fmt = '''(D3.3)'''
        result = [-1.0000000000000000e-02]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_328(self):
        inp = '''10000.'''
        fmt = '''(D3.3)'''
        result = [1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_329(self):
        inp = '''-10000.'''
        fmt = '''(D3.3)'''
        result = [-1.0000000000000000e-02]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_330(self):
        inp = '''100000.'''
        fmt = '''(D3.3)'''
        result = [1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_331(self):
        inp = '''-100000.'''
        fmt = '''(D3.3)'''
        result = [-1.0000000000000000e-02]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_332(self):
        inp = '''123456789.'''
        fmt = '''(D3.3)'''
        result = [1.2300000000000000e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_333(self):
        inp = '''0.1'''
        fmt = '''(D3.3)'''
        result = [1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_334(self):
        inp = '''-0.1'''
        fmt = '''(D3.3)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_335(self):
        inp = '''0.01'''
        fmt = '''(D3.3)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_336(self):
        inp = '''-0.01'''
        fmt = '''(D3.3)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_337(self):
        inp = '''0.001'''
        fmt = '''(D3.3)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_338(self):
        inp = '''-0.001'''
        fmt = '''(D3.3)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_339(self):
        inp = '''0.0001'''
        fmt = '''(D3.3)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_340(self):
        inp = '''-0.0001'''
        fmt = '''(D3.3)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_341(self):
        inp = '''-1.96e-16'''
        fmt = '''(D3.3)'''
        result = [-1.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_342(self):
        inp = '''3.14159-    1.0'''
        fmt = '''(D3.3)'''
        result = [3.1000000000000001e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_343(self):
        inp = '''1d12'''
        fmt = '''(D3.3)'''
        result = [1.0000000000000000e-02]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_344(self):
        inp = '''1D12'''
        fmt = '''(D3.3)'''
        result = [1.0000000000000000e-02]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_345(self):
        inp = '''-1   d12'''
        fmt = '''(D3.3)'''
        result = [-1.0000000000000000e-03]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_346(self):
        inp = '''.'''
        fmt = '''(D3.3)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_347(self):
        inp = '''.1'''
        fmt = '''(D3.3)'''
        result = [1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_348(self):
        inp = '''0.1E+200'''
        fmt = '''(D3.3)'''
        result = [1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_349(self):
        inp = '''3.'''
        fmt = '''(D4.3)'''
        result = [3.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_350(self):
        inp = '''-3.'''
        fmt = '''(D4.3)'''
        result = [-3.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_351(self):
        inp = '''10.'''
        fmt = '''(D4.3)'''
        result = [1.0000000000000000e+01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_352(self):
        inp = '''-10.'''
        fmt = '''(D4.3)'''
        result = [-1.0000000000000000e+01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_353(self):
        inp = '''100.'''
        fmt = '''(D4.3)'''
        result = [1.0000000000000000e+02]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_354(self):
        inp = '''-100.'''
        fmt = '''(D4.3)'''
        result = [-1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_355(self):
        inp = '''1000.'''
        fmt = '''(D4.3)'''
        result = [1.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_356(self):
        inp = '''-1000.'''
        fmt = '''(D4.3)'''
        result = [-1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_357(self):
        inp = '''10000.'''
        fmt = '''(D4.3)'''
        result = [1.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_358(self):
        inp = '''-10000.'''
        fmt = '''(D4.3)'''
        result = [-1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_359(self):
        inp = '''100000.'''
        fmt = '''(D4.3)'''
        result = [1.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_360(self):
        inp = '''-100000.'''
        fmt = '''(D4.3)'''
        result = [-1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_361(self):
        inp = '''123456789.'''
        fmt = '''(D4.3)'''
        result = [1.2340000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_362(self):
        inp = '''0.1'''
        fmt = '''(D4.3)'''
        result = [1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_363(self):
        inp = '''-0.1'''
        fmt = '''(D4.3)'''
        result = [-1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_364(self):
        inp = '''0.01'''
        fmt = '''(D4.3)'''
        result = [1.0000000000000000e-02]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_365(self):
        inp = '''-0.01'''
        fmt = '''(D4.3)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_366(self):
        inp = '''0.001'''
        fmt = '''(D4.3)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_367(self):
        inp = '''-0.001'''
        fmt = '''(D4.3)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_368(self):
        inp = '''0.0001'''
        fmt = '''(D4.3)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_369(self):
        inp = '''-0.0001'''
        fmt = '''(D4.3)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_370(self):
        inp = '''-1.96e-16'''
        fmt = '''(D4.3)'''
        result = [-1.8999999999999999e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_371(self):
        inp = '''3.14159-    1.0'''
        fmt = '''(D4.3)'''
        result = [3.1400000000000001e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_372(self):
        inp = '''1d12'''
        fmt = '''(D4.3)'''
        result = [1.0000000000000000e+09]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_373(self):
        inp = '''1D12'''
        fmt = '''(D4.3)'''
        result = [1.0000000000000000e+09]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_374(self):
        inp = '''-1   d12'''
        fmt = '''(D4.3)'''
        result = [-1.0000000000000000e-03]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_375(self):
        inp = '''.'''
        fmt = '''(D4.3)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_376(self):
        inp = '''.1'''
        fmt = '''(D4.3)'''
        result = [1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_377(self):
        inp = '''0.1E+200'''
        fmt = '''(D4.3)'''
        result = [1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_378(self):
        inp = '''3.'''
        fmt = '''(D5.3)'''
        result = [3.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_379(self):
        inp = '''-3.'''
        fmt = '''(D5.3)'''
        result = [-3.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_380(self):
        inp = '''10.'''
        fmt = '''(D5.3)'''
        result = [1.0000000000000000e+01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_381(self):
        inp = '''-10.'''
        fmt = '''(D5.3)'''
        result = [-1.0000000000000000e+01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_382(self):
        inp = '''100.'''
        fmt = '''(D5.3)'''
        result = [1.0000000000000000e+02]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_383(self):
        inp = '''-100.'''
        fmt = '''(D5.3)'''
        result = [-1.0000000000000000e+02]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_384(self):
        inp = '''1000.'''
        fmt = '''(D5.3)'''
        result = [1.0000000000000000e+03]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_385(self):
        inp = '''-1000.'''
        fmt = '''(D5.3)'''
        result = [-1.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_386(self):
        inp = '''10000.'''
        fmt = '''(D5.3)'''
        result = [1.0000000000000000e+01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_387(self):
        inp = '''-10000.'''
        fmt = '''(D5.3)'''
        result = [-1.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_388(self):
        inp = '''100000.'''
        fmt = '''(D5.3)'''
        result = [1.0000000000000000e+01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_389(self):
        inp = '''-100000.'''
        fmt = '''(D5.3)'''
        result = [-1.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_390(self):
        inp = '''123456789.'''
        fmt = '''(D5.3)'''
        result = [1.2345000000000001e+01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_391(self):
        inp = '''0.1'''
        fmt = '''(D5.3)'''
        result = [1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_392(self):
        inp = '''-0.1'''
        fmt = '''(D5.3)'''
        result = [-1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_393(self):
        inp = '''0.01'''
        fmt = '''(D5.3)'''
        result = [1.0000000000000000e-02]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_394(self):
        inp = '''-0.01'''
        fmt = '''(D5.3)'''
        result = [-1.0000000000000000e-02]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_395(self):
        inp = '''0.001'''
        fmt = '''(D5.3)'''
        result = [1.0000000000000000e-03]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_396(self):
        inp = '''-0.001'''
        fmt = '''(D5.3)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_397(self):
        inp = '''0.0001'''
        fmt = '''(D5.3)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_398(self):
        inp = '''-0.0001'''
        fmt = '''(D5.3)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_399(self):
        inp = '''-1.96e-16'''
        fmt = '''(D5.3)'''
        result = [-1.9600000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_400(self):
        inp = '''3.14159-    1.0'''
        fmt = '''(D5.3)'''
        result = [3.1410000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_401(self):
        inp = '''1d12'''
        fmt = '''(D5.3)'''
        result = [1.0000000000000000e+09]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_402(self):
        inp = '''1D12'''
        fmt = '''(D5.3)'''
        result = [1.0000000000000000e+09]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_403(self):
        inp = '''-1   d12'''
        fmt = '''(D5.3)'''
        result = [-1.0000000000000000e-03]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_404(self):
        inp = '''.'''
        fmt = '''(D5.3)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_405(self):
        inp = '''.1'''
        fmt = '''(D5.3)'''
        result = [1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_406(self):
        inp = '''0.1E+200'''
        fmt = '''(D5.3)'''
        result = [1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_407(self):
        inp = '''3.'''
        fmt = '''(D10.3)'''
        result = [3.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_408(self):
        inp = '''-3.'''
        fmt = '''(D10.3)'''
        result = [-3.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_409(self):
        inp = '''10.'''
        fmt = '''(D10.3)'''
        result = [1.0000000000000000e+01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_410(self):
        inp = '''-10.'''
        fmt = '''(D10.3)'''
        result = [-1.0000000000000000e+01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_411(self):
        inp = '''100.'''
        fmt = '''(D10.3)'''
        result = [1.0000000000000000e+02]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_412(self):
        inp = '''-100.'''
        fmt = '''(D10.3)'''
        result = [-1.0000000000000000e+02]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_413(self):
        inp = '''1000.'''
        fmt = '''(D10.3)'''
        result = [1.0000000000000000e+03]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_414(self):
        inp = '''-1000.'''
        fmt = '''(D10.3)'''
        result = [-1.0000000000000000e+03]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_415(self):
        inp = '''10000.'''
        fmt = '''(D10.3)'''
        result = [1.0000000000000000e+04]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_416(self):
        inp = '''-10000.'''
        fmt = '''(D10.3)'''
        result = [-1.0000000000000000e+04]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_417(self):
        inp = '''100000.'''
        fmt = '''(D10.3)'''
        result = [1.0000000000000000e+05]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_418(self):
        inp = '''-100000.'''
        fmt = '''(D10.3)'''
        result = [-1.0000000000000000e+05]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_419(self):
        inp = '''123456789.'''
        fmt = '''(D10.3)'''
        result = [1.2345678900000000e+08]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_420(self):
        inp = '''0.1'''
        fmt = '''(D10.3)'''
        result = [1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_421(self):
        inp = '''-0.1'''
        fmt = '''(D10.3)'''
        result = [-1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_422(self):
        inp = '''0.01'''
        fmt = '''(D10.3)'''
        result = [1.0000000000000000e-02]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_423(self):
        inp = '''-0.01'''
        fmt = '''(D10.3)'''
        result = [-1.0000000000000000e-02]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_424(self):
        inp = '''0.001'''
        fmt = '''(D10.3)'''
        result = [1.0000000000000000e-03]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_425(self):
        inp = '''-0.001'''
        fmt = '''(D10.3)'''
        result = [-1.0000000000000000e-03]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_426(self):
        inp = '''0.0001'''
        fmt = '''(D10.3)'''
        result = [1.0000000000000000e-04]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_427(self):
        inp = '''-0.0001'''
        fmt = '''(D10.3)'''
        result = [-1.0000000000000000e-04]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_428(self):
        inp = '''-1.96e-16'''
        fmt = '''(D10.3)'''
        result = [-1.9600000000000000e-16]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_429(self):
        inp = '''3.14159-    1.0'''
        fmt = '''(D10.3)'''
        result = [3.1415899999999999e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_430(self):
        inp = '''1d12'''
        fmt = '''(D10.3)'''
        result = [1.0000000000000000e+09]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_431(self):
        inp = '''1D12'''
        fmt = '''(D10.3)'''
        result = [1.0000000000000000e+09]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_432(self):
        inp = '''-1   d12'''
        fmt = '''(D10.3)'''
        result = [-1.0000000000000000e+09]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_433(self):
        inp = '''.'''
        fmt = '''(D10.3)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_434(self):
        inp = '''.1'''
        fmt = '''(D10.3)'''
        result = [1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_435(self):
        inp = '''0.1E+200'''
        fmt = '''(D10.3)'''
        result = [1.0000000000000001e+199]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_436(self):
        inp = '''3.'''
        fmt = '''(D4.4)'''
        result = [3.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_437(self):
        inp = '''-3.'''
        fmt = '''(D4.4)'''
        result = [-3.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_438(self):
        inp = '''10.'''
        fmt = '''(D4.4)'''
        result = [1.0000000000000000e+01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_439(self):
        inp = '''-10.'''
        fmt = '''(D4.4)'''
        result = [-1.0000000000000000e+01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_440(self):
        inp = '''100.'''
        fmt = '''(D4.4)'''
        result = [1.0000000000000000e+02]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_441(self):
        inp = '''-100.'''
        fmt = '''(D4.4)'''
        result = [-1.0000000000000000e-02]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_442(self):
        inp = '''1000.'''
        fmt = '''(D4.4)'''
        result = [1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_443(self):
        inp = '''-1000.'''
        fmt = '''(D4.4)'''
        result = [-1.0000000000000000e-02]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_444(self):
        inp = '''10000.'''
        fmt = '''(D4.4)'''
        result = [1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_445(self):
        inp = '''-10000.'''
        fmt = '''(D4.4)'''
        result = [-1.0000000000000000e-02]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_446(self):
        inp = '''100000.'''
        fmt = '''(D4.4)'''
        result = [1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_447(self):
        inp = '''-100000.'''
        fmt = '''(D4.4)'''
        result = [-1.0000000000000000e-02]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_448(self):
        inp = '''123456789.'''
        fmt = '''(D4.4)'''
        result = [1.2340000000000000e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_449(self):
        inp = '''0.1'''
        fmt = '''(D4.4)'''
        result = [1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_450(self):
        inp = '''-0.1'''
        fmt = '''(D4.4)'''
        result = [-1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_451(self):
        inp = '''0.01'''
        fmt = '''(D4.4)'''
        result = [1.0000000000000000e-02]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_452(self):
        inp = '''-0.01'''
        fmt = '''(D4.4)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_453(self):
        inp = '''0.001'''
        fmt = '''(D4.4)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_454(self):
        inp = '''-0.001'''
        fmt = '''(D4.4)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_455(self):
        inp = '''0.0001'''
        fmt = '''(D4.4)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_456(self):
        inp = '''-0.0001'''
        fmt = '''(D4.4)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_457(self):
        inp = '''-1.96e-16'''
        fmt = '''(D4.4)'''
        result = [-1.8999999999999999e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_458(self):
        inp = '''3.14159-    1.0'''
        fmt = '''(D4.4)'''
        result = [3.1400000000000001e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_459(self):
        inp = '''1d12'''
        fmt = '''(D4.4)'''
        result = [1.0000000000000000e+08]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_460(self):
        inp = '''1D12'''
        fmt = '''(D4.4)'''
        result = [1.0000000000000000e+08]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_461(self):
        inp = '''-1   d12'''
        fmt = '''(D4.4)'''
        result = [-1.0000000000000000e-04]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_462(self):
        inp = '''.'''
        fmt = '''(D4.4)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_463(self):
        inp = '''.1'''
        fmt = '''(D4.4)'''
        result = [1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_464(self):
        inp = '''0.1E+200'''
        fmt = '''(D4.4)'''
        result = [1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_465(self):
        inp = '''3.'''
        fmt = '''(D5.4)'''
        result = [3.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_466(self):
        inp = '''-3.'''
        fmt = '''(D5.4)'''
        result = [-3.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_467(self):
        inp = '''10.'''
        fmt = '''(D5.4)'''
        result = [1.0000000000000000e+01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_468(self):
        inp = '''-10.'''
        fmt = '''(D5.4)'''
        result = [-1.0000000000000000e+01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_469(self):
        inp = '''100.'''
        fmt = '''(D5.4)'''
        result = [1.0000000000000000e+02]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_470(self):
        inp = '''-100.'''
        fmt = '''(D5.4)'''
        result = [-1.0000000000000000e+02]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_471(self):
        inp = '''1000.'''
        fmt = '''(D5.4)'''
        result = [1.0000000000000000e+03]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_472(self):
        inp = '''-1000.'''
        fmt = '''(D5.4)'''
        result = [-1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_473(self):
        inp = '''10000.'''
        fmt = '''(D5.4)'''
        result = [1.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_474(self):
        inp = '''-10000.'''
        fmt = '''(D5.4)'''
        result = [-1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_475(self):
        inp = '''100000.'''
        fmt = '''(D5.4)'''
        result = [1.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_476(self):
        inp = '''-100000.'''
        fmt = '''(D5.4)'''
        result = [-1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_477(self):
        inp = '''123456789.'''
        fmt = '''(D5.4)'''
        result = [1.2344999999999999e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_478(self):
        inp = '''0.1'''
        fmt = '''(D5.4)'''
        result = [1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_479(self):
        inp = '''-0.1'''
        fmt = '''(D5.4)'''
        result = [-1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_480(self):
        inp = '''0.01'''
        fmt = '''(D5.4)'''
        result = [1.0000000000000000e-02]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_481(self):
        inp = '''-0.01'''
        fmt = '''(D5.4)'''
        result = [-1.0000000000000000e-02]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_482(self):
        inp = '''0.001'''
        fmt = '''(D5.4)'''
        result = [1.0000000000000000e-03]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_483(self):
        inp = '''-0.001'''
        fmt = '''(D5.4)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_484(self):
        inp = '''0.0001'''
        fmt = '''(D5.4)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_485(self):
        inp = '''-0.0001'''
        fmt = '''(D5.4)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_486(self):
        inp = '''-1.96e-16'''
        fmt = '''(D5.4)'''
        result = [-1.9600000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_487(self):
        inp = '''3.14159-    1.0'''
        fmt = '''(D5.4)'''
        result = [3.1410000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_488(self):
        inp = '''1d12'''
        fmt = '''(D5.4)'''
        result = [1.0000000000000000e+08]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_489(self):
        inp = '''1D12'''
        fmt = '''(D5.4)'''
        result = [1.0000000000000000e+08]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_490(self):
        inp = '''-1   d12'''
        fmt = '''(D5.4)'''
        result = [-1.0000000000000000e-04]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_491(self):
        inp = '''.'''
        fmt = '''(D5.4)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_492(self):
        inp = '''.1'''
        fmt = '''(D5.4)'''
        result = [1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_493(self):
        inp = '''0.1E+200'''
        fmt = '''(D5.4)'''
        result = [1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_494(self):
        inp = '''3.'''
        fmt = '''(D10.4)'''
        result = [3.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_495(self):
        inp = '''-3.'''
        fmt = '''(D10.4)'''
        result = [-3.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_496(self):
        inp = '''10.'''
        fmt = '''(D10.4)'''
        result = [1.0000000000000000e+01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_497(self):
        inp = '''-10.'''
        fmt = '''(D10.4)'''
        result = [-1.0000000000000000e+01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_498(self):
        inp = '''100.'''
        fmt = '''(D10.4)'''
        result = [1.0000000000000000e+02]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_499(self):
        inp = '''-100.'''
        fmt = '''(D10.4)'''
        result = [-1.0000000000000000e+02]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_500(self):
        inp = '''1000.'''
        fmt = '''(D10.4)'''
        result = [1.0000000000000000e+03]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_501(self):
        inp = '''-1000.'''
        fmt = '''(D10.4)'''
        result = [-1.0000000000000000e+03]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_502(self):
        inp = '''10000.'''
        fmt = '''(D10.4)'''
        result = [1.0000000000000000e+04]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_503(self):
        inp = '''-10000.'''
        fmt = '''(D10.4)'''
        result = [-1.0000000000000000e+04]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_504(self):
        inp = '''100000.'''
        fmt = '''(D10.4)'''
        result = [1.0000000000000000e+05]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_505(self):
        inp = '''-100000.'''
        fmt = '''(D10.4)'''
        result = [-1.0000000000000000e+05]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_506(self):
        inp = '''123456789.'''
        fmt = '''(D10.4)'''
        result = [1.2345678900000000e+08]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_507(self):
        inp = '''0.1'''
        fmt = '''(D10.4)'''
        result = [1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_508(self):
        inp = '''-0.1'''
        fmt = '''(D10.4)'''
        result = [-1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_509(self):
        inp = '''0.01'''
        fmt = '''(D10.4)'''
        result = [1.0000000000000000e-02]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_510(self):
        inp = '''-0.01'''
        fmt = '''(D10.4)'''
        result = [-1.0000000000000000e-02]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_511(self):
        inp = '''0.001'''
        fmt = '''(D10.4)'''
        result = [1.0000000000000000e-03]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_512(self):
        inp = '''-0.001'''
        fmt = '''(D10.4)'''
        result = [-1.0000000000000000e-03]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_513(self):
        inp = '''0.0001'''
        fmt = '''(D10.4)'''
        result = [1.0000000000000000e-04]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_514(self):
        inp = '''-0.0001'''
        fmt = '''(D10.4)'''
        result = [-1.0000000000000000e-04]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_515(self):
        inp = '''-1.96e-16'''
        fmt = '''(D10.4)'''
        result = [-1.9600000000000000e-16]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_516(self):
        inp = '''3.14159-    1.0'''
        fmt = '''(D10.4)'''
        result = [3.1415899999999999e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_517(self):
        inp = '''1d12'''
        fmt = '''(D10.4)'''
        result = [1.0000000000000000e+08]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_518(self):
        inp = '''1D12'''
        fmt = '''(D10.4)'''
        result = [1.0000000000000000e+08]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_519(self):
        inp = '''-1   d12'''
        fmt = '''(D10.4)'''
        result = [-1.0000000000000000e+08]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_520(self):
        inp = '''.'''
        fmt = '''(D10.4)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_521(self):
        inp = '''.1'''
        fmt = '''(D10.4)'''
        result = [1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_522(self):
        inp = '''0.1E+200'''
        fmt = '''(D10.4)'''
        result = [1.0000000000000001e+199]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_523(self):
        inp = '''3.'''
        fmt = '''(D5.5)'''
        result = [3.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_524(self):
        inp = '''-3.'''
        fmt = '''(D5.5)'''
        result = [-3.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_525(self):
        inp = '''10.'''
        fmt = '''(D5.5)'''
        result = [1.0000000000000000e+01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_526(self):
        inp = '''-10.'''
        fmt = '''(D5.5)'''
        result = [-1.0000000000000000e+01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_527(self):
        inp = '''100.'''
        fmt = '''(D5.5)'''
        result = [1.0000000000000000e+02]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_528(self):
        inp = '''-100.'''
        fmt = '''(D5.5)'''
        result = [-1.0000000000000000e+02]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_529(self):
        inp = '''1000.'''
        fmt = '''(D5.5)'''
        result = [1.0000000000000000e+03]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_530(self):
        inp = '''-1000.'''
        fmt = '''(D5.5)'''
        result = [-1.0000000000000000e-02]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_531(self):
        inp = '''10000.'''
        fmt = '''(D5.5)'''
        result = [1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_532(self):
        inp = '''-10000.'''
        fmt = '''(D5.5)'''
        result = [-1.0000000000000000e-02]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_533(self):
        inp = '''100000.'''
        fmt = '''(D5.5)'''
        result = [1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_534(self):
        inp = '''-100000.'''
        fmt = '''(D5.5)'''
        result = [-1.0000000000000000e-02]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_535(self):
        inp = '''123456789.'''
        fmt = '''(D5.5)'''
        result = [1.2345000000000000e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_536(self):
        inp = '''0.1'''
        fmt = '''(D5.5)'''
        result = [1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_537(self):
        inp = '''-0.1'''
        fmt = '''(D5.5)'''
        result = [-1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_538(self):
        inp = '''0.01'''
        fmt = '''(D5.5)'''
        result = [1.0000000000000000e-02]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_539(self):
        inp = '''-0.01'''
        fmt = '''(D5.5)'''
        result = [-1.0000000000000000e-02]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_540(self):
        inp = '''0.001'''
        fmt = '''(D5.5)'''
        result = [1.0000000000000000e-03]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_541(self):
        inp = '''-0.001'''
        fmt = '''(D5.5)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_542(self):
        inp = '''0.0001'''
        fmt = '''(D5.5)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_543(self):
        inp = '''-0.0001'''
        fmt = '''(D5.5)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_544(self):
        inp = '''-1.96e-16'''
        fmt = '''(D5.5)'''
        result = [-1.9600000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_545(self):
        inp = '''3.14159-    1.0'''
        fmt = '''(D5.5)'''
        result = [3.1410000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_546(self):
        inp = '''1d12'''
        fmt = '''(D5.5)'''
        result = [1.0000000000000000e+07]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_547(self):
        inp = '''1D12'''
        fmt = '''(D5.5)'''
        result = [1.0000000000000000e+07]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_548(self):
        inp = '''-1   d12'''
        fmt = '''(D5.5)'''
        result = [-1.0000000000000001e-05]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_549(self):
        inp = '''.'''
        fmt = '''(D5.5)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_550(self):
        inp = '''.1'''
        fmt = '''(D5.5)'''
        result = [1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_551(self):
        inp = '''0.1E+200'''
        fmt = '''(D5.5)'''
        result = [1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_552(self):
        inp = '''3.'''
        fmt = '''(D10.5)'''
        result = [3.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_553(self):
        inp = '''-3.'''
        fmt = '''(D10.5)'''
        result = [-3.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_554(self):
        inp = '''10.'''
        fmt = '''(D10.5)'''
        result = [1.0000000000000000e+01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_555(self):
        inp = '''-10.'''
        fmt = '''(D10.5)'''
        result = [-1.0000000000000000e+01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_556(self):
        inp = '''100.'''
        fmt = '''(D10.5)'''
        result = [1.0000000000000000e+02]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_557(self):
        inp = '''-100.'''
        fmt = '''(D10.5)'''
        result = [-1.0000000000000000e+02]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_558(self):
        inp = '''1000.'''
        fmt = '''(D10.5)'''
        result = [1.0000000000000000e+03]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_559(self):
        inp = '''-1000.'''
        fmt = '''(D10.5)'''
        result = [-1.0000000000000000e+03]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_560(self):
        inp = '''10000.'''
        fmt = '''(D10.5)'''
        result = [1.0000000000000000e+04]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_561(self):
        inp = '''-10000.'''
        fmt = '''(D10.5)'''
        result = [-1.0000000000000000e+04]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_562(self):
        inp = '''100000.'''
        fmt = '''(D10.5)'''
        result = [1.0000000000000000e+05]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_563(self):
        inp = '''-100000.'''
        fmt = '''(D10.5)'''
        result = [-1.0000000000000000e+05]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_564(self):
        inp = '''123456789.'''
        fmt = '''(D10.5)'''
        result = [1.2345678900000000e+08]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_565(self):
        inp = '''0.1'''
        fmt = '''(D10.5)'''
        result = [1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_566(self):
        inp = '''-0.1'''
        fmt = '''(D10.5)'''
        result = [-1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_567(self):
        inp = '''0.01'''
        fmt = '''(D10.5)'''
        result = [1.0000000000000000e-02]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_568(self):
        inp = '''-0.01'''
        fmt = '''(D10.5)'''
        result = [-1.0000000000000000e-02]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_569(self):
        inp = '''0.001'''
        fmt = '''(D10.5)'''
        result = [1.0000000000000000e-03]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_570(self):
        inp = '''-0.001'''
        fmt = '''(D10.5)'''
        result = [-1.0000000000000000e-03]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_571(self):
        inp = '''0.0001'''
        fmt = '''(D10.5)'''
        result = [1.0000000000000000e-04]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_572(self):
        inp = '''-0.0001'''
        fmt = '''(D10.5)'''
        result = [-1.0000000000000000e-04]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_573(self):
        inp = '''-1.96e-16'''
        fmt = '''(D10.5)'''
        result = [-1.9600000000000000e-16]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_574(self):
        inp = '''3.14159-    1.0'''
        fmt = '''(D10.5)'''
        result = [3.1415899999999999e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_575(self):
        inp = '''1d12'''
        fmt = '''(D10.5)'''
        result = [1.0000000000000000e+07]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_576(self):
        inp = '''1D12'''
        fmt = '''(D10.5)'''
        result = [1.0000000000000000e+07]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_577(self):
        inp = '''-1   d12'''
        fmt = '''(D10.5)'''
        result = [-1.0000000000000000e+07]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_578(self):
        inp = '''.'''
        fmt = '''(D10.5)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_579(self):
        inp = '''.1'''
        fmt = '''(D10.5)'''
        result = [1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_580(self):
        inp = '''0.1E+200'''
        fmt = '''(D10.5)'''
        result = [1.0000000000000001e+199]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_581(self):
        inp = '''3.'''
        fmt = '''(D10.10)'''
        result = [3.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_582(self):
        inp = '''-3.'''
        fmt = '''(D10.10)'''
        result = [-3.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_583(self):
        inp = '''10.'''
        fmt = '''(D10.10)'''
        result = [1.0000000000000000e+01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_584(self):
        inp = '''-10.'''
        fmt = '''(D10.10)'''
        result = [-1.0000000000000000e+01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_585(self):
        inp = '''100.'''
        fmt = '''(D10.10)'''
        result = [1.0000000000000000e+02]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_586(self):
        inp = '''-100.'''
        fmt = '''(D10.10)'''
        result = [-1.0000000000000000e+02]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_587(self):
        inp = '''1000.'''
        fmt = '''(D10.10)'''
        result = [1.0000000000000000e+03]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_588(self):
        inp = '''-1000.'''
        fmt = '''(D10.10)'''
        result = [-1.0000000000000000e+03]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_589(self):
        inp = '''10000.'''
        fmt = '''(D10.10)'''
        result = [1.0000000000000000e+04]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_590(self):
        inp = '''-10000.'''
        fmt = '''(D10.10)'''
        result = [-1.0000000000000000e+04]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_591(self):
        inp = '''100000.'''
        fmt = '''(D10.10)'''
        result = [1.0000000000000000e+05]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_592(self):
        inp = '''-100000.'''
        fmt = '''(D10.10)'''
        result = [-1.0000000000000000e+05]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_593(self):
        inp = '''123456789.'''
        fmt = '''(D10.10)'''
        result = [1.2345678900000000e+08]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_594(self):
        inp = '''0.1'''
        fmt = '''(D10.10)'''
        result = [1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_595(self):
        inp = '''-0.1'''
        fmt = '''(D10.10)'''
        result = [-1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_596(self):
        inp = '''0.01'''
        fmt = '''(D10.10)'''
        result = [1.0000000000000000e-02]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_597(self):
        inp = '''-0.01'''
        fmt = '''(D10.10)'''
        result = [-1.0000000000000000e-02]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_598(self):
        inp = '''0.001'''
        fmt = '''(D10.10)'''
        result = [1.0000000000000000e-03]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_599(self):
        inp = '''-0.001'''
        fmt = '''(D10.10)'''
        result = [-1.0000000000000000e-03]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_600(self):
        inp = '''0.0001'''
        fmt = '''(D10.10)'''
        result = [1.0000000000000000e-04]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_601(self):
        inp = '''-0.0001'''
        fmt = '''(D10.10)'''
        result = [-1.0000000000000000e-04]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_602(self):
        inp = '''-1.96e-16'''
        fmt = '''(D10.10)'''
        result = [-1.9600000000000000e-16]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_603(self):
        inp = '''3.14159-    1.0'''
        fmt = '''(D10.10)'''
        result = [3.1415899999999999e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_604(self):
        inp = '''1d12'''
        fmt = '''(D10.10)'''
        result = [1.0000000000000000e+02]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_605(self):
        inp = '''1D12'''
        fmt = '''(D10.10)'''
        result = [1.0000000000000000e+02]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_606(self):
        inp = '''-1   d12'''
        fmt = '''(D10.10)'''
        result = [-1.0000000000000000e+02]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_607(self):
        inp = '''.'''
        fmt = '''(D10.10)'''
        result = [0.0000000000000000e+00]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='D')
    def test_d_ed_input_608(self):
        inp = '''.1'''
        fmt = '''(D10.10)'''
        result = [1.0000000000000001e-01]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))


if __name__ == '__main__':
    unittest.main()