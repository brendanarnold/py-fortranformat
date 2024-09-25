

import unittest

from fortranformat._input import input as _input
from fortranformat._lexer import lexer as _lexer
from fortranformat._parser import parser as _parser
import fortranformat.config as config
from fortranformat._exceptions import *


class AllowZeroWidthEdsConfigTests(unittest.TestCase):

    def setUp(self):
        config.reset()

    def test_1(self):
        # By default zero width edit descriptor that is not positional
        # should raise no exception (although spec says it should!)
        fmt = '(F0.1)'
        toks = _lexer(fmt)
        try:
            _parser(toks)
        except InvalidFormat:
            self.assertFail()

    def test_2(self):
        # Explicitly specifying zero width edit descriptor that is not positional
        # should raise no exception
        config.ALLOW_ZERO_WIDTH_EDS = True
        fmt = '(F0.1)'
        toks = _lexer(fmt)
        try:
            _parser(toks)
        except InvalidFormat:
            self.assertFail()

    def test_3(self):
        # Setting the ALLOW_ZERO_WIDTH_EDS to False should now raise
        # exceptions as specified in spec
        config.ALLOW_ZERO_WIDTH_EDS = False
        fmt = '(F0.1)'
        toks = _lexer(fmt)
        self.assertRaises(InvalidFormat, _parser, toks)

    def test_4(self):
        # Positional editdescriptors always raise error when passed a
        # zero argument
        fmt = ('T0')
        toks = _lexer(fmt)
        self.assertRaises(InvalidFormat, _parser, toks)

    def test_5(self):
        # Positional editdescriptors always raise error when passed a
        # zero argument
        fmt = ('TL0')
        toks = _lexer(fmt)
        self.assertRaises(InvalidFormat, _parser, toks)

    def test_6(self):
        # Positional editdescriptors always raise error when passed a
        # zero argument
        fmt = ('TR0')
        toks = _lexer(fmt)
        self.assertRaises(InvalidFormat, _parser, toks)

    def test_7(self):
        # Positional editdescriptors always raise error when passed a
        # zero argument
        fmt = ('0X')
        toks = _lexer(fmt)
        self.assertRaises(InvalidFormat, _parser, toks)

    def test_8(self):
        # Positional editdescriptors always raise error when passed a
        # zero argument, even when ALLOW_ZERO_WIDTH_EDS is explicitly
        # specified
        fmt = ('0X')
        config.ALLOW_ZERO_WIDTH_EDS = True
        toks = _lexer(fmt)
        self.assertRaises(InvalidFormat, _parser, toks)

    def test_9(self):
        # Positional editdescriptors always raise error when passed a
        # zero argument, even when ALLOW_ZERO_WIDTH_EDS is explicitly
        # not specified
        fmt = ('0X')
        config.ALLOW_ZERO_WIDTH_EDS = False
        toks = _lexer(fmt)
        self.assertRaises(InvalidFormat, _parser, toks)
