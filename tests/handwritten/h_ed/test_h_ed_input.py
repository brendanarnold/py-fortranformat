import unittest

from fortranformat._input import input as _input
from fortranformat._lexer import lexer as _lexer
from fortranformat._parser import parser as _parser
from fortranformat._exceptions import InvalidFormat
import fortranformat.config as config


class HEditDescriptorTests(unittest.TestCase):

    def setUp(self):
        config.reset()

    def test_1(self):
        inpt = 'sdf'
        fmt = '(3Hsdf)'
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(InvalidFormat, _input, eds, rev_eds, inpt)

    def test_2(self):
        inpt = 'sdf'
        fmt = '(3Hsdf, F3.1)'
        eds, rev_eds = _parser(_lexer(fmt))
        self.assertRaises(InvalidFormat, _input, eds, rev_eds, inpt)
