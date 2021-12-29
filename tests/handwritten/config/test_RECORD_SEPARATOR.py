

import unittest

from fortranformat import FortranRecordWriter
import fortranformat.config as config

class ConfigTests(unittest.TestCase):

    def setUp(self):
        config.reset()

    def config_test_1(self):
      '''Default RECORD_SEPARATOR ('\n')'''
      ff = FortranRecordWriter('(2I10)')
      result = ff.write([0, 0, 0, 0])
      self.assertEqual(result, '         0         0\n         0         0')

    def config_test_2(self):
      '''RECORD_SEPARATOR = |'''
      config.RECORD_SEPARATOR = '|'
      result = FortranRecordWriter('(2I10)').write([0, 0, 0, 0])
      self.assertEqual(result, '         0         0|         0         0')

    
      
