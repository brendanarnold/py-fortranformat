
import unittest

import fortranformat as ff

class FortranRecordWriterTests(unittest.TestCase):

  def f_ed_test_1(self):
    record_line = ff.FortranRecordWriter("f6.0")
    self.assertEqual(record_line.write([99999.01]), '99999.')