

import unittest
import os
import sys

# sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from fortranformat._input import input as _input
from fortranformat._lexer import lexer as _lexer
from fortranformat._parser import parser as _parser
import fortranformat.config as config

class GConfigTests(unittest.TestCase):

    def setUp(self):
        config.reset()

    def g_config_test_1(self):
        # By default G_INPUT_TRIAL_EDS is set to ['F', 'L', 'A'] see if
        # float is tried first
        inpt = '3.1'
        fmt = '(G3.1)'
        eds, rev_eds = _parser(_lexer(fmt))
        result = [3.1]
        self.assertEqual(result, _input(eds, rev_eds, inpt))

    def g_config_test_2(self):
        # By default G_INPUT_TRIAL_EDS is set to ['F', 'L', 'A'] see if
        # float is tried first
        inpt = '3.13.1'
        fmt = '(G3.1, G3.1)'
        eds, rev_eds = _parser(_lexer(fmt))
        result = [3.1, 3.1]
        self.assertEqual(result, _input(eds, rev_eds, inpt))

    def g_config_test_3(self):
        # By default G_INPUT_TRIAL_EDS is set to ['F', 'L', 'A'] see if
        # Logical tried next
        inpt = '  F'
        fmt = '(G3.1)'
        eds, rev_eds = _parser(_lexer(fmt))
        result = [False]
        self.assertEqual(result, _input(eds, rev_eds, inpt))

    def g_config_test_4(self):
        # By default G_INPUT_TRIAL_EDS is set to ['F', 'L', 'A'] see if
        # text finally tried
        inpt = '  R'
        fmt = '(G3.1)'
        eds, rev_eds = _parser(_lexer(fmt))
        result = ['  R']
        self.assertEqual(result, _input(eds, rev_eds, inpt))

    def g_config_test_5(self):
        # By default G_INPUT_TRIAL_EDS is set to ['F', 'L', 'A'] see if
        # combination of different values gives correct results
        inpt = '  R3.1'
        fmt = '(2G3.1)'
        eds, rev_eds = _parser(_lexer(fmt))
        result = ['  R', 3.1]
        self.assertEqual(result, _input(eds, rev_eds, inpt))

    def g_config_test_6(self):
        # Try custom list of edit descriptors
        config.G_INPUT_TRIAL_EDS = ['Z', 'A']
        inpt = ' 10'
        fmt = '(G3.1)'
        eds, rev_eds = _parser(_lexer(fmt))
        result = [16]
        self.assertEqual(result, _input(eds, rev_eds, inpt))

    def g_config_test_7(self):
        # Try custom list of edit descriptors
        config.G_INPUT_TRIAL_EDS = ['Z', 'A']
        inpt = ' L0'
        fmt = '(G3.1)'
        eds, rev_eds = _parser(_lexer(fmt))
        result = [' L0']
        self.assertEqual(result, _input(eds, rev_eds, inpt))
        
        
