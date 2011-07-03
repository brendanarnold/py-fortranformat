
import unittest
import os
import sys

# sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from fortranformat._input import input as _input
from fortranformat._lexer import lexer as _lexer
from fortranformat._parser import parser as _parser
import fortranformat.config as config

class MultiEditDescriptorTests(unittest.TestCase):

    def setUp(self):
        config.reset()

    def multi_test_1(self):
        # Widthless A edit descriptor takes up entire rest of string
        # Extra numerical edit descriptors cannot be read, so default
        # return None so number of values commensurate with number of
        # edit descriptors
        inpt = '1234567890'
        fmt = '(I1, A, I1, F3.1)'
        eds, rev_eds = _parser(_lexer(fmt))
        result = [1, '234567890', None, None]
        self.assertEqual(result, _input(eds, rev_eds, inpt))

    def multi_test_2(self):
        # Can change behaviour using configuration. Setting
        # RET_UNWRITTEN_VARS_NONE to False returns default content for
        # Fortran variables (i.e. zero for numbers and ERROR for
        # logicals)
        inpt = '1234567890'
        fmt = '(I1, A, I1, F3.1)'
        config.RET_UNWRITTEN_VARS_NONE = False
        eds, rev_eds = _parser(_lexer(fmt))
        result = [1, '234567890', 0, 0.0]
        self.assertEqual(result, _input(eds, rev_eds, inpt))

    def multi_test_3(self):
        # Can change behaviour using configuration. Setting
        # RET_UNWRITTEN_VARS_NONE to False returns default content for
        # Fortran variables (i.e. zero for numbers and ERROR for
        # logicals)
        inpt = '1234567890'
        fmt = '(I1, A, L1, F3.1)'
        config.RET_UNWRITTEN_VARS_NONE = False
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(ValueError, _input, eds, rev_eds, inpt)

    def multi_test_4(self):
        # Can change behaviour using configuration. Setting
        # RET_WRITTEN_VARS_ONLY should remove unwritten varibles from
        # returned output (i.e. if run out of record, return only the
        # FORTRAN variables that have been read into)
        inpt = '1'
        fmt = '(3I1)'
        config.RET_UNWRITTEN_VARS_NONE = True
        config.RET_WRITTEN_VARS_ONLY = True
        eds, rev_eds = _parser(_lexer(fmt))
        result = [1]
        self.assertEqual(result, _input(eds, rev_eds, inpt))

    def multi_test_5(self):
        # Can change behaviour using configuration. Setting
        # RET_WRITTEN_VARS_ONLY should remove unwritten varibles from
        # returned output (i.e. if run out of record, return only the
        # FORTRAN variables that have been read into)
        inpt = '1'
        fmt = '(3I1)'
        config.RET_UNWRITTEN_VARS_NONE = False
        config.RET_WRITTEN_VARS_ONLY = True
        eds, rev_eds = _parser(_lexer(fmt))
        result = [1]
        self.assertEqual(result, _input(eds, rev_eds, inpt))

    def multi_test_6(self):
        # Widthless A edit descriptor takes up entire rest of string
        # Can use T to reread though
        inpt = '1234567890'
        fmt = '(I1.1, A, T1, I1.1)'
        eds, rev_eds = _parser(_lexer(fmt))
        result = [1, '234567890', 1]
        self.assertEqual(result, _input(eds, rev_eds, inpt))

    def multi_test_7(self):
        # Logical does not have a sensible default, raises error when
        # reading beyond end of record
        inpt = 'T23456789T'
        fmt = '(L1, A, L1)'
        eds, rev_eds = _parser(_lexer(fmt))
        result = [True, '23456789T', None]
        self.assertEqual(result, _input(eds, rev_eds, inpt))

    def multi_test_8(self):
        inpt = '1234567890'
        fmt = '(A, A)'
        eds, rev_eds = _parser(_lexer(fmt))
        result = ['1234567890', '']
        self.assertEqual(result, _input(eds, rev_eds, inpt))

    def multi_test_9(self):
        # An actual typical record
        inpt = '    T    F   12  3.4 1.1E+02'
        fmt = '(L5, L5, I5.2, F5.5, E8.8E2)'
        eds, rev_eds = _parser(_lexer(fmt))
        result = [True, False, 12, 3.4, 1.1e2]
        self.assertEqual(result, _input(eds, rev_eds, inpt))

    def multi_test_10(self):
        # More edit descriptors than the input string specifies
        # Should give None by default for variables that aren't 'read'
        # into
        inpt = '1'
        fmt = '(3I1)'
        eds, rev_eds = _parser(_lexer(fmt))
        result = [1, None, None]
        self.assertEqual(result, _input(eds, rev_eds, inpt))

    def multi_test_11(self):
        # More edit descriptors than the input string specifies
        # Should give None by default for variables that aren't 'read'
        # into
        inpt = '1'
        fmt = '(I1, I1, I1)'
        eds, rev_eds = _parser(_lexer(fmt))
        result = [1, None, None]
        self.assertEqual(result, _input(eds, rev_eds, inpt))

    def multi_test_12(self):
        # Test behaviour of BN, BZ
        inpt = '12  '
        fmt = '(BZ, I4)'
        eds, rev_eds = _parser(_lexer(fmt))
        result = [1200]
        self.assertEqual(result, _input(eds, rev_eds, inpt))

    def multi_test_13(self):
        # Test behaviour of BN, BZ
        inpt = '12  '
        fmt = '(BZ, BN, I4)'
        eds, rev_eds = _parser(_lexer(fmt))
        result = [12]
        self.assertEqual(result, _input(eds, rev_eds, inpt))

    def multi_test_14(self):
        # Test behaviour of BN, BZ
        inpt = '12 1'
        fmt = '(BZ, I4)'
        eds, rev_eds = _parser(_lexer(fmt))
        result = [1201]
        self.assertEqual(result, _input(eds, rev_eds, inpt))

    def multi_test_15(self):
        # Test behaviour of BN, BZ
        inpt = '12 1'
        fmt = '(I3, BZ, I1)'
        eds, rev_eds = _parser(_lexer(fmt))
        result = [12, 1]
