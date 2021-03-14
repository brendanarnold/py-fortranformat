
import sys
import os
import unittest
from nose.plugins.attrib import attr

# To change this, re-run 'build-unittests.py'

from fortranformat._input import input as _input
from fortranformat._lexer import lexer as _lexer
from fortranformat._parser import parser as _parser
import unittest

class OEditDescriptorBatch2TestCase(unittest.TestCase):

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_1(self):
        inp = '''1000'''
        fmt = '''(1O3)'''
        result = [64]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_2(self):
        inp = '''-1000'''
        fmt = '''(1O3)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_3(self):
        inp = '''10000'''
        fmt = '''(1O3)'''
        result = [64]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_4(self):
        inp = '''-10000'''
        fmt = '''(1O3)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_5(self):
        inp = '''100000'''
        fmt = '''(1O3)'''
        result = [64]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_6(self):
        inp = '''-100000'''
        fmt = '''(1O3)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_7(self):
        inp = '''12345678'''
        fmt = '''(1O3)'''
        result = [83]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_8(self):
        inp = '''123456789'''
        fmt = '''(1O3)'''
        result = [83]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_9(self):
        inp = '''0'''
        fmt = '''(1O5)'''
        result = [0]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_10(self):
        inp = '''-0'''
        fmt = '''(1O5)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_11(self):
        inp = '''1'''
        fmt = '''(1O5)'''
        result = [1]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_12(self):
        inp = '''-1'''
        fmt = '''(1O5)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_13(self):
        inp = '''3'''
        fmt = '''(1O5)'''
        result = [3]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_14(self):
        inp = '''-3'''
        fmt = '''(1O5)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_15(self):
        inp = '''10'''
        fmt = '''(1O5)'''
        result = [8]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_16(self):
        inp = '''-10'''
        fmt = '''(1O5)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_17(self):
        inp = '''100'''
        fmt = '''(1O5)'''
        result = [64]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_18(self):
        inp = '''-100'''
        fmt = '''(1O5)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_19(self):
        inp = '''1000'''
        fmt = '''(1O5)'''
        result = [512]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_20(self):
        inp = '''-1000'''
        fmt = '''(1O5)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_21(self):
        inp = '''10000'''
        fmt = '''(1O5)'''
        result = [4096]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_22(self):
        inp = '''-10000'''
        fmt = '''(1O5)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_23(self):
        inp = '''100000'''
        fmt = '''(1O5)'''
        result = [4096]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_24(self):
        inp = '''-100000'''
        fmt = '''(1O5)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_25(self):
        inp = '''12345678'''
        fmt = '''(1O5)'''
        result = [5349]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_26(self):
        inp = '''123456789'''
        fmt = '''(1O5)'''
        result = [5349]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_27(self):
        inp = '''0'''
        fmt = '''(1O10)'''
        result = [0]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_28(self):
        inp = '''-0'''
        fmt = '''(1O10)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_29(self):
        inp = '''1'''
        fmt = '''(1O10)'''
        result = [1]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_30(self):
        inp = '''-1'''
        fmt = '''(1O10)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_31(self):
        inp = '''3'''
        fmt = '''(1O10)'''
        result = [3]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_32(self):
        inp = '''-3'''
        fmt = '''(1O10)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_33(self):
        inp = '''10'''
        fmt = '''(1O10)'''
        result = [8]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_34(self):
        inp = '''-10'''
        fmt = '''(1O10)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_35(self):
        inp = '''100'''
        fmt = '''(1O10)'''
        result = [64]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_36(self):
        inp = '''-100'''
        fmt = '''(1O10)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_37(self):
        inp = '''1000'''
        fmt = '''(1O10)'''
        result = [512]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_38(self):
        inp = '''-1000'''
        fmt = '''(1O10)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_39(self):
        inp = '''10000'''
        fmt = '''(1O10)'''
        result = [4096]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_40(self):
        inp = '''-10000'''
        fmt = '''(1O10)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_41(self):
        inp = '''100000'''
        fmt = '''(1O10)'''
        result = [32768]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_42(self):
        inp = '''-100000'''
        fmt = '''(1O10)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_43(self):
        inp = '''12345678'''
        fmt = '''(1O10)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_44(self):
        inp = '''123456789'''
        fmt = '''(1O10)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_45(self):
        inp = '''0'''
        fmt = '''(1O1.0)'''
        result = [0]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_46(self):
        inp = '''-0'''
        fmt = '''(1O1.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_47(self):
        inp = '''1'''
        fmt = '''(1O1.0)'''
        result = [1]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_48(self):
        inp = '''-1'''
        fmt = '''(1O1.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_49(self):
        inp = '''3'''
        fmt = '''(1O1.0)'''
        result = [3]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_50(self):
        inp = '''-3'''
        fmt = '''(1O1.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_51(self):
        inp = '''10'''
        fmt = '''(1O1.0)'''
        result = [1]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_52(self):
        inp = '''-10'''
        fmt = '''(1O1.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_53(self):
        inp = '''100'''
        fmt = '''(1O1.0)'''
        result = [1]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_54(self):
        inp = '''-100'''
        fmt = '''(1O1.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_55(self):
        inp = '''1000'''
        fmt = '''(1O1.0)'''
        result = [1]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_56(self):
        inp = '''-1000'''
        fmt = '''(1O1.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_57(self):
        inp = '''10000'''
        fmt = '''(1O1.0)'''
        result = [1]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_58(self):
        inp = '''-10000'''
        fmt = '''(1O1.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_59(self):
        inp = '''100000'''
        fmt = '''(1O1.0)'''
        result = [1]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_60(self):
        inp = '''-100000'''
        fmt = '''(1O1.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_61(self):
        inp = '''12345678'''
        fmt = '''(1O1.0)'''
        result = [1]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_62(self):
        inp = '''123456789'''
        fmt = '''(1O1.0)'''
        result = [1]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_63(self):
        inp = '''0'''
        fmt = '''(1O2.0)'''
        result = [0]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_64(self):
        inp = '''-0'''
        fmt = '''(1O2.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_65(self):
        inp = '''1'''
        fmt = '''(1O2.0)'''
        result = [1]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_66(self):
        inp = '''-1'''
        fmt = '''(1O2.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_67(self):
        inp = '''3'''
        fmt = '''(1O2.0)'''
        result = [3]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_68(self):
        inp = '''-3'''
        fmt = '''(1O2.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_69(self):
        inp = '''10'''
        fmt = '''(1O2.0)'''
        result = [8]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_70(self):
        inp = '''-10'''
        fmt = '''(1O2.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_71(self):
        inp = '''100'''
        fmt = '''(1O2.0)'''
        result = [8]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_72(self):
        inp = '''-100'''
        fmt = '''(1O2.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_73(self):
        inp = '''1000'''
        fmt = '''(1O2.0)'''
        result = [8]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_74(self):
        inp = '''-1000'''
        fmt = '''(1O2.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_75(self):
        inp = '''10000'''
        fmt = '''(1O2.0)'''
        result = [8]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_76(self):
        inp = '''-10000'''
        fmt = '''(1O2.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_77(self):
        inp = '''100000'''
        fmt = '''(1O2.0)'''
        result = [8]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_78(self):
        inp = '''-100000'''
        fmt = '''(1O2.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_79(self):
        inp = '''12345678'''
        fmt = '''(1O2.0)'''
        result = [10]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_80(self):
        inp = '''123456789'''
        fmt = '''(1O2.0)'''
        result = [10]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_81(self):
        inp = '''0'''
        fmt = '''(1O3.0)'''
        result = [0]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_82(self):
        inp = '''-0'''
        fmt = '''(1O3.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_83(self):
        inp = '''1'''
        fmt = '''(1O3.0)'''
        result = [1]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_84(self):
        inp = '''-1'''
        fmt = '''(1O3.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_85(self):
        inp = '''3'''
        fmt = '''(1O3.0)'''
        result = [3]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_86(self):
        inp = '''-3'''
        fmt = '''(1O3.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_87(self):
        inp = '''10'''
        fmt = '''(1O3.0)'''
        result = [8]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_88(self):
        inp = '''-10'''
        fmt = '''(1O3.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_89(self):
        inp = '''100'''
        fmt = '''(1O3.0)'''
        result = [64]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_90(self):
        inp = '''-100'''
        fmt = '''(1O3.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_91(self):
        inp = '''1000'''
        fmt = '''(1O3.0)'''
        result = [64]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_92(self):
        inp = '''-1000'''
        fmt = '''(1O3.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_93(self):
        inp = '''10000'''
        fmt = '''(1O3.0)'''
        result = [64]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_94(self):
        inp = '''-10000'''
        fmt = '''(1O3.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_95(self):
        inp = '''100000'''
        fmt = '''(1O3.0)'''
        result = [64]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_96(self):
        inp = '''-100000'''
        fmt = '''(1O3.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_97(self):
        inp = '''12345678'''
        fmt = '''(1O3.0)'''
        result = [83]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_98(self):
        inp = '''123456789'''
        fmt = '''(1O3.0)'''
        result = [83]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_99(self):
        inp = '''0'''
        fmt = '''(1O5.0)'''
        result = [0]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_100(self):
        inp = '''-0'''
        fmt = '''(1O5.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_101(self):
        inp = '''1'''
        fmt = '''(1O5.0)'''
        result = [1]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_102(self):
        inp = '''-1'''
        fmt = '''(1O5.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_103(self):
        inp = '''3'''
        fmt = '''(1O5.0)'''
        result = [3]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_104(self):
        inp = '''-3'''
        fmt = '''(1O5.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_105(self):
        inp = '''10'''
        fmt = '''(1O5.0)'''
        result = [8]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_106(self):
        inp = '''-10'''
        fmt = '''(1O5.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_107(self):
        inp = '''100'''
        fmt = '''(1O5.0)'''
        result = [64]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_108(self):
        inp = '''-100'''
        fmt = '''(1O5.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_109(self):
        inp = '''1000'''
        fmt = '''(1O5.0)'''
        result = [512]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_110(self):
        inp = '''-1000'''
        fmt = '''(1O5.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_111(self):
        inp = '''10000'''
        fmt = '''(1O5.0)'''
        result = [4096]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_112(self):
        inp = '''-10000'''
        fmt = '''(1O5.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_113(self):
        inp = '''100000'''
        fmt = '''(1O5.0)'''
        result = [4096]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_114(self):
        inp = '''-100000'''
        fmt = '''(1O5.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_115(self):
        inp = '''12345678'''
        fmt = '''(1O5.0)'''
        result = [5349]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_116(self):
        inp = '''123456789'''
        fmt = '''(1O5.0)'''
        result = [5349]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_117(self):
        inp = '''0'''
        fmt = '''(1O10.0)'''
        result = [0]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_118(self):
        inp = '''-0'''
        fmt = '''(1O10.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_119(self):
        inp = '''1'''
        fmt = '''(1O10.0)'''
        result = [1]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_120(self):
        inp = '''-1'''
        fmt = '''(1O10.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_121(self):
        inp = '''3'''
        fmt = '''(1O10.0)'''
        result = [3]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_122(self):
        inp = '''-3'''
        fmt = '''(1O10.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_123(self):
        inp = '''10'''
        fmt = '''(1O10.0)'''
        result = [8]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_124(self):
        inp = '''-10'''
        fmt = '''(1O10.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_125(self):
        inp = '''100'''
        fmt = '''(1O10.0)'''
        result = [64]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_126(self):
        inp = '''-100'''
        fmt = '''(1O10.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_127(self):
        inp = '''1000'''
        fmt = '''(1O10.0)'''
        result = [512]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_128(self):
        inp = '''-1000'''
        fmt = '''(1O10.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_129(self):
        inp = '''10000'''
        fmt = '''(1O10.0)'''
        result = [4096]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_130(self):
        inp = '''-10000'''
        fmt = '''(1O10.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_131(self):
        inp = '''100000'''
        fmt = '''(1O10.0)'''
        result = [32768]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_132(self):
        inp = '''-100000'''
        fmt = '''(1O10.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_133(self):
        inp = '''12345678'''
        fmt = '''(1O10.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_134(self):
        inp = '''123456789'''
        fmt = '''(1O10.0)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_135(self):
        inp = '''0'''
        fmt = '''(1O3.3)'''
        result = [0]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_136(self):
        inp = '''-0'''
        fmt = '''(1O3.3)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_137(self):
        inp = '''1'''
        fmt = '''(1O3.3)'''
        result = [1]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_138(self):
        inp = '''-1'''
        fmt = '''(1O3.3)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_139(self):
        inp = '''3'''
        fmt = '''(1O3.3)'''
        result = [3]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_140(self):
        inp = '''-3'''
        fmt = '''(1O3.3)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_141(self):
        inp = '''10'''
        fmt = '''(1O3.3)'''
        result = [8]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_142(self):
        inp = '''-10'''
        fmt = '''(1O3.3)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_143(self):
        inp = '''100'''
        fmt = '''(1O3.3)'''
        result = [64]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_144(self):
        inp = '''-100'''
        fmt = '''(1O3.3)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_145(self):
        inp = '''1000'''
        fmt = '''(1O3.3)'''
        result = [64]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_146(self):
        inp = '''-1000'''
        fmt = '''(1O3.3)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_147(self):
        inp = '''10000'''
        fmt = '''(1O3.3)'''
        result = [64]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_148(self):
        inp = '''-10000'''
        fmt = '''(1O3.3)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_149(self):
        inp = '''100000'''
        fmt = '''(1O3.3)'''
        result = [64]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_150(self):
        inp = '''-100000'''
        fmt = '''(1O3.3)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_151(self):
        inp = '''12345678'''
        fmt = '''(1O3.3)'''
        result = [83]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_152(self):
        inp = '''123456789'''
        fmt = '''(1O3.3)'''
        result = [83]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_153(self):
        inp = '''0'''
        fmt = '''(1O5.3)'''
        result = [0]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_154(self):
        inp = '''-0'''
        fmt = '''(1O5.3)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_155(self):
        inp = '''1'''
        fmt = '''(1O5.3)'''
        result = [1]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_156(self):
        inp = '''-1'''
        fmt = '''(1O5.3)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_157(self):
        inp = '''3'''
        fmt = '''(1O5.3)'''
        result = [3]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_158(self):
        inp = '''-3'''
        fmt = '''(1O5.3)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_159(self):
        inp = '''10'''
        fmt = '''(1O5.3)'''
        result = [8]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_160(self):
        inp = '''-10'''
        fmt = '''(1O5.3)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_161(self):
        inp = '''100'''
        fmt = '''(1O5.3)'''
        result = [64]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_162(self):
        inp = '''-100'''
        fmt = '''(1O5.3)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_163(self):
        inp = '''1000'''
        fmt = '''(1O5.3)'''
        result = [512]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_164(self):
        inp = '''-1000'''
        fmt = '''(1O5.3)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_165(self):
        inp = '''10000'''
        fmt = '''(1O5.3)'''
        result = [4096]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_166(self):
        inp = '''-10000'''
        fmt = '''(1O5.3)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_167(self):
        inp = '''100000'''
        fmt = '''(1O5.3)'''
        result = [4096]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_168(self):
        inp = '''-100000'''
        fmt = '''(1O5.3)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_169(self):
        inp = '''12345678'''
        fmt = '''(1O5.3)'''
        result = [5349]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_170(self):
        inp = '''123456789'''
        fmt = '''(1O5.3)'''
        result = [5349]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_171(self):
        inp = '''0'''
        fmt = '''(1O10.3)'''
        result = [0]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_172(self):
        inp = '''-0'''
        fmt = '''(1O10.3)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_173(self):
        inp = '''1'''
        fmt = '''(1O10.3)'''
        result = [1]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_174(self):
        inp = '''-1'''
        fmt = '''(1O10.3)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_175(self):
        inp = '''3'''
        fmt = '''(1O10.3)'''
        result = [3]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_176(self):
        inp = '''-3'''
        fmt = '''(1O10.3)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_177(self):
        inp = '''10'''
        fmt = '''(1O10.3)'''
        result = [8]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_178(self):
        inp = '''-10'''
        fmt = '''(1O10.3)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_179(self):
        inp = '''100'''
        fmt = '''(1O10.3)'''
        result = [64]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_180(self):
        inp = '''-100'''
        fmt = '''(1O10.3)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_181(self):
        inp = '''1000'''
        fmt = '''(1O10.3)'''
        result = [512]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_182(self):
        inp = '''-1000'''
        fmt = '''(1O10.3)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_183(self):
        inp = '''10000'''
        fmt = '''(1O10.3)'''
        result = [4096]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_184(self):
        inp = '''-10000'''
        fmt = '''(1O10.3)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_185(self):
        inp = '''100000'''
        fmt = '''(1O10.3)'''
        result = [32768]
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertEqual(result, _input(eds, rev_eds, inp))

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_186(self):
        inp = '''-100000'''
        fmt = '''(1O10.3)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)

    @attr(platform='9-1_linux_intel')
    @attr('input')
    @attr(ed='O')
    def test_o_ed_input_187(self):
        inp = '''12345678'''
        fmt = '''(1O10.3)'''
        result = ['''ERR''']
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inp)


if __name__ == '__main__':
    unittest.main()