
import unittest

import fortranformat as ff


class FortranRecordWriterTests(unittest.TestCase):

    def test_1(self):
        '''Smoke test of FortranRecordReader'''
        record_line = ff.FortranRecordReader('(I4, I4, I4)')
        self.assertEqual(record_line.read('  12   34567'), [12, 3, 4567])
