

import unittest
import os
import sys

# sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from fortranformat._output import output as _output
from fortranformat._lexer import lexer as _lexer
from fortranformat._parser import parser as _parser
import fortranformat.config as config

class GOutputTests(unittest.TestCase):

    def setUp(self):
        config.reset()

    def g_output_test_1(self):
        inpt = [0.0]
        fmt = '(G10.2)'
        eds, rev_eds = _parser(_lexer(fmt))
        result = "  0.00E+00"
        self.assertEqual(result, _output(eds, rev_eds, inpt))


