

import unittest
import os
import sys

from fortranformat import FortranRecordReader
import fortranformat.config as config

class ConfigTests(unittest.TestCase):

    def setUp(self):
        config.reset()

    def config_test_1(self):
      '''Default G_INPUT_TRIAL_EDS'''
      ff = FortranRecordReader('(G10.2)')
      result = ff.read('         0')
      self.assertEqual(result, [0.0])

    def config_test_2(self):
      '''Default G_INPUT_TRIAL_EDS'''
      ff = FortranRecordReader('(G10.2)')
      result = ff.read('       .T.')
      self.assertEqual(result, [True])

    def config_test_3(self):
      '''Default G_INPUT_TRIAL_EDS'''
      ff = FortranRecordReader('(G10.2)')
      result = ff.read('       .F.')
      self.assertEqual(result, [False])

    def config_test_4(self):
      '''Default G_INPUT_TRIAL_EDS'''
      ff = FortranRecordReader('(G10.2)')
      result = ff.read('       STR')
      self.assertEqual(result, ['       STR'])

    def config_test_5(self):
      '''Custom G_INPUT_TRIAL_EDS'''
      config.G_INPUT_TRIAL_EDS = ['A']
      ff = FortranRecordReader('(G10.2)')
      result = ff.read('         0')
      self.assertEqual(result, ['         0'])

    def config_test_6(self):
      self.skipTest('hangs, issue logged at https://github.com/brendanarnold/py-fortranformat/issues/15')
      '''Custom G_INPUT_TRIAL_EDS'''
      config.G_INPUT_TRIAL_EDS = ['L']
      ff = FortranRecordReader('(G10.2)')
      result = ff.read('         0')
      self.assertEqual(result, [None])
      
