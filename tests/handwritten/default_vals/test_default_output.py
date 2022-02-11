import unittest

from fortranformat._output import output as _output
from fortranformat._lexer import lexer as _lexer
from fortranformat._parser import parser as _parser
import fortranformat.config as config


class DefaultOutputTests(unittest.TestCase):
    """
    Raised off the back of https://github.com/brendanarnold/py-fortranformat/issues/21
    Basically the output for 'None' should represent the uninitialise/default values of 
    FORTRAN variables
    """

    def setUp(self):
        config.reset()

    def test_1(self):
        """
        Integer default value is 0
        """
        inpt = [0.0, 1.0, None]
        fmt = '(3I10)'
        eds, rev_eds = _parser(_lexer(fmt))
        result = '         0         1         0'
        self.assertEqual(result, _output(eds, rev_eds, inpt))

    def test_2(self):
        """
        Integer default value is 0
        """
        inpt = [0.0, None, 1.0]
        fmt = '(3I10)'
        eds, rev_eds = _parser(_lexer(fmt))
        result = '         0         0         1'
        self.assertEqual(result, _output(eds, rev_eds, inpt))

    def test_3(self):
        """
        Float default value is 0
        """
        inpt = [0.0, None, 1.0]
        fmt = '(3F10.1)'
        eds, rev_eds = _parser(_lexer(fmt))
        result = '       0.0       0.0       1.0'
        self.assertEqual(result, _output(eds, rev_eds, inpt))

    def test_4(self):
        """
        Logical default value is .TRUE.
        """
        inpt = [True, None, False]
        fmt = '(3L10)'
        eds, rev_eds = _parser(_lexer(fmt))
        result = '         T         T         F'
        self.assertEqual(result, _output(eds, rev_eds, inpt))

    def test_5(self):
        """
        String default value is empty
        """
        inpt = ['[', None, ']']
        fmt = '(3A10)'
        eds, rev_eds = _parser(_lexer(fmt))
        result = '         [                   ]'
        self.assertEqual(result, _output(eds, rev_eds, inpt))

    def test_6(self):
        """
        Hex default value is 0
        """
        inpt = [1, None, 1]
        fmt = '(3Z10)'
        eds, rev_eds = _parser(_lexer(fmt))
        result = '         1         0         1'
        self.assertEqual(result, _output(eds, rev_eds, inpt))

    def test_7(self):
        """
        Binary default value is 0
        """
        inpt = [1, None, 1]
        fmt = '(3B10)'
        eds, rev_eds = _parser(_lexer(fmt))
        result = '         1         0         1'
        self.assertEqual(result, _output(eds, rev_eds, inpt))

    def test_7(self):
        """
        Octal default value is 0
        """
        inpt = [1, None, 1]
        fmt = '(3O10)'
        eds, rev_eds = _parser(_lexer(fmt))
        result = '         1         0         1'
        self.assertEqual(result, _output(eds, rev_eds, inpt))

    def test_8(self):
        """
        Exponential default value is 0.0
        """
        inpt = [1, None, 1]
        fmt = '(3E10.1)'
        eds, rev_eds = _parser(_lexer(fmt))
        result = '   0.1E+01   0.0E+00   0.1E+01'
        self.assertEqual(result, _output(eds, rev_eds, inpt))

    def test_9(self):
        """
        Exponential D default value is 0.0
        """
        inpt = [1, None, 1]
        fmt = '(3D10.1)'
        eds, rev_eds = _parser(_lexer(fmt))
        result = '   0.1D+01   0.0D+00   0.1D+01'
        self.assertEqual(result, _output(eds, rev_eds, inpt))

    def test_10(self):
        """
        Exponential EN default value is 0.0
        """
        inpt = [1, None, 1]
        fmt = '(3EN10.1)'
        eds, rev_eds = _parser(_lexer(fmt))
        result = '   1.0E+00   0.0E+00   1.0E+00'
        self.assertEqual(result, _output(eds, rev_eds, inpt))

    def test_11(self):
        """
        Exponential ES default value is 0.0
        """
        inpt = [1, None, 1]
        fmt = '(3ES10.1)'
        eds, rev_eds = _parser(_lexer(fmt))
        result = '   1.0E+00   0.0E+00   1.0E+00'
        self.assertEqual(result, _output(eds, rev_eds, inpt))
