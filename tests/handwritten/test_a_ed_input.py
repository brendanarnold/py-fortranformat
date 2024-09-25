import unittest

from fortranformat._input import input as _input
from fortranformat._lexer import lexer as _lexer
from fortranformat._parser import parser as _parser


class AEditDescriptorTests(unittest.TestCase):

    # Test simple A use

    def test_1(self):
        inpt = '1234567890'
        fmt = '(A)'
        eds, rev_eds = _parser(_lexer(fmt))
        result = ['1234567890']
        self.assertEqual(result, _input(eds, rev_eds, inpt))

    def test_2(self):
        # Should not escape doubled quotes like Fortran
        inpt = "''"
        fmt = '(A)'
        eds, rev_eds = _parser(_lexer(fmt))
        result = ["''"]
        self.assertEqual(result, _input(eds, rev_eds, inpt))

    def test_3(self):
        inpt = "'This is what I mean' - said Alice."
        fmt = '(A)'
        eds, rev_eds = _parser(_lexer(fmt))
        result = ["'This is what I mean' - said Alice."]
        self.assertEqual(result, _input(eds, rev_eds, inpt))

    def test_4(self):
        inpt = '"I didn\'t do that!" said Alice'
        fmt = '(A)'
        eds, rev_eds = _parser(_lexer(fmt))
        result = ['"I didn\'t do that!" said Alice']
        self.assertEqual(result, _input(eds, rev_eds, inpt))

    def test_5(self):
        inpt = '""'
        fmt = '(A)'
        eds, rev_eds = _parser(_lexer(fmt))
        result = ['""']
        self.assertEqual(result, _input(eds, rev_eds, inpt))

    def test_6(self):
        inpt = ''
        fmt = '(A)'
        eds, rev_eds = _parser(_lexer(fmt))
        result = ['']
        self.assertEqual(result, _input(eds, rev_eds, inpt))

    def test_7(self):
        # Should pad string with blanks at end
        inpt = '1234567890'
        fmt = '(A15)'
        eds, rev_eds = _parser(_lexer(fmt))
        result = ['1234567890     ']
        self.assertEqual(result, _input(eds, rev_eds, inpt))

    # Test with TR

    def test_tr_1(self):
        inpt = '1234567890'
        fmt = '(TR1, A)'
        eds, rev_eds = _parser(_lexer(fmt))
        result = ['234567890']
        self.assertEqual(result, _input(eds, rev_eds, inpt))

    def test_tr_2(self):
        inpt = '1234567890'
        fmt = '(TR10, A)'
        eds, rev_eds = _parser(_lexer(fmt))
        result = ['']
        self.assertEqual(result, _input(eds, rev_eds, inpt))

    def test_tr_3(self):
        inpt = '1234567890'
        fmt = '(TR11, A)'
        eds, rev_eds = _parser(_lexer(fmt))
        result = ['']
        self.assertEqual(result, _input(eds, rev_eds, inpt))

    def test_tr_4(self):
        inpt = '1234567890'
        fmt = '(TR4, A)'
        eds, rev_eds = _parser(_lexer(fmt))
        result = ['567890']
        self.assertEqual(result, _input(eds, rev_eds, inpt))

    def test_tr_5(self):
        inpt = '1234567890'
        fmt = '(TR1, A1)'
        eds, rev_eds = _parser(_lexer(fmt))
        result = ['2']
        self.assertEqual(result, _input(eds, rev_eds, inpt))

    def test_tr_6(self):
        inpt = '1234567890'
        fmt = '(TR11, A1)'
        eds, rev_eds = _parser(_lexer(fmt))
        # Make the call that width will be respected always
        result = [' ']
        self.assertEqual(result, _input(eds, rev_eds, inpt))

    # Test with X (should be same as TR)

    def test_x_1(self):
        inpt = '1234567890'
        fmt = '(1X, A)'
        eds, rev_eds = _parser(_lexer(fmt))
        result = ['234567890']
        self.assertEqual(result, _input(eds, rev_eds, inpt))

    def test_x_2(self):
        inpt = '1234567890'
        fmt = '(10X, A)'
        eds, rev_eds = _parser(_lexer(fmt))
        result = ['']
        self.assertEqual(result, _input(eds, rev_eds, inpt))

    def test_x_3(self):
        inpt = '1234567890'
        fmt = '(11X, A)'
        eds, rev_eds = _parser(_lexer(fmt))
        result = ['']
        self.assertEqual(result, _input(eds, rev_eds, inpt))

    def test_x_4(self):
        inpt = '1234567890'
        fmt = '(4X, A)'
        eds, rev_eds = _parser(_lexer(fmt))
        result = ['567890']
        self.assertEqual(result, _input(eds, rev_eds, inpt))

    def test_x_5(self):
        inpt = '1234567890'
        fmt = '(1X, A1)'
        eds, rev_eds = _parser(_lexer(fmt))
        result = ['2']
        self.assertEqual(result, _input(eds, rev_eds, inpt))

    def test_x_6(self):
        inpt = '1234567890'
        fmt = '(11X, A1)'
        eds, rev_eds = _parser(_lexer(fmt))
        # Make the call that width will be respected always
        result = [' ']
        self.assertEqual(result, _input(eds, rev_eds, inpt))

    # Test with TL

    def test_tl_1(self):
        inpt = '1234567890'
        fmt = '(TL1, A)'
        eds, rev_eds = _parser(_lexer(fmt))
        result = ['1234567890']
        self.assertEqual(result, _input(eds, rev_eds, inpt))

    def test_tl_2(self):
        inpt = '1234567890'
        fmt = '(TL10, A)'
        eds, rev_eds = _parser(_lexer(fmt))
        result = ['1234567890']
        self.assertEqual(result, _input(eds, rev_eds, inpt))

    def test_tl_5(self):
        inpt = '1234567890'
        fmt = '(TL1, A1)'
        eds, rev_eds = _parser(_lexer(fmt))
        result = ['1']
        self.assertEqual(result, _input(eds, rev_eds, inpt))

    # Test combined TL and TR

    def test_tl_tr_1(self):
        inpt = '1234567890'
        fmt = '(TL5, TR5, A1)'
        eds, rev_eds = _parser(_lexer(fmt))
        result = ['6']
        self.assertEqual(result, _input(eds, rev_eds, inpt))

    def test_tl_tr_2(self):
        inpt = '1234567890'
        fmt = '(TL5, TR1, A1)'
        eds, rev_eds = _parser(_lexer(fmt))
        result = ['2']
        self.assertEqual(result, _input(eds, rev_eds, inpt))

    def test_tl_tr_3(self):
        inpt = '1234567890'
        fmt = '(TL1, TR1, A1)'
        eds, rev_eds = _parser(_lexer(fmt))
        result = ['2']
        self.assertEqual(result, _input(eds, rev_eds, inpt))

    def test_tl_tr_4(self):
        inpt = '1234567890'
        fmt = '(TR15, TL1, A1)'
        eds, rev_eds = _parser(_lexer(fmt))
        result = ['0']
        self.assertEqual(result, _input(eds, rev_eds, inpt))

    def test_tl_tr_5(self):
        inpt = '1234567890'
        fmt = '(TR2, TL1, A1)'
        eds, rev_eds = _parser(_lexer(fmt))
        result = ['2']
        self.assertEqual(result, _input(eds, rev_eds, inpt))

    # Test combined TL and X (should be the same as TL and TR)

    def test_tl_x_1(self):
        inpt = '1234567890'
        fmt = '(TL5, 5X, A1)'
        eds, rev_eds = _parser(_lexer(fmt))
        result = ['6']
        self.assertEqual(result, _input(eds, rev_eds, inpt))

    def test_tl_x_2(self):
        inpt = '1234567890'
        fmt = '(TL5, 1X, A1)'
        eds, rev_eds = _parser(_lexer(fmt))
        result = ['2']
        self.assertEqual(result, _input(eds, rev_eds, inpt))

    def test_tl_x_3(self):
        inpt = '1234567890'
        fmt = '(TL1, 1X, A1)'
        eds, rev_eds = _parser(_lexer(fmt))
        result = ['2']
        self.assertEqual(result, _input(eds, rev_eds, inpt))

    def test_tl_x_4(self):
        inpt = '1234567890'
        fmt = '(15X, TL1, A1)'
        eds, rev_eds = _parser(_lexer(fmt))
        result = ['0']
        self.assertEqual(result, _input(eds, rev_eds, inpt))

    def test_tl_x_5(self):
        inpt = '1234567890'
        fmt = '(2X, TL1, A1)'
        eds, rev_eds = _parser(_lexer(fmt))
        result = ['2']
        self.assertEqual(result, _input(eds, rev_eds, inpt))

    # T positioning

    def test_t_1(self):
        inpt = '1234567890'
        fmt = '(T2, A1)'
        eds, rev_eds = _parser(_lexer(fmt))
        result = ['2']
        self.assertEqual(result, _input(eds, rev_eds, inpt))

    # T positioning with TL

    def test_t_tl_1(self):
        inpt = '1234567890'
        fmt = '(T15, TL1, A1)'
        eds, rev_eds = _parser(_lexer(fmt))
        result = ['0']
        self.assertEqual(result, _input(eds, rev_eds, inpt))

    def test_t_tl_2(self):
        inpt = '1234567890'
        fmt = '(T15, TL1, A)'
        eds, rev_eds = _parser(_lexer(fmt))
        result = ['0']
        self.assertEqual(result, _input(eds, rev_eds, inpt))
