

import unittest

from fortranformat import FortranRecordReader
import fortranformat.config as config

class ConfigTests(unittest.TestCase):

    def setUp(self):
        config.reset()

    def config_test_1(self):
      '''Default RET_WRITTEN_VARS_ONLY (False)'''
      ff = FortranRecordReader('(3G10.2)')
      result = ff.read('         0         0')
      self.assertEqual(result, [0.0, 0.0, None])

    def config_test_2(self):
      '''RET_WRITTEN_VARS_ONLY = True'''
      config.RET_WRITTEN_VARS_ONLY = True
      ff = FortranRecordReader('(3G10.2)')
      result = ff.read('         0         0')
      self.assertEqual(result, [0.0, 0.0])

    def config_test_3(self):
      '''RET_WRITTEN_VARS_ONLY = False'''
      config.RET_WRITTEN_VARS_ONLY = False
      ff = FortranRecordReader('(3G10.2)')
      result = ff.read('         0         0')
      self.assertEqual(result, [0.0, 0.0, None])

    
      
