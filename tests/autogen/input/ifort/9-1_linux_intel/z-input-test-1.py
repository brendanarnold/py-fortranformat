
import sys
import os
import unittest
from nose.plugins.attrib import attr

# To change this, re-run 'build-unittests.py'

from fortranformat._input import input as _input
from fortranformat._lexer import lexer as _lexer
from fortranformat._parser import parser as _parser
import unittest

class ZEditDescriptorBatch1TestCase(unittest.TestCase):

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_1(self):
        inp = '''0'''
        fmt = '''(Z1)'''
        result = [0]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_2(self):
        inp = '''-0'''
        fmt = '''(Z1)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_3(self):
        inp = '''1'''
        fmt = '''(Z1)'''
        result = [1]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_4(self):
        inp = '''-1'''
        fmt = '''(Z1)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_5(self):
        inp = '''3'''
        fmt = '''(Z1)'''
        result = [3]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_6(self):
        inp = '''-3'''
        fmt = '''(Z1)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_7(self):
        inp = '''10'''
        fmt = '''(Z1)'''
        result = [1]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_8(self):
        inp = '''-10'''
        fmt = '''(Z1)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_9(self):
        inp = '''100'''
        fmt = '''(Z1)'''
        result = [1]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_10(self):
        inp = '''-100'''
        fmt = '''(Z1)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_11(self):
        inp = '''1000'''
        fmt = '''(Z1)'''
        result = [1]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_12(self):
        inp = '''-1000'''
        fmt = '''(Z1)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_13(self):
        inp = '''10000'''
        fmt = '''(Z1)'''
        result = [1]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_14(self):
        inp = '''-10000'''
        fmt = '''(Z1)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_15(self):
        inp = '''100000'''
        fmt = '''(Z1)'''
        result = [1]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_16(self):
        inp = '''-100000'''
        fmt = '''(Z1)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_17(self):
        inp = '''123456789'''
        fmt = '''(Z1)'''
        result = [1]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_18(self):
        inp = '''ff'''
        fmt = '''(Z1)'''
        result = [15]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_19(self):
        inp = '''F'''
        fmt = '''(Z1)'''
        result = [15]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_20(self):
        inp = ''' F F F'''
        fmt = '''(Z1)'''
        result = [0]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_21(self):
        inp = '''A a 2B'''
        fmt = '''(Z1)'''
        result = [10]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_22(self):
        inp = '''A.'''
        fmt = '''(Z1)'''
        result = [10]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_23(self):
        inp = '''0'''
        fmt = '''(Z2)'''
        result = [0]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_24(self):
        inp = '''-0'''
        fmt = '''(Z2)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_25(self):
        inp = '''1'''
        fmt = '''(Z2)'''
        result = [1]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_26(self):
        inp = '''-1'''
        fmt = '''(Z2)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_27(self):
        inp = '''3'''
        fmt = '''(Z2)'''
        result = [3]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_28(self):
        inp = '''-3'''
        fmt = '''(Z2)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_29(self):
        inp = '''10'''
        fmt = '''(Z2)'''
        result = [16]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_30(self):
        inp = '''-10'''
        fmt = '''(Z2)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_31(self):
        inp = '''100'''
        fmt = '''(Z2)'''
        result = [16]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_32(self):
        inp = '''-100'''
        fmt = '''(Z2)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_33(self):
        inp = '''1000'''
        fmt = '''(Z2)'''
        result = [16]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_34(self):
        inp = '''-1000'''
        fmt = '''(Z2)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_35(self):
        inp = '''10000'''
        fmt = '''(Z2)'''
        result = [16]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_36(self):
        inp = '''-10000'''
        fmt = '''(Z2)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_37(self):
        inp = '''100000'''
        fmt = '''(Z2)'''
        result = [16]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_38(self):
        inp = '''-100000'''
        fmt = '''(Z2)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_39(self):
        inp = '''123456789'''
        fmt = '''(Z2)'''
        result = [18]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_40(self):
        inp = '''ff'''
        fmt = '''(Z2)'''
        result = [255]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_41(self):
        inp = '''F'''
        fmt = '''(Z2)'''
        result = [15]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_42(self):
        inp = ''' F F F'''
        fmt = '''(Z2)'''
        result = [15]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_43(self):
        inp = '''A a 2B'''
        fmt = '''(Z2)'''
        result = [10]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_44(self):
        inp = '''A.'''
        fmt = '''(Z2)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_45(self):
        inp = '''0'''
        fmt = '''(Z3)'''
        result = [0]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_46(self):
        inp = '''-0'''
        fmt = '''(Z3)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_47(self):
        inp = '''1'''
        fmt = '''(Z3)'''
        result = [1]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_48(self):
        inp = '''-1'''
        fmt = '''(Z3)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_49(self):
        inp = '''3'''
        fmt = '''(Z3)'''
        result = [3]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_50(self):
        inp = '''-3'''
        fmt = '''(Z3)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_51(self):
        inp = '''10'''
        fmt = '''(Z3)'''
        result = [16]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_52(self):
        inp = '''-10'''
        fmt = '''(Z3)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_53(self):
        inp = '''100'''
        fmt = '''(Z3)'''
        result = [256]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_54(self):
        inp = '''-100'''
        fmt = '''(Z3)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_55(self):
        inp = '''1000'''
        fmt = '''(Z3)'''
        result = [256]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_56(self):
        inp = '''-1000'''
        fmt = '''(Z3)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_57(self):
        inp = '''10000'''
        fmt = '''(Z3)'''
        result = [256]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_58(self):
        inp = '''-10000'''
        fmt = '''(Z3)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_59(self):
        inp = '''100000'''
        fmt = '''(Z3)'''
        result = [256]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_60(self):
        inp = '''-100000'''
        fmt = '''(Z3)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_61(self):
        inp = '''123456789'''
        fmt = '''(Z3)'''
        result = [291]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_62(self):
        inp = '''ff'''
        fmt = '''(Z3)'''
        result = [255]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_63(self):
        inp = '''F'''
        fmt = '''(Z3)'''
        result = [15]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_64(self):
        inp = ''' F F F'''
        fmt = '''(Z3)'''
        result = [15]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_65(self):
        inp = '''A a 2B'''
        fmt = '''(Z3)'''
        result = [170]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_66(self):
        inp = '''A.'''
        fmt = '''(Z3)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_67(self):
        inp = '''0'''
        fmt = '''(Z4)'''
        result = [0]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_68(self):
        inp = '''-0'''
        fmt = '''(Z4)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_69(self):
        inp = '''1'''
        fmt = '''(Z4)'''
        result = [1]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_70(self):
        inp = '''-1'''
        fmt = '''(Z4)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_71(self):
        inp = '''3'''
        fmt = '''(Z4)'''
        result = [3]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_72(self):
        inp = '''-3'''
        fmt = '''(Z4)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_73(self):
        inp = '''10'''
        fmt = '''(Z4)'''
        result = [16]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_74(self):
        inp = '''-10'''
        fmt = '''(Z4)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_75(self):
        inp = '''100'''
        fmt = '''(Z4)'''
        result = [256]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_76(self):
        inp = '''-100'''
        fmt = '''(Z4)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_77(self):
        inp = '''1000'''
        fmt = '''(Z4)'''
        result = [4096]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_78(self):
        inp = '''-1000'''
        fmt = '''(Z4)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_79(self):
        inp = '''10000'''
        fmt = '''(Z4)'''
        result = [4096]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_80(self):
        inp = '''-10000'''
        fmt = '''(Z4)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_81(self):
        inp = '''100000'''
        fmt = '''(Z4)'''
        result = [4096]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_82(self):
        inp = '''-100000'''
        fmt = '''(Z4)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_83(self):
        inp = '''123456789'''
        fmt = '''(Z4)'''
        result = [4660]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_84(self):
        inp = '''ff'''
        fmt = '''(Z4)'''
        result = [255]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_85(self):
        inp = '''F'''
        fmt = '''(Z4)'''
        result = [15]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_86(self):
        inp = ''' F F F'''
        fmt = '''(Z4)'''
        result = [255]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_87(self):
        inp = '''A a 2B'''
        fmt = '''(Z4)'''
        result = [170]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_88(self):
        inp = '''A.'''
        fmt = '''(Z4)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_89(self):
        inp = '''0'''
        fmt = '''(Z5)'''
        result = [0]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_90(self):
        inp = '''-0'''
        fmt = '''(Z5)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_91(self):
        inp = '''1'''
        fmt = '''(Z5)'''
        result = [1]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_92(self):
        inp = '''-1'''
        fmt = '''(Z5)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_93(self):
        inp = '''3'''
        fmt = '''(Z5)'''
        result = [3]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_94(self):
        inp = '''-3'''
        fmt = '''(Z5)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_95(self):
        inp = '''10'''
        fmt = '''(Z5)'''
        result = [16]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_96(self):
        inp = '''-10'''
        fmt = '''(Z5)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_97(self):
        inp = '''100'''
        fmt = '''(Z5)'''
        result = [256]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_98(self):
        inp = '''-100'''
        fmt = '''(Z5)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_99(self):
        inp = '''1000'''
        fmt = '''(Z5)'''
        result = [4096]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_100(self):
        inp = '''-1000'''
        fmt = '''(Z5)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_101(self):
        inp = '''10000'''
        fmt = '''(Z5)'''
        result = [65536]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_102(self):
        inp = '''-10000'''
        fmt = '''(Z5)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_103(self):
        inp = '''100000'''
        fmt = '''(Z5)'''
        result = [65536]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_104(self):
        inp = '''-100000'''
        fmt = '''(Z5)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_105(self):
        inp = '''123456789'''
        fmt = '''(Z5)'''
        result = [74565]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_106(self):
        inp = '''ff'''
        fmt = '''(Z5)'''
        result = [255]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_107(self):
        inp = '''F'''
        fmt = '''(Z5)'''
        result = [15]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_108(self):
        inp = ''' F F F'''
        fmt = '''(Z5)'''
        result = [255]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_109(self):
        inp = '''A a 2B'''
        fmt = '''(Z5)'''
        result = [2722]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_110(self):
        inp = '''A.'''
        fmt = '''(Z5)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_111(self):
        inp = '''0'''
        fmt = '''(Z6)'''
        result = [0]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_112(self):
        inp = '''-0'''
        fmt = '''(Z6)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_113(self):
        inp = '''1'''
        fmt = '''(Z6)'''
        result = [1]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_114(self):
        inp = '''-1'''
        fmt = '''(Z6)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_115(self):
        inp = '''3'''
        fmt = '''(Z6)'''
        result = [3]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_116(self):
        inp = '''-3'''
        fmt = '''(Z6)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_117(self):
        inp = '''10'''
        fmt = '''(Z6)'''
        result = [16]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_118(self):
        inp = '''-10'''
        fmt = '''(Z6)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_119(self):
        inp = '''100'''
        fmt = '''(Z6)'''
        result = [256]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_120(self):
        inp = '''-100'''
        fmt = '''(Z6)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_121(self):
        inp = '''1000'''
        fmt = '''(Z6)'''
        result = [4096]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_122(self):
        inp = '''-1000'''
        fmt = '''(Z6)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_123(self):
        inp = '''10000'''
        fmt = '''(Z6)'''
        result = [65536]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_124(self):
        inp = '''-10000'''
        fmt = '''(Z6)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_125(self):
        inp = '''100000'''
        fmt = '''(Z6)'''
        result = [1048576]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_126(self):
        inp = '''-100000'''
        fmt = '''(Z6)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_127(self):
        inp = '''123456789'''
        fmt = '''(Z6)'''
        result = [1193046]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_128(self):
        inp = '''ff'''
        fmt = '''(Z6)'''
        result = [255]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_129(self):
        inp = '''F'''
        fmt = '''(Z6)'''
        result = [15]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_130(self):
        inp = ''' F F F'''
        fmt = '''(Z6)'''
        result = [4095]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_131(self):
        inp = '''A a 2B'''
        fmt = '''(Z6)'''
        result = [43563]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_132(self):
        inp = '''A.'''
        fmt = '''(Z6)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_133(self):
        inp = '''0'''
        fmt = '''(Z7)'''
        result = [0]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_134(self):
        inp = '''-0'''
        fmt = '''(Z7)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_135(self):
        inp = '''1'''
        fmt = '''(Z7)'''
        result = [1]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_136(self):
        inp = '''-1'''
        fmt = '''(Z7)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_137(self):
        inp = '''3'''
        fmt = '''(Z7)'''
        result = [3]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_138(self):
        inp = '''-3'''
        fmt = '''(Z7)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_139(self):
        inp = '''10'''
        fmt = '''(Z7)'''
        result = [16]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_140(self):
        inp = '''-10'''
        fmt = '''(Z7)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_141(self):
        inp = '''100'''
        fmt = '''(Z7)'''
        result = [256]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_142(self):
        inp = '''-100'''
        fmt = '''(Z7)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_143(self):
        inp = '''1000'''
        fmt = '''(Z7)'''
        result = [4096]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_144(self):
        inp = '''-1000'''
        fmt = '''(Z7)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_145(self):
        inp = '''10000'''
        fmt = '''(Z7)'''
        result = [65536]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_146(self):
        inp = '''-10000'''
        fmt = '''(Z7)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_147(self):
        inp = '''100000'''
        fmt = '''(Z7)'''
        result = [1048576]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_148(self):
        inp = '''-100000'''
        fmt = '''(Z7)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_149(self):
        inp = '''123456789'''
        fmt = '''(Z7)'''
        result = [19088743]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_150(self):
        inp = '''ff'''
        fmt = '''(Z7)'''
        result = [255]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_151(self):
        inp = '''F'''
        fmt = '''(Z7)'''
        result = [15]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_152(self):
        inp = ''' F F F'''
        fmt = '''(Z7)'''
        result = [4095]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_153(self):
        inp = '''A a 2B'''
        fmt = '''(Z7)'''
        result = [43563]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_154(self):
        inp = '''A.'''
        fmt = '''(Z7)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_155(self):
        inp = '''0'''
        fmt = '''(Z8)'''
        result = [0]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_156(self):
        inp = '''-0'''
        fmt = '''(Z8)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_157(self):
        inp = '''1'''
        fmt = '''(Z8)'''
        result = [1]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_158(self):
        inp = '''-1'''
        fmt = '''(Z8)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_159(self):
        inp = '''3'''
        fmt = '''(Z8)'''
        result = [3]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_160(self):
        inp = '''-3'''
        fmt = '''(Z8)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_161(self):
        inp = '''10'''
        fmt = '''(Z8)'''
        result = [16]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_162(self):
        inp = '''-10'''
        fmt = '''(Z8)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_163(self):
        inp = '''100'''
        fmt = '''(Z8)'''
        result = [256]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_164(self):
        inp = '''-100'''
        fmt = '''(Z8)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_165(self):
        inp = '''1000'''
        fmt = '''(Z8)'''
        result = [4096]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_166(self):
        inp = '''-1000'''
        fmt = '''(Z8)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_167(self):
        inp = '''10000'''
        fmt = '''(Z8)'''
        result = [65536]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_168(self):
        inp = '''-10000'''
        fmt = '''(Z8)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_169(self):
        inp = '''100000'''
        fmt = '''(Z8)'''
        result = [1048576]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_170(self):
        inp = '''-100000'''
        fmt = '''(Z8)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_171(self):
        inp = '''123456789'''
        fmt = '''(Z8)'''
        result = [305419896]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_172(self):
        inp = '''ff'''
        fmt = '''(Z8)'''
        result = [255]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_173(self):
        inp = '''F'''
        fmt = '''(Z8)'''
        result = [15]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_174(self):
        inp = ''' F F F'''
        fmt = '''(Z8)'''
        result = [4095]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_175(self):
        inp = '''A a 2B'''
        fmt = '''(Z8)'''
        result = [43563]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_176(self):
        inp = '''A.'''
        fmt = '''(Z8)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_177(self):
        inp = '''0'''
        fmt = '''(Z9)'''
        result = [0]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_178(self):
        inp = '''-0'''
        fmt = '''(Z9)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_179(self):
        inp = '''1'''
        fmt = '''(Z9)'''
        result = [1]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_180(self):
        inp = '''-1'''
        fmt = '''(Z9)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_181(self):
        inp = '''3'''
        fmt = '''(Z9)'''
        result = [3]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_182(self):
        inp = '''-3'''
        fmt = '''(Z9)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_183(self):
        inp = '''10'''
        fmt = '''(Z9)'''
        result = [16]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_184(self):
        inp = '''-10'''
        fmt = '''(Z9)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_185(self):
        inp = '''100'''
        fmt = '''(Z9)'''
        result = [256]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_186(self):
        inp = '''-100'''
        fmt = '''(Z9)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_187(self):
        inp = '''1000'''
        fmt = '''(Z9)'''
        result = [4096]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_188(self):
        inp = '''-1000'''
        fmt = '''(Z9)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_189(self):
        inp = '''10000'''
        fmt = '''(Z9)'''
        result = [65536]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_190(self):
        inp = '''-10000'''
        fmt = '''(Z9)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_191(self):
        inp = '''100000'''
        fmt = '''(Z9)'''
        result = [1048576]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_192(self):
        inp = '''-100000'''
        fmt = '''(Z9)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_193(self):
        inp = '''123456789'''
        fmt = '''(Z9)'''
        result = [4886718345]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_194(self):
        inp = '''ff'''
        fmt = '''(Z9)'''
        result = [255]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_195(self):
        inp = '''F'''
        fmt = '''(Z9)'''
        result = [15]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_196(self):
        inp = ''' F F F'''
        fmt = '''(Z9)'''
        result = [4095]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_197(self):
        inp = '''A a 2B'''
        fmt = '''(Z9)'''
        result = [43563]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_198(self):
        inp = '''A.'''
        fmt = '''(Z9)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_199(self):
        inp = '''0'''
        fmt = '''(Z10)'''
        result = [0]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_200(self):
        inp = '''-0'''
        fmt = '''(Z10)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_201(self):
        inp = '''1'''
        fmt = '''(Z10)'''
        result = [1]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_202(self):
        inp = '''-1'''
        fmt = '''(Z10)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_203(self):
        inp = '''3'''
        fmt = '''(Z10)'''
        result = [3]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_204(self):
        inp = '''-3'''
        fmt = '''(Z10)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_205(self):
        inp = '''10'''
        fmt = '''(Z10)'''
        result = [16]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_206(self):
        inp = '''-10'''
        fmt = '''(Z10)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_207(self):
        inp = '''100'''
        fmt = '''(Z10)'''
        result = [256]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_208(self):
        inp = '''-100'''
        fmt = '''(Z10)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_209(self):
        inp = '''1000'''
        fmt = '''(Z10)'''
        result = [4096]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_210(self):
        inp = '''-1000'''
        fmt = '''(Z10)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_211(self):
        inp = '''10000'''
        fmt = '''(Z10)'''
        result = [65536]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_212(self):
        inp = '''-10000'''
        fmt = '''(Z10)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_213(self):
        inp = '''100000'''
        fmt = '''(Z10)'''
        result = [1048576]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_214(self):
        inp = '''-100000'''
        fmt = '''(Z10)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_215(self):
        inp = '''123456789'''
        fmt = '''(Z10)'''
        result = [4886718345]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_216(self):
        inp = '''ff'''
        fmt = '''(Z10)'''
        result = [255]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_217(self):
        inp = '''F'''
        fmt = '''(Z10)'''
        result = [15]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_218(self):
        inp = ''' F F F'''
        fmt = '''(Z10)'''
        result = [4095]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_219(self):
        inp = '''A a 2B'''
        fmt = '''(Z10)'''
        result = [43563]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_220(self):
        inp = '''A.'''
        fmt = '''(Z10)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_221(self):
        inp = '''0'''
        fmt = '''(Z1.0)'''
        result = [0]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_222(self):
        inp = '''-0'''
        fmt = '''(Z1.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_223(self):
        inp = '''1'''
        fmt = '''(Z1.0)'''
        result = [1]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_224(self):
        inp = '''-1'''
        fmt = '''(Z1.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_225(self):
        inp = '''3'''
        fmt = '''(Z1.0)'''
        result = [3]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_226(self):
        inp = '''-3'''
        fmt = '''(Z1.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_227(self):
        inp = '''10'''
        fmt = '''(Z1.0)'''
        result = [1]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_228(self):
        inp = '''-10'''
        fmt = '''(Z1.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_229(self):
        inp = '''100'''
        fmt = '''(Z1.0)'''
        result = [1]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_230(self):
        inp = '''-100'''
        fmt = '''(Z1.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_231(self):
        inp = '''1000'''
        fmt = '''(Z1.0)'''
        result = [1]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_232(self):
        inp = '''-1000'''
        fmt = '''(Z1.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_233(self):
        inp = '''10000'''
        fmt = '''(Z1.0)'''
        result = [1]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_234(self):
        inp = '''-10000'''
        fmt = '''(Z1.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_235(self):
        inp = '''100000'''
        fmt = '''(Z1.0)'''
        result = [1]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_236(self):
        inp = '''-100000'''
        fmt = '''(Z1.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_237(self):
        inp = '''123456789'''
        fmt = '''(Z1.0)'''
        result = [1]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_238(self):
        inp = '''ff'''
        fmt = '''(Z1.0)'''
        result = [15]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_239(self):
        inp = '''F'''
        fmt = '''(Z1.0)'''
        result = [15]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_240(self):
        inp = ''' F F F'''
        fmt = '''(Z1.0)'''
        result = [0]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_241(self):
        inp = '''A a 2B'''
        fmt = '''(Z1.0)'''
        result = [10]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_242(self):
        inp = '''A.'''
        fmt = '''(Z1.0)'''
        result = [10]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_243(self):
        inp = '''0'''
        fmt = '''(Z2.0)'''
        result = [0]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_244(self):
        inp = '''-0'''
        fmt = '''(Z2.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_245(self):
        inp = '''1'''
        fmt = '''(Z2.0)'''
        result = [1]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_246(self):
        inp = '''-1'''
        fmt = '''(Z2.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_247(self):
        inp = '''3'''
        fmt = '''(Z2.0)'''
        result = [3]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_248(self):
        inp = '''-3'''
        fmt = '''(Z2.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_249(self):
        inp = '''10'''
        fmt = '''(Z2.0)'''
        result = [16]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_250(self):
        inp = '''-10'''
        fmt = '''(Z2.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_251(self):
        inp = '''100'''
        fmt = '''(Z2.0)'''
        result = [16]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_252(self):
        inp = '''-100'''
        fmt = '''(Z2.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_253(self):
        inp = '''1000'''
        fmt = '''(Z2.0)'''
        result = [16]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_254(self):
        inp = '''-1000'''
        fmt = '''(Z2.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_255(self):
        inp = '''10000'''
        fmt = '''(Z2.0)'''
        result = [16]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_256(self):
        inp = '''-10000'''
        fmt = '''(Z2.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_257(self):
        inp = '''100000'''
        fmt = '''(Z2.0)'''
        result = [16]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_258(self):
        inp = '''-100000'''
        fmt = '''(Z2.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_259(self):
        inp = '''123456789'''
        fmt = '''(Z2.0)'''
        result = [18]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_260(self):
        inp = '''ff'''
        fmt = '''(Z2.0)'''
        result = [255]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_261(self):
        inp = '''F'''
        fmt = '''(Z2.0)'''
        result = [15]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_262(self):
        inp = ''' F F F'''
        fmt = '''(Z2.0)'''
        result = [15]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_263(self):
        inp = '''A a 2B'''
        fmt = '''(Z2.0)'''
        result = [10]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_264(self):
        inp = '''A.'''
        fmt = '''(Z2.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_265(self):
        inp = '''0'''
        fmt = '''(Z3.0)'''
        result = [0]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_266(self):
        inp = '''-0'''
        fmt = '''(Z3.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_267(self):
        inp = '''1'''
        fmt = '''(Z3.0)'''
        result = [1]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_268(self):
        inp = '''-1'''
        fmt = '''(Z3.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_269(self):
        inp = '''3'''
        fmt = '''(Z3.0)'''
        result = [3]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_270(self):
        inp = '''-3'''
        fmt = '''(Z3.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_271(self):
        inp = '''10'''
        fmt = '''(Z3.0)'''
        result = [16]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_272(self):
        inp = '''-10'''
        fmt = '''(Z3.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_273(self):
        inp = '''100'''
        fmt = '''(Z3.0)'''
        result = [256]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_274(self):
        inp = '''-100'''
        fmt = '''(Z3.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_275(self):
        inp = '''1000'''
        fmt = '''(Z3.0)'''
        result = [256]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_276(self):
        inp = '''-1000'''
        fmt = '''(Z3.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_277(self):
        inp = '''10000'''
        fmt = '''(Z3.0)'''
        result = [256]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_278(self):
        inp = '''-10000'''
        fmt = '''(Z3.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_279(self):
        inp = '''100000'''
        fmt = '''(Z3.0)'''
        result = [256]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_280(self):
        inp = '''-100000'''
        fmt = '''(Z3.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_281(self):
        inp = '''123456789'''
        fmt = '''(Z3.0)'''
        result = [291]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_282(self):
        inp = '''ff'''
        fmt = '''(Z3.0)'''
        result = [255]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_283(self):
        inp = '''F'''
        fmt = '''(Z3.0)'''
        result = [15]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_284(self):
        inp = ''' F F F'''
        fmt = '''(Z3.0)'''
        result = [15]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_285(self):
        inp = '''A a 2B'''
        fmt = '''(Z3.0)'''
        result = [170]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_286(self):
        inp = '''A.'''
        fmt = '''(Z3.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_287(self):
        inp = '''0'''
        fmt = '''(Z4.0)'''
        result = [0]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_288(self):
        inp = '''-0'''
        fmt = '''(Z4.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_289(self):
        inp = '''1'''
        fmt = '''(Z4.0)'''
        result = [1]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_290(self):
        inp = '''-1'''
        fmt = '''(Z4.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_291(self):
        inp = '''3'''
        fmt = '''(Z4.0)'''
        result = [3]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_292(self):
        inp = '''-3'''
        fmt = '''(Z4.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_293(self):
        inp = '''10'''
        fmt = '''(Z4.0)'''
        result = [16]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_294(self):
        inp = '''-10'''
        fmt = '''(Z4.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_295(self):
        inp = '''100'''
        fmt = '''(Z4.0)'''
        result = [256]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_296(self):
        inp = '''-100'''
        fmt = '''(Z4.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_297(self):
        inp = '''1000'''
        fmt = '''(Z4.0)'''
        result = [4096]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_298(self):
        inp = '''-1000'''
        fmt = '''(Z4.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_299(self):
        inp = '''10000'''
        fmt = '''(Z4.0)'''
        result = [4096]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_300(self):
        inp = '''-10000'''
        fmt = '''(Z4.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_301(self):
        inp = '''100000'''
        fmt = '''(Z4.0)'''
        result = [4096]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_302(self):
        inp = '''-100000'''
        fmt = '''(Z4.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_303(self):
        inp = '''123456789'''
        fmt = '''(Z4.0)'''
        result = [4660]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_304(self):
        inp = '''ff'''
        fmt = '''(Z4.0)'''
        result = [255]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_305(self):
        inp = '''F'''
        fmt = '''(Z4.0)'''
        result = [15]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_306(self):
        inp = ''' F F F'''
        fmt = '''(Z4.0)'''
        result = [255]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_307(self):
        inp = '''A a 2B'''
        fmt = '''(Z4.0)'''
        result = [170]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_308(self):
        inp = '''A.'''
        fmt = '''(Z4.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_309(self):
        inp = '''0'''
        fmt = '''(Z5.0)'''
        result = [0]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_310(self):
        inp = '''-0'''
        fmt = '''(Z5.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_311(self):
        inp = '''1'''
        fmt = '''(Z5.0)'''
        result = [1]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_312(self):
        inp = '''-1'''
        fmt = '''(Z5.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_313(self):
        inp = '''3'''
        fmt = '''(Z5.0)'''
        result = [3]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_314(self):
        inp = '''-3'''
        fmt = '''(Z5.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_315(self):
        inp = '''10'''
        fmt = '''(Z5.0)'''
        result = [16]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_316(self):
        inp = '''-10'''
        fmt = '''(Z5.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_317(self):
        inp = '''100'''
        fmt = '''(Z5.0)'''
        result = [256]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_318(self):
        inp = '''-100'''
        fmt = '''(Z5.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_319(self):
        inp = '''1000'''
        fmt = '''(Z5.0)'''
        result = [4096]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_320(self):
        inp = '''-1000'''
        fmt = '''(Z5.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_321(self):
        inp = '''10000'''
        fmt = '''(Z5.0)'''
        result = [65536]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_322(self):
        inp = '''-10000'''
        fmt = '''(Z5.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_323(self):
        inp = '''100000'''
        fmt = '''(Z5.0)'''
        result = [65536]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_324(self):
        inp = '''-100000'''
        fmt = '''(Z5.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_325(self):
        inp = '''123456789'''
        fmt = '''(Z5.0)'''
        result = [74565]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_326(self):
        inp = '''ff'''
        fmt = '''(Z5.0)'''
        result = [255]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_327(self):
        inp = '''F'''
        fmt = '''(Z5.0)'''
        result = [15]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_328(self):
        inp = ''' F F F'''
        fmt = '''(Z5.0)'''
        result = [255]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_329(self):
        inp = '''A a 2B'''
        fmt = '''(Z5.0)'''
        result = [2722]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_330(self):
        inp = '''A.'''
        fmt = '''(Z5.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_331(self):
        inp = '''0'''
        fmt = '''(Z6.0)'''
        result = [0]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_332(self):
        inp = '''-0'''
        fmt = '''(Z6.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_333(self):
        inp = '''1'''
        fmt = '''(Z6.0)'''
        result = [1]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_334(self):
        inp = '''-1'''
        fmt = '''(Z6.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_335(self):
        inp = '''3'''
        fmt = '''(Z6.0)'''
        result = [3]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_336(self):
        inp = '''-3'''
        fmt = '''(Z6.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_337(self):
        inp = '''10'''
        fmt = '''(Z6.0)'''
        result = [16]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_338(self):
        inp = '''-10'''
        fmt = '''(Z6.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_339(self):
        inp = '''100'''
        fmt = '''(Z6.0)'''
        result = [256]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_340(self):
        inp = '''-100'''
        fmt = '''(Z6.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_341(self):
        inp = '''1000'''
        fmt = '''(Z6.0)'''
        result = [4096]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_342(self):
        inp = '''-1000'''
        fmt = '''(Z6.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_343(self):
        inp = '''10000'''
        fmt = '''(Z6.0)'''
        result = [65536]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_344(self):
        inp = '''-10000'''
        fmt = '''(Z6.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_345(self):
        inp = '''100000'''
        fmt = '''(Z6.0)'''
        result = [1048576]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_346(self):
        inp = '''-100000'''
        fmt = '''(Z6.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_347(self):
        inp = '''123456789'''
        fmt = '''(Z6.0)'''
        result = [1193046]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_348(self):
        inp = '''ff'''
        fmt = '''(Z6.0)'''
        result = [255]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_349(self):
        inp = '''F'''
        fmt = '''(Z6.0)'''
        result = [15]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_350(self):
        inp = ''' F F F'''
        fmt = '''(Z6.0)'''
        result = [4095]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_351(self):
        inp = '''A a 2B'''
        fmt = '''(Z6.0)'''
        result = [43563]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_352(self):
        inp = '''A.'''
        fmt = '''(Z6.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_353(self):
        inp = '''0'''
        fmt = '''(Z7.0)'''
        result = [0]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_354(self):
        inp = '''-0'''
        fmt = '''(Z7.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_355(self):
        inp = '''1'''
        fmt = '''(Z7.0)'''
        result = [1]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_356(self):
        inp = '''-1'''
        fmt = '''(Z7.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_357(self):
        inp = '''3'''
        fmt = '''(Z7.0)'''
        result = [3]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_358(self):
        inp = '''-3'''
        fmt = '''(Z7.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_359(self):
        inp = '''10'''
        fmt = '''(Z7.0)'''
        result = [16]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_360(self):
        inp = '''-10'''
        fmt = '''(Z7.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_361(self):
        inp = '''100'''
        fmt = '''(Z7.0)'''
        result = [256]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_362(self):
        inp = '''-100'''
        fmt = '''(Z7.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_363(self):
        inp = '''1000'''
        fmt = '''(Z7.0)'''
        result = [4096]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_364(self):
        inp = '''-1000'''
        fmt = '''(Z7.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_365(self):
        inp = '''10000'''
        fmt = '''(Z7.0)'''
        result = [65536]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_366(self):
        inp = '''-10000'''
        fmt = '''(Z7.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_367(self):
        inp = '''100000'''
        fmt = '''(Z7.0)'''
        result = [1048576]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_368(self):
        inp = '''-100000'''
        fmt = '''(Z7.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_369(self):
        inp = '''123456789'''
        fmt = '''(Z7.0)'''
        result = [19088743]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_370(self):
        inp = '''ff'''
        fmt = '''(Z7.0)'''
        result = [255]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_371(self):
        inp = '''F'''
        fmt = '''(Z7.0)'''
        result = [15]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_372(self):
        inp = ''' F F F'''
        fmt = '''(Z7.0)'''
        result = [4095]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_373(self):
        inp = '''A a 2B'''
        fmt = '''(Z7.0)'''
        result = [43563]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_374(self):
        inp = '''A.'''
        fmt = '''(Z7.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_375(self):
        inp = '''0'''
        fmt = '''(Z8.0)'''
        result = [0]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_376(self):
        inp = '''-0'''
        fmt = '''(Z8.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_377(self):
        inp = '''1'''
        fmt = '''(Z8.0)'''
        result = [1]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_378(self):
        inp = '''-1'''
        fmt = '''(Z8.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_379(self):
        inp = '''3'''
        fmt = '''(Z8.0)'''
        result = [3]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_380(self):
        inp = '''-3'''
        fmt = '''(Z8.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_381(self):
        inp = '''10'''
        fmt = '''(Z8.0)'''
        result = [16]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_382(self):
        inp = '''-10'''
        fmt = '''(Z8.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_383(self):
        inp = '''100'''
        fmt = '''(Z8.0)'''
        result = [256]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_384(self):
        inp = '''-100'''
        fmt = '''(Z8.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_385(self):
        inp = '''1000'''
        fmt = '''(Z8.0)'''
        result = [4096]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_386(self):
        inp = '''-1000'''
        fmt = '''(Z8.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_387(self):
        inp = '''10000'''
        fmt = '''(Z8.0)'''
        result = [65536]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_388(self):
        inp = '''-10000'''
        fmt = '''(Z8.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_389(self):
        inp = '''100000'''
        fmt = '''(Z8.0)'''
        result = [1048576]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_390(self):
        inp = '''-100000'''
        fmt = '''(Z8.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_391(self):
        inp = '''123456789'''
        fmt = '''(Z8.0)'''
        result = [305419896]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_392(self):
        inp = '''ff'''
        fmt = '''(Z8.0)'''
        result = [255]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_393(self):
        inp = '''F'''
        fmt = '''(Z8.0)'''
        result = [15]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_394(self):
        inp = ''' F F F'''
        fmt = '''(Z8.0)'''
        result = [4095]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_395(self):
        inp = '''A a 2B'''
        fmt = '''(Z8.0)'''
        result = [43563]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_396(self):
        inp = '''A.'''
        fmt = '''(Z8.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_397(self):
        inp = '''0'''
        fmt = '''(Z9.0)'''
        result = [0]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_398(self):
        inp = '''-0'''
        fmt = '''(Z9.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_399(self):
        inp = '''1'''
        fmt = '''(Z9.0)'''
        result = [1]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_400(self):
        inp = '''-1'''
        fmt = '''(Z9.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_401(self):
        inp = '''3'''
        fmt = '''(Z9.0)'''
        result = [3]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_402(self):
        inp = '''-3'''
        fmt = '''(Z9.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_403(self):
        inp = '''10'''
        fmt = '''(Z9.0)'''
        result = [16]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_404(self):
        inp = '''-10'''
        fmt = '''(Z9.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_405(self):
        inp = '''100'''
        fmt = '''(Z9.0)'''
        result = [256]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_406(self):
        inp = '''-100'''
        fmt = '''(Z9.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_407(self):
        inp = '''1000'''
        fmt = '''(Z9.0)'''
        result = [4096]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_408(self):
        inp = '''-1000'''
        fmt = '''(Z9.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_409(self):
        inp = '''10000'''
        fmt = '''(Z9.0)'''
        result = [65536]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_410(self):
        inp = '''-10000'''
        fmt = '''(Z9.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_411(self):
        inp = '''100000'''
        fmt = '''(Z9.0)'''
        result = [1048576]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_412(self):
        inp = '''-100000'''
        fmt = '''(Z9.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_413(self):
        inp = '''123456789'''
        fmt = '''(Z9.0)'''
        result = [4886718345]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_414(self):
        inp = '''ff'''
        fmt = '''(Z9.0)'''
        result = [255]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_415(self):
        inp = '''F'''
        fmt = '''(Z9.0)'''
        result = [15]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_416(self):
        inp = ''' F F F'''
        fmt = '''(Z9.0)'''
        result = [4095]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_417(self):
        inp = '''A a 2B'''
        fmt = '''(Z9.0)'''
        result = [43563]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_418(self):
        inp = '''A.'''
        fmt = '''(Z9.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_419(self):
        inp = '''0'''
        fmt = '''(Z10.0)'''
        result = [0]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_420(self):
        inp = '''-0'''
        fmt = '''(Z10.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_421(self):
        inp = '''1'''
        fmt = '''(Z10.0)'''
        result = [1]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_422(self):
        inp = '''-1'''
        fmt = '''(Z10.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_423(self):
        inp = '''3'''
        fmt = '''(Z10.0)'''
        result = [3]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_424(self):
        inp = '''-3'''
        fmt = '''(Z10.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_425(self):
        inp = '''10'''
        fmt = '''(Z10.0)'''
        result = [16]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_426(self):
        inp = '''-10'''
        fmt = '''(Z10.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_427(self):
        inp = '''100'''
        fmt = '''(Z10.0)'''
        result = [256]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_428(self):
        inp = '''-100'''
        fmt = '''(Z10.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_429(self):
        inp = '''1000'''
        fmt = '''(Z10.0)'''
        result = [4096]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_430(self):
        inp = '''-1000'''
        fmt = '''(Z10.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_431(self):
        inp = '''10000'''
        fmt = '''(Z10.0)'''
        result = [65536]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_432(self):
        inp = '''-10000'''
        fmt = '''(Z10.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_433(self):
        inp = '''100000'''
        fmt = '''(Z10.0)'''
        result = [1048576]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_434(self):
        inp = '''-100000'''
        fmt = '''(Z10.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_435(self):
        inp = '''123456789'''
        fmt = '''(Z10.0)'''
        result = [4886718345]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_436(self):
        inp = '''ff'''
        fmt = '''(Z10.0)'''
        result = [255]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_437(self):
        inp = '''F'''
        fmt = '''(Z10.0)'''
        result = [15]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_438(self):
        inp = ''' F F F'''
        fmt = '''(Z10.0)'''
        result = [4095]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_439(self):
        inp = '''A a 2B'''
        fmt = '''(Z10.0)'''
        result = [43563]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_440(self):
        inp = '''A.'''
        fmt = '''(Z10.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_441(self):
        inp = '''0'''
        fmt = '''(Z1.1)'''
        result = [0]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_442(self):
        inp = '''-0'''
        fmt = '''(Z1.1)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_443(self):
        inp = '''1'''
        fmt = '''(Z1.1)'''
        result = [1]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_444(self):
        inp = '''-1'''
        fmt = '''(Z1.1)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_445(self):
        inp = '''3'''
        fmt = '''(Z1.1)'''
        result = [3]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_446(self):
        inp = '''-3'''
        fmt = '''(Z1.1)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_447(self):
        inp = '''10'''
        fmt = '''(Z1.1)'''
        result = [1]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_448(self):
        inp = '''-10'''
        fmt = '''(Z1.1)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_449(self):
        inp = '''100'''
        fmt = '''(Z1.1)'''
        result = [1]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_450(self):
        inp = '''-100'''
        fmt = '''(Z1.1)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_451(self):
        inp = '''1000'''
        fmt = '''(Z1.1)'''
        result = [1]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_452(self):
        inp = '''-1000'''
        fmt = '''(Z1.1)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_453(self):
        inp = '''10000'''
        fmt = '''(Z1.1)'''
        result = [1]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_454(self):
        inp = '''-10000'''
        fmt = '''(Z1.1)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_455(self):
        inp = '''100000'''
        fmt = '''(Z1.1)'''
        result = [1]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_456(self):
        inp = '''-100000'''
        fmt = '''(Z1.1)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_457(self):
        inp = '''123456789'''
        fmt = '''(Z1.1)'''
        result = [1]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_458(self):
        inp = '''ff'''
        fmt = '''(Z1.1)'''
        result = [15]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_459(self):
        inp = '''F'''
        fmt = '''(Z1.1)'''
        result = [15]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_460(self):
        inp = ''' F F F'''
        fmt = '''(Z1.1)'''
        result = [0]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_461(self):
        inp = '''A a 2B'''
        fmt = '''(Z1.1)'''
        result = [10]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_462(self):
        inp = '''A.'''
        fmt = '''(Z1.1)'''
        result = [10]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_463(self):
        inp = '''0'''
        fmt = '''(Z2.1)'''
        result = [0]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_464(self):
        inp = '''-0'''
        fmt = '''(Z2.1)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_465(self):
        inp = '''1'''
        fmt = '''(Z2.1)'''
        result = [1]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_466(self):
        inp = '''-1'''
        fmt = '''(Z2.1)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_467(self):
        inp = '''3'''
        fmt = '''(Z2.1)'''
        result = [3]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_468(self):
        inp = '''-3'''
        fmt = '''(Z2.1)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_469(self):
        inp = '''10'''
        fmt = '''(Z2.1)'''
        result = [16]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_470(self):
        inp = '''-10'''
        fmt = '''(Z2.1)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_471(self):
        inp = '''100'''
        fmt = '''(Z2.1)'''
        result = [16]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_472(self):
        inp = '''-100'''
        fmt = '''(Z2.1)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_473(self):
        inp = '''1000'''
        fmt = '''(Z2.1)'''
        result = [16]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_474(self):
        inp = '''-1000'''
        fmt = '''(Z2.1)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_475(self):
        inp = '''10000'''
        fmt = '''(Z2.1)'''
        result = [16]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_476(self):
        inp = '''-10000'''
        fmt = '''(Z2.1)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_477(self):
        inp = '''100000'''
        fmt = '''(Z2.1)'''
        result = [16]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_478(self):
        inp = '''-100000'''
        fmt = '''(Z2.1)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_479(self):
        inp = '''123456789'''
        fmt = '''(Z2.1)'''
        result = [18]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_480(self):
        inp = '''ff'''
        fmt = '''(Z2.1)'''
        result = [255]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_481(self):
        inp = '''F'''
        fmt = '''(Z2.1)'''
        result = [15]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_482(self):
        inp = ''' F F F'''
        fmt = '''(Z2.1)'''
        result = [15]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_483(self):
        inp = '''A a 2B'''
        fmt = '''(Z2.1)'''
        result = [10]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_484(self):
        inp = '''A.'''
        fmt = '''(Z2.1)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_485(self):
        inp = '''0'''
        fmt = '''(Z3.1)'''
        result = [0]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_486(self):
        inp = '''-0'''
        fmt = '''(Z3.1)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_487(self):
        inp = '''1'''
        fmt = '''(Z3.1)'''
        result = [1]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_488(self):
        inp = '''-1'''
        fmt = '''(Z3.1)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_489(self):
        inp = '''3'''
        fmt = '''(Z3.1)'''
        result = [3]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_490(self):
        inp = '''-3'''
        fmt = '''(Z3.1)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_491(self):
        inp = '''10'''
        fmt = '''(Z3.1)'''
        result = [16]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_492(self):
        inp = '''-10'''
        fmt = '''(Z3.1)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_493(self):
        inp = '''100'''
        fmt = '''(Z3.1)'''
        result = [256]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_494(self):
        inp = '''-100'''
        fmt = '''(Z3.1)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_495(self):
        inp = '''1000'''
        fmt = '''(Z3.1)'''
        result = [256]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_496(self):
        inp = '''-1000'''
        fmt = '''(Z3.1)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_497(self):
        inp = '''10000'''
        fmt = '''(Z3.1)'''
        result = [256]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_498(self):
        inp = '''-10000'''
        fmt = '''(Z3.1)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_499(self):
        inp = '''100000'''
        fmt = '''(Z3.1)'''
        result = [256]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_500(self):
        inp = '''-100000'''
        fmt = '''(Z3.1)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_501(self):
        inp = '''123456789'''
        fmt = '''(Z3.1)'''
        result = [291]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_502(self):
        inp = '''ff'''
        fmt = '''(Z3.1)'''
        result = [255]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_503(self):
        inp = '''F'''
        fmt = '''(Z3.1)'''
        result = [15]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_504(self):
        inp = ''' F F F'''
        fmt = '''(Z3.1)'''
        result = [15]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_505(self):
        inp = '''A a 2B'''
        fmt = '''(Z3.1)'''
        result = [170]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_506(self):
        inp = '''A.'''
        fmt = '''(Z3.1)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_507(self):
        inp = '''0'''
        fmt = '''(Z4.1)'''
        result = [0]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_508(self):
        inp = '''-0'''
        fmt = '''(Z4.1)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_509(self):
        inp = '''1'''
        fmt = '''(Z4.1)'''
        result = [1]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_510(self):
        inp = '''-1'''
        fmt = '''(Z4.1)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_511(self):
        inp = '''3'''
        fmt = '''(Z4.1)'''
        result = [3]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_512(self):
        inp = '''-3'''
        fmt = '''(Z4.1)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_513(self):
        inp = '''10'''
        fmt = '''(Z4.1)'''
        result = [16]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_514(self):
        inp = '''-10'''
        fmt = '''(Z4.1)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_515(self):
        inp = '''100'''
        fmt = '''(Z4.1)'''
        result = [256]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_516(self):
        inp = '''-100'''
        fmt = '''(Z4.1)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_517(self):
        inp = '''1000'''
        fmt = '''(Z4.1)'''
        result = [4096]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_518(self):
        inp = '''-1000'''
        fmt = '''(Z4.1)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_519(self):
        inp = '''10000'''
        fmt = '''(Z4.1)'''
        result = [4096]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_520(self):
        inp = '''-10000'''
        fmt = '''(Z4.1)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_521(self):
        inp = '''100000'''
        fmt = '''(Z4.1)'''
        result = [4096]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_522(self):
        inp = '''-100000'''
        fmt = '''(Z4.1)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_523(self):
        inp = '''123456789'''
        fmt = '''(Z4.1)'''
        result = [4660]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_524(self):
        inp = '''ff'''
        fmt = '''(Z4.1)'''
        result = [255]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_525(self):
        inp = '''F'''
        fmt = '''(Z4.1)'''
        result = [15]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_526(self):
        inp = ''' F F F'''
        fmt = '''(Z4.1)'''
        result = [255]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_527(self):
        inp = '''A a 2B'''
        fmt = '''(Z4.1)'''
        result = [170]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_528(self):
        inp = '''A.'''
        fmt = '''(Z4.1)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_529(self):
        inp = '''0'''
        fmt = '''(Z5.1)'''
        result = [0]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_530(self):
        inp = '''-0'''
        fmt = '''(Z5.1)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_531(self):
        inp = '''1'''
        fmt = '''(Z5.1)'''
        result = [1]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_532(self):
        inp = '''-1'''
        fmt = '''(Z5.1)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_533(self):
        inp = '''3'''
        fmt = '''(Z5.1)'''
        result = [3]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_534(self):
        inp = '''-3'''
        fmt = '''(Z5.1)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_535(self):
        inp = '''10'''
        fmt = '''(Z5.1)'''
        result = [16]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_536(self):
        inp = '''-10'''
        fmt = '''(Z5.1)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_537(self):
        inp = '''100'''
        fmt = '''(Z5.1)'''
        result = [256]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_538(self):
        inp = '''-100'''
        fmt = '''(Z5.1)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_539(self):
        inp = '''1000'''
        fmt = '''(Z5.1)'''
        result = [4096]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_540(self):
        inp = '''-1000'''
        fmt = '''(Z5.1)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_541(self):
        inp = '''10000'''
        fmt = '''(Z5.1)'''
        result = [65536]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_542(self):
        inp = '''-10000'''
        fmt = '''(Z5.1)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_543(self):
        inp = '''100000'''
        fmt = '''(Z5.1)'''
        result = [65536]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_544(self):
        inp = '''-100000'''
        fmt = '''(Z5.1)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_545(self):
        inp = '''123456789'''
        fmt = '''(Z5.1)'''
        result = [74565]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_546(self):
        inp = '''ff'''
        fmt = '''(Z5.1)'''
        result = [255]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_547(self):
        inp = '''F'''
        fmt = '''(Z5.1)'''
        result = [15]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_548(self):
        inp = ''' F F F'''
        fmt = '''(Z5.1)'''
        result = [255]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_549(self):
        inp = '''A a 2B'''
        fmt = '''(Z5.1)'''
        result = [2722]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_550(self):
        inp = '''A.'''
        fmt = '''(Z5.1)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_551(self):
        inp = '''0'''
        fmt = '''(Z6.1)'''
        result = [0]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_552(self):
        inp = '''-0'''
        fmt = '''(Z6.1)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_553(self):
        inp = '''1'''
        fmt = '''(Z6.1)'''
        result = [1]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_554(self):
        inp = '''-1'''
        fmt = '''(Z6.1)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_555(self):
        inp = '''3'''
        fmt = '''(Z6.1)'''
        result = [3]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_556(self):
        inp = '''-3'''
        fmt = '''(Z6.1)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_557(self):
        inp = '''10'''
        fmt = '''(Z6.1)'''
        result = [16]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_558(self):
        inp = '''-10'''
        fmt = '''(Z6.1)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_559(self):
        inp = '''100'''
        fmt = '''(Z6.1)'''
        result = [256]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_560(self):
        inp = '''-100'''
        fmt = '''(Z6.1)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_561(self):
        inp = '''1000'''
        fmt = '''(Z6.1)'''
        result = [4096]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_562(self):
        inp = '''-1000'''
        fmt = '''(Z6.1)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_563(self):
        inp = '''10000'''
        fmt = '''(Z6.1)'''
        result = [65536]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_564(self):
        inp = '''-10000'''
        fmt = '''(Z6.1)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_565(self):
        inp = '''100000'''
        fmt = '''(Z6.1)'''
        result = [1048576]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_566(self):
        inp = '''-100000'''
        fmt = '''(Z6.1)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_567(self):
        inp = '''123456789'''
        fmt = '''(Z6.1)'''
        result = [1193046]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_568(self):
        inp = '''ff'''
        fmt = '''(Z6.1)'''
        result = [255]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_569(self):
        inp = '''F'''
        fmt = '''(Z6.1)'''
        result = [15]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_570(self):
        inp = ''' F F F'''
        fmt = '''(Z6.1)'''
        result = [4095]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_571(self):
        inp = '''A a 2B'''
        fmt = '''(Z6.1)'''
        result = [43563]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_572(self):
        inp = '''A.'''
        fmt = '''(Z6.1)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_573(self):
        inp = '''0'''
        fmt = '''(Z7.1)'''
        result = [0]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_574(self):
        inp = '''-0'''
        fmt = '''(Z7.1)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_575(self):
        inp = '''1'''
        fmt = '''(Z7.1)'''
        result = [1]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_576(self):
        inp = '''-1'''
        fmt = '''(Z7.1)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_577(self):
        inp = '''3'''
        fmt = '''(Z7.1)'''
        result = [3]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_578(self):
        inp = '''-3'''
        fmt = '''(Z7.1)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_579(self):
        inp = '''10'''
        fmt = '''(Z7.1)'''
        result = [16]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_580(self):
        inp = '''-10'''
        fmt = '''(Z7.1)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_581(self):
        inp = '''100'''
        fmt = '''(Z7.1)'''
        result = [256]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_582(self):
        inp = '''-100'''
        fmt = '''(Z7.1)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_583(self):
        inp = '''1000'''
        fmt = '''(Z7.1)'''
        result = [4096]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_584(self):
        inp = '''-1000'''
        fmt = '''(Z7.1)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_585(self):
        inp = '''10000'''
        fmt = '''(Z7.1)'''
        result = [65536]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_586(self):
        inp = '''-10000'''
        fmt = '''(Z7.1)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_587(self):
        inp = '''100000'''
        fmt = '''(Z7.1)'''
        result = [1048576]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_588(self):
        inp = '''-100000'''
        fmt = '''(Z7.1)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_589(self):
        inp = '''123456789'''
        fmt = '''(Z7.1)'''
        result = [19088743]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_590(self):
        inp = '''ff'''
        fmt = '''(Z7.1)'''
        result = [255]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_591(self):
        inp = '''F'''
        fmt = '''(Z7.1)'''
        result = [15]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_592(self):
        inp = ''' F F F'''
        fmt = '''(Z7.1)'''
        result = [4095]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_593(self):
        inp = '''A a 2B'''
        fmt = '''(Z7.1)'''
        result = [43563]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_594(self):
        inp = '''A.'''
        fmt = '''(Z7.1)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_595(self):
        inp = '''0'''
        fmt = '''(Z8.1)'''
        result = [0]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_596(self):
        inp = '''-0'''
        fmt = '''(Z8.1)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_597(self):
        inp = '''1'''
        fmt = '''(Z8.1)'''
        result = [1]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_598(self):
        inp = '''-1'''
        fmt = '''(Z8.1)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_599(self):
        inp = '''3'''
        fmt = '''(Z8.1)'''
        result = [3]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_600(self):
        inp = '''-3'''
        fmt = '''(Z8.1)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_601(self):
        inp = '''10'''
        fmt = '''(Z8.1)'''
        result = [16]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_602(self):
        inp = '''-10'''
        fmt = '''(Z8.1)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_603(self):
        inp = '''100'''
        fmt = '''(Z8.1)'''
        result = [256]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_604(self):
        inp = '''-100'''
        fmt = '''(Z8.1)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_605(self):
        inp = '''1000'''
        fmt = '''(Z8.1)'''
        result = [4096]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_606(self):
        inp = '''-1000'''
        fmt = '''(Z8.1)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_607(self):
        inp = '''10000'''
        fmt = '''(Z8.1)'''
        result = [65536]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_608(self):
        inp = '''-10000'''
        fmt = '''(Z8.1)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_609(self):
        inp = '''100000'''
        fmt = '''(Z8.1)'''
        result = [1048576]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_610(self):
        inp = '''-100000'''
        fmt = '''(Z8.1)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_611(self):
        inp = '''123456789'''
        fmt = '''(Z8.1)'''
        result = [305419896]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_612(self):
        inp = '''ff'''
        fmt = '''(Z8.1)'''
        result = [255]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_613(self):
        inp = '''F'''
        fmt = '''(Z8.1)'''
        result = [15]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_614(self):
        inp = ''' F F F'''
        fmt = '''(Z8.1)'''
        result = [4095]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_615(self):
        inp = '''A a 2B'''
        fmt = '''(Z8.1)'''
        result = [43563]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_616(self):
        inp = '''A.'''
        fmt = '''(Z8.1)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_617(self):
        inp = '''0'''
        fmt = '''(Z9.1)'''
        result = [0]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_618(self):
        inp = '''-0'''
        fmt = '''(Z9.1)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_619(self):
        inp = '''1'''
        fmt = '''(Z9.1)'''
        result = [1]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_620(self):
        inp = '''-1'''
        fmt = '''(Z9.1)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_621(self):
        inp = '''3'''
        fmt = '''(Z9.1)'''
        result = [3]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_622(self):
        inp = '''-3'''
        fmt = '''(Z9.1)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_623(self):
        inp = '''10'''
        fmt = '''(Z9.1)'''
        result = [16]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_624(self):
        inp = '''-10'''
        fmt = '''(Z9.1)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_625(self):
        inp = '''100'''
        fmt = '''(Z9.1)'''
        result = [256]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_626(self):
        inp = '''-100'''
        fmt = '''(Z9.1)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_627(self):
        inp = '''1000'''
        fmt = '''(Z9.1)'''
        result = [4096]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_628(self):
        inp = '''-1000'''
        fmt = '''(Z9.1)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_629(self):
        inp = '''10000'''
        fmt = '''(Z9.1)'''
        result = [65536]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_630(self):
        inp = '''-10000'''
        fmt = '''(Z9.1)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_631(self):
        inp = '''100000'''
        fmt = '''(Z9.1)'''
        result = [1048576]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_632(self):
        inp = '''-100000'''
        fmt = '''(Z9.1)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_633(self):
        inp = '''123456789'''
        fmt = '''(Z9.1)'''
        result = [4886718345]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_634(self):
        inp = '''ff'''
        fmt = '''(Z9.1)'''
        result = [255]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_635(self):
        inp = '''F'''
        fmt = '''(Z9.1)'''
        result = [15]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_636(self):
        inp = ''' F F F'''
        fmt = '''(Z9.1)'''
        result = [4095]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_637(self):
        inp = '''A a 2B'''
        fmt = '''(Z9.1)'''
        result = [43563]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_638(self):
        inp = '''A.'''
        fmt = '''(Z9.1)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_639(self):
        inp = '''0'''
        fmt = '''(Z10.1)'''
        result = [0]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_640(self):
        inp = '''-0'''
        fmt = '''(Z10.1)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_641(self):
        inp = '''1'''
        fmt = '''(Z10.1)'''
        result = [1]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_642(self):
        inp = '''-1'''
        fmt = '''(Z10.1)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_643(self):
        inp = '''3'''
        fmt = '''(Z10.1)'''
        result = [3]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_644(self):
        inp = '''-3'''
        fmt = '''(Z10.1)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_645(self):
        inp = '''10'''
        fmt = '''(Z10.1)'''
        result = [16]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_646(self):
        inp = '''-10'''
        fmt = '''(Z10.1)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_647(self):
        inp = '''100'''
        fmt = '''(Z10.1)'''
        result = [256]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_648(self):
        inp = '''-100'''
        fmt = '''(Z10.1)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_649(self):
        inp = '''1000'''
        fmt = '''(Z10.1)'''
        result = [4096]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_650(self):
        inp = '''-1000'''
        fmt = '''(Z10.1)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_651(self):
        inp = '''10000'''
        fmt = '''(Z10.1)'''
        result = [65536]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_652(self):
        inp = '''-10000'''
        fmt = '''(Z10.1)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_653(self):
        inp = '''100000'''
        fmt = '''(Z10.1)'''
        result = [1048576]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_654(self):
        inp = '''-100000'''
        fmt = '''(Z10.1)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_655(self):
        inp = '''123456789'''
        fmt = '''(Z10.1)'''
        result = [4886718345]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_656(self):
        inp = '''ff'''
        fmt = '''(Z10.1)'''
        result = [255]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_657(self):
        inp = '''F'''
        fmt = '''(Z10.1)'''
        result = [15]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_658(self):
        inp = ''' F F F'''
        fmt = '''(Z10.1)'''
        result = [4095]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_659(self):
        inp = '''A a 2B'''
        fmt = '''(Z10.1)'''
        result = [43563]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_660(self):
        inp = '''A.'''
        fmt = '''(Z10.1)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_661(self):
        inp = '''0'''
        fmt = '''(Z2.2)'''
        result = [0]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_662(self):
        inp = '''-0'''
        fmt = '''(Z2.2)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_663(self):
        inp = '''1'''
        fmt = '''(Z2.2)'''
        result = [1]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_664(self):
        inp = '''-1'''
        fmt = '''(Z2.2)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_665(self):
        inp = '''3'''
        fmt = '''(Z2.2)'''
        result = [3]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_666(self):
        inp = '''-3'''
        fmt = '''(Z2.2)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_667(self):
        inp = '''10'''
        fmt = '''(Z2.2)'''
        result = [16]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_668(self):
        inp = '''-10'''
        fmt = '''(Z2.2)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_669(self):
        inp = '''100'''
        fmt = '''(Z2.2)'''
        result = [16]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_670(self):
        inp = '''-100'''
        fmt = '''(Z2.2)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_671(self):
        inp = '''1000'''
        fmt = '''(Z2.2)'''
        result = [16]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_672(self):
        inp = '''-1000'''
        fmt = '''(Z2.2)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_673(self):
        inp = '''10000'''
        fmt = '''(Z2.2)'''
        result = [16]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_674(self):
        inp = '''-10000'''
        fmt = '''(Z2.2)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_675(self):
        inp = '''100000'''
        fmt = '''(Z2.2)'''
        result = [16]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_676(self):
        inp = '''-100000'''
        fmt = '''(Z2.2)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_677(self):
        inp = '''123456789'''
        fmt = '''(Z2.2)'''
        result = [18]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_678(self):
        inp = '''ff'''
        fmt = '''(Z2.2)'''
        result = [255]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_679(self):
        inp = '''F'''
        fmt = '''(Z2.2)'''
        result = [15]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_680(self):
        inp = ''' F F F'''
        fmt = '''(Z2.2)'''
        result = [15]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_681(self):
        inp = '''A a 2B'''
        fmt = '''(Z2.2)'''
        result = [10]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_682(self):
        inp = '''A.'''
        fmt = '''(Z2.2)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_683(self):
        inp = '''0'''
        fmt = '''(Z3.2)'''
        result = [0]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_684(self):
        inp = '''-0'''
        fmt = '''(Z3.2)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_685(self):
        inp = '''1'''
        fmt = '''(Z3.2)'''
        result = [1]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_686(self):
        inp = '''-1'''
        fmt = '''(Z3.2)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_687(self):
        inp = '''3'''
        fmt = '''(Z3.2)'''
        result = [3]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_688(self):
        inp = '''-3'''
        fmt = '''(Z3.2)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_689(self):
        inp = '''10'''
        fmt = '''(Z3.2)'''
        result = [16]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_690(self):
        inp = '''-10'''
        fmt = '''(Z3.2)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_691(self):
        inp = '''100'''
        fmt = '''(Z3.2)'''
        result = [256]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_692(self):
        inp = '''-100'''
        fmt = '''(Z3.2)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_693(self):
        inp = '''1000'''
        fmt = '''(Z3.2)'''
        result = [256]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_694(self):
        inp = '''-1000'''
        fmt = '''(Z3.2)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_695(self):
        inp = '''10000'''
        fmt = '''(Z3.2)'''
        result = [256]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_696(self):
        inp = '''-10000'''
        fmt = '''(Z3.2)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_697(self):
        inp = '''100000'''
        fmt = '''(Z3.2)'''
        result = [256]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_698(self):
        inp = '''-100000'''
        fmt = '''(Z3.2)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_699(self):
        inp = '''123456789'''
        fmt = '''(Z3.2)'''
        result = [291]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_700(self):
        inp = '''ff'''
        fmt = '''(Z3.2)'''
        result = [255]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_701(self):
        inp = '''F'''
        fmt = '''(Z3.2)'''
        result = [15]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_702(self):
        inp = ''' F F F'''
        fmt = '''(Z3.2)'''
        result = [15]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_703(self):
        inp = '''A a 2B'''
        fmt = '''(Z3.2)'''
        result = [170]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_704(self):
        inp = '''A.'''
        fmt = '''(Z3.2)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_705(self):
        inp = '''0'''
        fmt = '''(Z4.2)'''
        result = [0]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_706(self):
        inp = '''-0'''
        fmt = '''(Z4.2)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_707(self):
        inp = '''1'''
        fmt = '''(Z4.2)'''
        result = [1]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_708(self):
        inp = '''-1'''
        fmt = '''(Z4.2)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_709(self):
        inp = '''3'''
        fmt = '''(Z4.2)'''
        result = [3]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_710(self):
        inp = '''-3'''
        fmt = '''(Z4.2)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_711(self):
        inp = '''10'''
        fmt = '''(Z4.2)'''
        result = [16]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_712(self):
        inp = '''-10'''
        fmt = '''(Z4.2)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_713(self):
        inp = '''100'''
        fmt = '''(Z4.2)'''
        result = [256]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_714(self):
        inp = '''-100'''
        fmt = '''(Z4.2)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_715(self):
        inp = '''1000'''
        fmt = '''(Z4.2)'''
        result = [4096]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_716(self):
        inp = '''-1000'''
        fmt = '''(Z4.2)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_717(self):
        inp = '''10000'''
        fmt = '''(Z4.2)'''
        result = [4096]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_718(self):
        inp = '''-10000'''
        fmt = '''(Z4.2)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_719(self):
        inp = '''100000'''
        fmt = '''(Z4.2)'''
        result = [4096]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_720(self):
        inp = '''-100000'''
        fmt = '''(Z4.2)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_721(self):
        inp = '''123456789'''
        fmt = '''(Z4.2)'''
        result = [4660]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_722(self):
        inp = '''ff'''
        fmt = '''(Z4.2)'''
        result = [255]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_723(self):
        inp = '''F'''
        fmt = '''(Z4.2)'''
        result = [15]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_724(self):
        inp = ''' F F F'''
        fmt = '''(Z4.2)'''
        result = [255]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_725(self):
        inp = '''A a 2B'''
        fmt = '''(Z4.2)'''
        result = [170]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_726(self):
        inp = '''A.'''
        fmt = '''(Z4.2)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_727(self):
        inp = '''0'''
        fmt = '''(Z5.2)'''
        result = [0]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_728(self):
        inp = '''-0'''
        fmt = '''(Z5.2)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_729(self):
        inp = '''1'''
        fmt = '''(Z5.2)'''
        result = [1]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_730(self):
        inp = '''-1'''
        fmt = '''(Z5.2)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_731(self):
        inp = '''3'''
        fmt = '''(Z5.2)'''
        result = [3]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_732(self):
        inp = '''-3'''
        fmt = '''(Z5.2)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_733(self):
        inp = '''10'''
        fmt = '''(Z5.2)'''
        result = [16]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_734(self):
        inp = '''-10'''
        fmt = '''(Z5.2)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_735(self):
        inp = '''100'''
        fmt = '''(Z5.2)'''
        result = [256]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_736(self):
        inp = '''-100'''
        fmt = '''(Z5.2)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_737(self):
        inp = '''1000'''
        fmt = '''(Z5.2)'''
        result = [4096]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_738(self):
        inp = '''-1000'''
        fmt = '''(Z5.2)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_739(self):
        inp = '''10000'''
        fmt = '''(Z5.2)'''
        result = [65536]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_740(self):
        inp = '''-10000'''
        fmt = '''(Z5.2)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_741(self):
        inp = '''100000'''
        fmt = '''(Z5.2)'''
        result = [65536]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_742(self):
        inp = '''-100000'''
        fmt = '''(Z5.2)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_743(self):
        inp = '''123456789'''
        fmt = '''(Z5.2)'''
        result = [74565]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_744(self):
        inp = '''ff'''
        fmt = '''(Z5.2)'''
        result = [255]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_745(self):
        inp = '''F'''
        fmt = '''(Z5.2)'''
        result = [15]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_746(self):
        inp = ''' F F F'''
        fmt = '''(Z5.2)'''
        result = [255]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_747(self):
        inp = '''A a 2B'''
        fmt = '''(Z5.2)'''
        result = [2722]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_748(self):
        inp = '''A.'''
        fmt = '''(Z5.2)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_749(self):
        inp = '''0'''
        fmt = '''(Z6.2)'''
        result = [0]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_750(self):
        inp = '''-0'''
        fmt = '''(Z6.2)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_751(self):
        inp = '''1'''
        fmt = '''(Z6.2)'''
        result = [1]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_752(self):
        inp = '''-1'''
        fmt = '''(Z6.2)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_753(self):
        inp = '''3'''
        fmt = '''(Z6.2)'''
        result = [3]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_754(self):
        inp = '''-3'''
        fmt = '''(Z6.2)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_755(self):
        inp = '''10'''
        fmt = '''(Z6.2)'''
        result = [16]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_756(self):
        inp = '''-10'''
        fmt = '''(Z6.2)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_757(self):
        inp = '''100'''
        fmt = '''(Z6.2)'''
        result = [256]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_758(self):
        inp = '''-100'''
        fmt = '''(Z6.2)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_759(self):
        inp = '''1000'''
        fmt = '''(Z6.2)'''
        result = [4096]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_760(self):
        inp = '''-1000'''
        fmt = '''(Z6.2)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_761(self):
        inp = '''10000'''
        fmt = '''(Z6.2)'''
        result = [65536]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_762(self):
        inp = '''-10000'''
        fmt = '''(Z6.2)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_763(self):
        inp = '''100000'''
        fmt = '''(Z6.2)'''
        result = [1048576]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_764(self):
        inp = '''-100000'''
        fmt = '''(Z6.2)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_765(self):
        inp = '''123456789'''
        fmt = '''(Z6.2)'''
        result = [1193046]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_766(self):
        inp = '''ff'''
        fmt = '''(Z6.2)'''
        result = [255]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_767(self):
        inp = '''F'''
        fmt = '''(Z6.2)'''
        result = [15]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_768(self):
        inp = ''' F F F'''
        fmt = '''(Z6.2)'''
        result = [4095]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_769(self):
        inp = '''A a 2B'''
        fmt = '''(Z6.2)'''
        result = [43563]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_770(self):
        inp = '''A.'''
        fmt = '''(Z6.2)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_771(self):
        inp = '''0'''
        fmt = '''(Z7.2)'''
        result = [0]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_772(self):
        inp = '''-0'''
        fmt = '''(Z7.2)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_773(self):
        inp = '''1'''
        fmt = '''(Z7.2)'''
        result = [1]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_774(self):
        inp = '''-1'''
        fmt = '''(Z7.2)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_775(self):
        inp = '''3'''
        fmt = '''(Z7.2)'''
        result = [3]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_776(self):
        inp = '''-3'''
        fmt = '''(Z7.2)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_777(self):
        inp = '''10'''
        fmt = '''(Z7.2)'''
        result = [16]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_778(self):
        inp = '''-10'''
        fmt = '''(Z7.2)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_779(self):
        inp = '''100'''
        fmt = '''(Z7.2)'''
        result = [256]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_780(self):
        inp = '''-100'''
        fmt = '''(Z7.2)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_781(self):
        inp = '''1000'''
        fmt = '''(Z7.2)'''
        result = [4096]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_782(self):
        inp = '''-1000'''
        fmt = '''(Z7.2)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_783(self):
        inp = '''10000'''
        fmt = '''(Z7.2)'''
        result = [65536]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_784(self):
        inp = '''-10000'''
        fmt = '''(Z7.2)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_785(self):
        inp = '''100000'''
        fmt = '''(Z7.2)'''
        result = [1048576]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_786(self):
        inp = '''-100000'''
        fmt = '''(Z7.2)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_787(self):
        inp = '''123456789'''
        fmt = '''(Z7.2)'''
        result = [19088743]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_788(self):
        inp = '''ff'''
        fmt = '''(Z7.2)'''
        result = [255]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_789(self):
        inp = '''F'''
        fmt = '''(Z7.2)'''
        result = [15]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_790(self):
        inp = ''' F F F'''
        fmt = '''(Z7.2)'''
        result = [4095]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_791(self):
        inp = '''A a 2B'''
        fmt = '''(Z7.2)'''
        result = [43563]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_792(self):
        inp = '''A.'''
        fmt = '''(Z7.2)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_793(self):
        inp = '''0'''
        fmt = '''(Z8.2)'''
        result = [0]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_794(self):
        inp = '''-0'''
        fmt = '''(Z8.2)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_795(self):
        inp = '''1'''
        fmt = '''(Z8.2)'''
        result = [1]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_796(self):
        inp = '''-1'''
        fmt = '''(Z8.2)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_797(self):
        inp = '''3'''
        fmt = '''(Z8.2)'''
        result = [3]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_798(self):
        inp = '''-3'''
        fmt = '''(Z8.2)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_799(self):
        inp = '''10'''
        fmt = '''(Z8.2)'''
        result = [16]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_800(self):
        inp = '''-10'''
        fmt = '''(Z8.2)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_801(self):
        inp = '''100'''
        fmt = '''(Z8.2)'''
        result = [256]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_802(self):
        inp = '''-100'''
        fmt = '''(Z8.2)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_803(self):
        inp = '''1000'''
        fmt = '''(Z8.2)'''
        result = [4096]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_804(self):
        inp = '''-1000'''
        fmt = '''(Z8.2)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_805(self):
        inp = '''10000'''
        fmt = '''(Z8.2)'''
        result = [65536]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_806(self):
        inp = '''-10000'''
        fmt = '''(Z8.2)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_807(self):
        inp = '''100000'''
        fmt = '''(Z8.2)'''
        result = [1048576]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_808(self):
        inp = '''-100000'''
        fmt = '''(Z8.2)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_809(self):
        inp = '''123456789'''
        fmt = '''(Z8.2)'''
        result = [305419896]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_810(self):
        inp = '''ff'''
        fmt = '''(Z8.2)'''
        result = [255]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_811(self):
        inp = '''F'''
        fmt = '''(Z8.2)'''
        result = [15]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_812(self):
        inp = ''' F F F'''
        fmt = '''(Z8.2)'''
        result = [4095]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_813(self):
        inp = '''A a 2B'''
        fmt = '''(Z8.2)'''
        result = [43563]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_814(self):
        inp = '''A.'''
        fmt = '''(Z8.2)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_815(self):
        inp = '''0'''
        fmt = '''(Z9.2)'''
        result = [0]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_816(self):
        inp = '''-0'''
        fmt = '''(Z9.2)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_817(self):
        inp = '''1'''
        fmt = '''(Z9.2)'''
        result = [1]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_818(self):
        inp = '''-1'''
        fmt = '''(Z9.2)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_819(self):
        inp = '''3'''
        fmt = '''(Z9.2)'''
        result = [3]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_820(self):
        inp = '''-3'''
        fmt = '''(Z9.2)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_821(self):
        inp = '''10'''
        fmt = '''(Z9.2)'''
        result = [16]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_822(self):
        inp = '''-10'''
        fmt = '''(Z9.2)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_823(self):
        inp = '''100'''
        fmt = '''(Z9.2)'''
        result = [256]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_824(self):
        inp = '''-100'''
        fmt = '''(Z9.2)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_825(self):
        inp = '''1000'''
        fmt = '''(Z9.2)'''
        result = [4096]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_826(self):
        inp = '''-1000'''
        fmt = '''(Z9.2)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_827(self):
        inp = '''10000'''
        fmt = '''(Z9.2)'''
        result = [65536]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_828(self):
        inp = '''-10000'''
        fmt = '''(Z9.2)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_829(self):
        inp = '''100000'''
        fmt = '''(Z9.2)'''
        result = [1048576]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_830(self):
        inp = '''-100000'''
        fmt = '''(Z9.2)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_831(self):
        inp = '''123456789'''
        fmt = '''(Z9.2)'''
        result = [4886718345]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_832(self):
        inp = '''ff'''
        fmt = '''(Z9.2)'''
        result = [255]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_833(self):
        inp = '''F'''
        fmt = '''(Z9.2)'''
        result = [15]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_834(self):
        inp = ''' F F F'''
        fmt = '''(Z9.2)'''
        result = [4095]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_835(self):
        inp = '''A a 2B'''
        fmt = '''(Z9.2)'''
        result = [43563]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_836(self):
        inp = '''A.'''
        fmt = '''(Z9.2)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_837(self):
        inp = '''0'''
        fmt = '''(Z10.2)'''
        result = [0]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_838(self):
        inp = '''-0'''
        fmt = '''(Z10.2)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_839(self):
        inp = '''1'''
        fmt = '''(Z10.2)'''
        result = [1]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_840(self):
        inp = '''-1'''
        fmt = '''(Z10.2)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_841(self):
        inp = '''3'''
        fmt = '''(Z10.2)'''
        result = [3]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_842(self):
        inp = '''-3'''
        fmt = '''(Z10.2)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_843(self):
        inp = '''10'''
        fmt = '''(Z10.2)'''
        result = [16]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_844(self):
        inp = '''-10'''
        fmt = '''(Z10.2)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_845(self):
        inp = '''100'''
        fmt = '''(Z10.2)'''
        result = [256]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_846(self):
        inp = '''-100'''
        fmt = '''(Z10.2)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_847(self):
        inp = '''1000'''
        fmt = '''(Z10.2)'''
        result = [4096]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_848(self):
        inp = '''-1000'''
        fmt = '''(Z10.2)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_849(self):
        inp = '''10000'''
        fmt = '''(Z10.2)'''
        result = [65536]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_850(self):
        inp = '''-10000'''
        fmt = '''(Z10.2)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_851(self):
        inp = '''100000'''
        fmt = '''(Z10.2)'''
        result = [1048576]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_852(self):
        inp = '''-100000'''
        fmt = '''(Z10.2)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_853(self):
        inp = '''123456789'''
        fmt = '''(Z10.2)'''
        result = [4886718345]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_854(self):
        inp = '''ff'''
        fmt = '''(Z10.2)'''
        result = [255]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_855(self):
        inp = '''F'''
        fmt = '''(Z10.2)'''
        result = [15]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_856(self):
        inp = ''' F F F'''
        fmt = '''(Z10.2)'''
        result = [4095]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_857(self):
        inp = '''A a 2B'''
        fmt = '''(Z10.2)'''
        result = [43563]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_858(self):
        inp = '''A.'''
        fmt = '''(Z10.2)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_859(self):
        inp = '''0'''
        fmt = '''(Z3.3)'''
        result = [0]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_860(self):
        inp = '''-0'''
        fmt = '''(Z3.3)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_861(self):
        inp = '''1'''
        fmt = '''(Z3.3)'''
        result = [1]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_862(self):
        inp = '''-1'''
        fmt = '''(Z3.3)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_863(self):
        inp = '''3'''
        fmt = '''(Z3.3)'''
        result = [3]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_864(self):
        inp = '''-3'''
        fmt = '''(Z3.3)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_865(self):
        inp = '''10'''
        fmt = '''(Z3.3)'''
        result = [16]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_866(self):
        inp = '''-10'''
        fmt = '''(Z3.3)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_867(self):
        inp = '''100'''
        fmt = '''(Z3.3)'''
        result = [256]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_868(self):
        inp = '''-100'''
        fmt = '''(Z3.3)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_869(self):
        inp = '''1000'''
        fmt = '''(Z3.3)'''
        result = [256]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_870(self):
        inp = '''-1000'''
        fmt = '''(Z3.3)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_871(self):
        inp = '''10000'''
        fmt = '''(Z3.3)'''
        result = [256]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_872(self):
        inp = '''-10000'''
        fmt = '''(Z3.3)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_873(self):
        inp = '''100000'''
        fmt = '''(Z3.3)'''
        result = [256]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_874(self):
        inp = '''-100000'''
        fmt = '''(Z3.3)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_875(self):
        inp = '''123456789'''
        fmt = '''(Z3.3)'''
        result = [291]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_876(self):
        inp = '''ff'''
        fmt = '''(Z3.3)'''
        result = [255]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_877(self):
        inp = '''F'''
        fmt = '''(Z3.3)'''
        result = [15]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_878(self):
        inp = ''' F F F'''
        fmt = '''(Z3.3)'''
        result = [15]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_879(self):
        inp = '''A a 2B'''
        fmt = '''(Z3.3)'''
        result = [170]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_880(self):
        inp = '''A.'''
        fmt = '''(Z3.3)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_881(self):
        inp = '''0'''
        fmt = '''(Z4.3)'''
        result = [0]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_882(self):
        inp = '''-0'''
        fmt = '''(Z4.3)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_883(self):
        inp = '''1'''
        fmt = '''(Z4.3)'''
        result = [1]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_884(self):
        inp = '''-1'''
        fmt = '''(Z4.3)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_885(self):
        inp = '''3'''
        fmt = '''(Z4.3)'''
        result = [3]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_886(self):
        inp = '''-3'''
        fmt = '''(Z4.3)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_887(self):
        inp = '''10'''
        fmt = '''(Z4.3)'''
        result = [16]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_888(self):
        inp = '''-10'''
        fmt = '''(Z4.3)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_889(self):
        inp = '''100'''
        fmt = '''(Z4.3)'''
        result = [256]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_890(self):
        inp = '''-100'''
        fmt = '''(Z4.3)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_891(self):
        inp = '''1000'''
        fmt = '''(Z4.3)'''
        result = [4096]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_892(self):
        inp = '''-1000'''
        fmt = '''(Z4.3)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_893(self):
        inp = '''10000'''
        fmt = '''(Z4.3)'''
        result = [4096]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_894(self):
        inp = '''-10000'''
        fmt = '''(Z4.3)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_895(self):
        inp = '''100000'''
        fmt = '''(Z4.3)'''
        result = [4096]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_896(self):
        inp = '''-100000'''
        fmt = '''(Z4.3)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_897(self):
        inp = '''123456789'''
        fmt = '''(Z4.3)'''
        result = [4660]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_898(self):
        inp = '''ff'''
        fmt = '''(Z4.3)'''
        result = [255]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_899(self):
        inp = '''F'''
        fmt = '''(Z4.3)'''
        result = [15]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_900(self):
        inp = ''' F F F'''
        fmt = '''(Z4.3)'''
        result = [255]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_901(self):
        inp = '''A a 2B'''
        fmt = '''(Z4.3)'''
        result = [170]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_902(self):
        inp = '''A.'''
        fmt = '''(Z4.3)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_903(self):
        inp = '''0'''
        fmt = '''(Z5.3)'''
        result = [0]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_904(self):
        inp = '''-0'''
        fmt = '''(Z5.3)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_905(self):
        inp = '''1'''
        fmt = '''(Z5.3)'''
        result = [1]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_906(self):
        inp = '''-1'''
        fmt = '''(Z5.3)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_907(self):
        inp = '''3'''
        fmt = '''(Z5.3)'''
        result = [3]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_908(self):
        inp = '''-3'''
        fmt = '''(Z5.3)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_909(self):
        inp = '''10'''
        fmt = '''(Z5.3)'''
        result = [16]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_910(self):
        inp = '''-10'''
        fmt = '''(Z5.3)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_911(self):
        inp = '''100'''
        fmt = '''(Z5.3)'''
        result = [256]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_912(self):
        inp = '''-100'''
        fmt = '''(Z5.3)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_913(self):
        inp = '''1000'''
        fmt = '''(Z5.3)'''
        result = [4096]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_914(self):
        inp = '''-1000'''
        fmt = '''(Z5.3)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_915(self):
        inp = '''10000'''
        fmt = '''(Z5.3)'''
        result = [65536]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_916(self):
        inp = '''-10000'''
        fmt = '''(Z5.3)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_917(self):
        inp = '''100000'''
        fmt = '''(Z5.3)'''
        result = [65536]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_918(self):
        inp = '''-100000'''
        fmt = '''(Z5.3)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_919(self):
        inp = '''123456789'''
        fmt = '''(Z5.3)'''
        result = [74565]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_920(self):
        inp = '''ff'''
        fmt = '''(Z5.3)'''
        result = [255]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_921(self):
        inp = '''F'''
        fmt = '''(Z5.3)'''
        result = [15]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_922(self):
        inp = ''' F F F'''
        fmt = '''(Z5.3)'''
        result = [255]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_923(self):
        inp = '''A a 2B'''
        fmt = '''(Z5.3)'''
        result = [2722]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_924(self):
        inp = '''A.'''
        fmt = '''(Z5.3)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_925(self):
        inp = '''0'''
        fmt = '''(Z6.3)'''
        result = [0]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_926(self):
        inp = '''-0'''
        fmt = '''(Z6.3)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_927(self):
        inp = '''1'''
        fmt = '''(Z6.3)'''
        result = [1]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_928(self):
        inp = '''-1'''
        fmt = '''(Z6.3)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_929(self):
        inp = '''3'''
        fmt = '''(Z6.3)'''
        result = [3]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_930(self):
        inp = '''-3'''
        fmt = '''(Z6.3)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_931(self):
        inp = '''10'''
        fmt = '''(Z6.3)'''
        result = [16]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_932(self):
        inp = '''-10'''
        fmt = '''(Z6.3)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_933(self):
        inp = '''100'''
        fmt = '''(Z6.3)'''
        result = [256]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_934(self):
        inp = '''-100'''
        fmt = '''(Z6.3)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_935(self):
        inp = '''1000'''
        fmt = '''(Z6.3)'''
        result = [4096]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_936(self):
        inp = '''-1000'''
        fmt = '''(Z6.3)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_937(self):
        inp = '''10000'''
        fmt = '''(Z6.3)'''
        result = [65536]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_938(self):
        inp = '''-10000'''
        fmt = '''(Z6.3)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_939(self):
        inp = '''100000'''
        fmt = '''(Z6.3)'''
        result = [1048576]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_940(self):
        inp = '''-100000'''
        fmt = '''(Z6.3)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_941(self):
        inp = '''123456789'''
        fmt = '''(Z6.3)'''
        result = [1193046]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_942(self):
        inp = '''ff'''
        fmt = '''(Z6.3)'''
        result = [255]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_943(self):
        inp = '''F'''
        fmt = '''(Z6.3)'''
        result = [15]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_944(self):
        inp = ''' F F F'''
        fmt = '''(Z6.3)'''
        result = [4095]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_945(self):
        inp = '''A a 2B'''
        fmt = '''(Z6.3)'''
        result = [43563]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_946(self):
        inp = '''A.'''
        fmt = '''(Z6.3)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_947(self):
        inp = '''0'''
        fmt = '''(Z7.3)'''
        result = [0]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_948(self):
        inp = '''-0'''
        fmt = '''(Z7.3)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_949(self):
        inp = '''1'''
        fmt = '''(Z7.3)'''
        result = [1]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_950(self):
        inp = '''-1'''
        fmt = '''(Z7.3)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_951(self):
        inp = '''3'''
        fmt = '''(Z7.3)'''
        result = [3]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_952(self):
        inp = '''-3'''
        fmt = '''(Z7.3)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_953(self):
        inp = '''10'''
        fmt = '''(Z7.3)'''
        result = [16]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_954(self):
        inp = '''-10'''
        fmt = '''(Z7.3)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_955(self):
        inp = '''100'''
        fmt = '''(Z7.3)'''
        result = [256]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_956(self):
        inp = '''-100'''
        fmt = '''(Z7.3)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_957(self):
        inp = '''1000'''
        fmt = '''(Z7.3)'''
        result = [4096]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_958(self):
        inp = '''-1000'''
        fmt = '''(Z7.3)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_959(self):
        inp = '''10000'''
        fmt = '''(Z7.3)'''
        result = [65536]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_960(self):
        inp = '''-10000'''
        fmt = '''(Z7.3)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_961(self):
        inp = '''100000'''
        fmt = '''(Z7.3)'''
        result = [1048576]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_962(self):
        inp = '''-100000'''
        fmt = '''(Z7.3)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_963(self):
        inp = '''123456789'''
        fmt = '''(Z7.3)'''
        result = [19088743]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_964(self):
        inp = '''ff'''
        fmt = '''(Z7.3)'''
        result = [255]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_965(self):
        inp = '''F'''
        fmt = '''(Z7.3)'''
        result = [15]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_966(self):
        inp = ''' F F F'''
        fmt = '''(Z7.3)'''
        result = [4095]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_967(self):
        inp = '''A a 2B'''
        fmt = '''(Z7.3)'''
        result = [43563]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_968(self):
        inp = '''A.'''
        fmt = '''(Z7.3)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_969(self):
        inp = '''0'''
        fmt = '''(Z8.3)'''
        result = [0]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_970(self):
        inp = '''-0'''
        fmt = '''(Z8.3)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_971(self):
        inp = '''1'''
        fmt = '''(Z8.3)'''
        result = [1]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_972(self):
        inp = '''-1'''
        fmt = '''(Z8.3)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_973(self):
        inp = '''3'''
        fmt = '''(Z8.3)'''
        result = [3]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_974(self):
        inp = '''-3'''
        fmt = '''(Z8.3)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_975(self):
        inp = '''10'''
        fmt = '''(Z8.3)'''
        result = [16]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_976(self):
        inp = '''-10'''
        fmt = '''(Z8.3)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_977(self):
        inp = '''100'''
        fmt = '''(Z8.3)'''
        result = [256]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_978(self):
        inp = '''-100'''
        fmt = '''(Z8.3)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_979(self):
        inp = '''1000'''
        fmt = '''(Z8.3)'''
        result = [4096]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_980(self):
        inp = '''-1000'''
        fmt = '''(Z8.3)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_981(self):
        inp = '''10000'''
        fmt = '''(Z8.3)'''
        result = [65536]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_982(self):
        inp = '''-10000'''
        fmt = '''(Z8.3)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_983(self):
        inp = '''100000'''
        fmt = '''(Z8.3)'''
        result = [1048576]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_984(self):
        inp = '''-100000'''
        fmt = '''(Z8.3)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_985(self):
        inp = '''123456789'''
        fmt = '''(Z8.3)'''
        result = [305419896]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_986(self):
        inp = '''ff'''
        fmt = '''(Z8.3)'''
        result = [255]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_987(self):
        inp = '''F'''
        fmt = '''(Z8.3)'''
        result = [15]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_988(self):
        inp = ''' F F F'''
        fmt = '''(Z8.3)'''
        result = [4095]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_989(self):
        inp = '''A a 2B'''
        fmt = '''(Z8.3)'''
        result = [43563]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_990(self):
        inp = '''A.'''
        fmt = '''(Z8.3)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_991(self):
        inp = '''0'''
        fmt = '''(Z9.3)'''
        result = [0]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_992(self):
        inp = '''-0'''
        fmt = '''(Z9.3)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_993(self):
        inp = '''1'''
        fmt = '''(Z9.3)'''
        result = [1]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_994(self):
        inp = '''-1'''
        fmt = '''(Z9.3)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_995(self):
        inp = '''3'''
        fmt = '''(Z9.3)'''
        result = [3]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_996(self):
        inp = '''-3'''
        fmt = '''(Z9.3)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_997(self):
        inp = '''10'''
        fmt = '''(Z9.3)'''
        result = [16]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_998(self):
        inp = '''-10'''
        fmt = '''(Z9.3)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='Z')
    def test_z_ed_input_999(self):
        inp = '''100'''
        fmt = '''(Z9.3)'''
        result = [256]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))


if __name__ == '__main__':
    unittest.main()