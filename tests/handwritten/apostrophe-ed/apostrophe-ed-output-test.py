import unittest
import os
import sys

from fortranformat._output import output as _output
from fortranformat._lexer import lexer as _lexer
from fortranformat._parser import parser as _parser
import fortranformat.config as config

class ApostropheOutputTests(unittest.TestCase):

    def setUp(self):
        config.reset()

    def apostrophe_output_test_1(self):
      fmt = "'Some Text'"
      eds, rev_eds = _parser(_lexer(fmt))
      result = "Some Text"
      self.assertEqual(result, _output(eds, rev_eds, []))

    def apostrophe_output_test_2(self):
      '''With commented apostrophe'''
      fmt = "'Don''t you, forget about me'"
      eds, rev_eds = _parser(_lexer(fmt))
      result = "Don't you, forget about me"
      self.assertEqual(result, _output(eds, rev_eds, []))
