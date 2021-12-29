
import unittest

import fortranformat as ff


class FortranRecordWriterTests(unittest.TestCase):

    def test_1(self):
        '''Test to cover https://github.com/brendanarnold/py-fortranformat/issues/17'''
        record_line = ff.FortranRecordWriter("f6.0")
        self.assertEqual(record_line.write([99999.01]), '99999.')
