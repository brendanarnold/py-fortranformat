

import unittest
import os
import sys

from fortranformat import FortranRecordWriter, FortranRecordReader
import fortranformat.config as config

class ConfigTests(unittest.TestCase):

    def setUp(self):
        config.reset()

    def config_test_1(self):
        '''Set config after-creation of format'''
        ff = FortranRecordWriter('(2I10)')
        result = ff.write([0, 0, 0, 0])
        self.assertEqual(result, '         0         0\n         0         0')
        config.RECORD_SEPARATOR = '|'
        result = ff.write([0, 0, 0, 0])
        self.assertEqual(result, '         0         0|         0         0')


    def config_test_2(self):
        '''Test case reported on float'''
        ff = FortranRecordReader('(6g13.5)')
        result = ff.read('   1.0000       9.0000       105.09       1.0000                   ')
        config.RET_UNWRITTEN_VARS_NONE = True
        self.assertEqual(result, [1.0, 9.0, 105.09, 1.0, 0.0, 0.0])

    
      
