
import unittest
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from _input import input as _input
from _lexer import lexer as _lexer
from _parser import parser as _parser

class MultiEditDescriptorTests(unittest.TestCase):

    def multi_test_1(self):
        # Widthless A edit descriptor takes up entire rest of string
        # Extra numerical edit descriptors should be 0, should return
        # number of values commensurate with number of edit descriptors
        inpt = '1234567890'
        fmt = '(I1, A, I1, F3.1)'
        eds, rev_eds = _parser(_lexer(fmt))
        result = [1, '234567890', 0, 0.0]
        self.assertEqual(result, _input(eds, rev_eds, inpt))

    def multi_test_2(self):
        # Widthless A edit descriptor takes up entire rest of string
        # Can use T to reread though
        inpt = '1234567890'
        fmt = '(I1.1, A, T1, I1.1)'
        eds, rev_eds = _parser(_lexer(fmt))
        result = [1, '234567890', 1]
        self.assertEqual(result, _input(eds, rev_eds, inpt))

    def multi_test_3(self):
        # Logical does not have a sensible default, raises error when
        # reading beyond end of record
        inpt = 'T23456789T'
        fmt = '(L1, A, L1)'
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inpt)

    def multi_test_4(self):
        inpt = '1234567890'
        fmt = '(A, A)'
        eds, rev_eds = _parser(_lexer(fmt))
        result = ['1234567890', '']
        self.assertEqual(result, _input(eds, rev_eds, inpt))

    def multi_test_5(self):
        # An actual typical record
        inpt = '    T    F   12  3.4 1.1E+02'
        fmt = '(L5, L5, I5.2, F5.5, E8.8E2)'
        eds, rev_eds = _parser(_lexer(fmt))
        result = [True, False, 12, 3.4, 1.1e2]
        self.assertEqual(result, _input(eds, rev_eds, inpt))

    def multi_test_6(self):
        # More edit descriptors than the input string specifies
        # Section 13.3 of F77 spec. details that format control
        # terminates, does not raise an error.
        inpt = '1'
        fmt = '(3I1)'
        eds, rev_eds = _parser(_lexer(fmt))
        result = [1]
        self.assertEqual(result, _input(eds, rev_eds, inpt))

    def multi_test_7(self):
        # More edit descriptors than the input string specifies
        # Section 13.3 of F77 spec. details that format control
        # terminates, does not raise an error.
        inpt = '1'
        fmt = '(I1, I1, I1)'
        eds, rev_eds = _parser(_lexer(fmt))
        result = [1]
        self.assertEqual(result, _input(eds, rev_eds, inpt))
