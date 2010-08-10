from _output import output
from _parser import parser

class FortranRecordWriter(object):
    '''
    Generate a writer object for FORTRAN format strings
    '''
    def __init__(self, format, version=None):
        self.version = version
        self.format = format
        self._parser = parser
        self._edit_descriptors = []
        self._parse_format()

    def __eq__(self, other):
        if type(other) == str:
            return self.match(other) 
        else:
            return object.__eq__(self, other)

    def write(self, values):
        '''
        Pass a list of values correspoding to the FORTRAN format specified
        to generate a string
        '''
        return _output(self.edit_descriptors)

    def get_format(self):
        return self._format

    def set_format(self, format):
        self._format = format
        self._parse_format()
    format = property(get_format, set_format)

    def get_version(self):
        return self._version
    def set_version(self, version):
        self._version = version
        self._parse_format()
    version = property(get_version, set_version)

    def _parse_format(self):
        self._edit_descriptors = self._parser(self.format, self.version)


if __name__ == '__main__':
    import doctest
    import os
    doctest.testmod()
##     doctest.testfile(os.path.join('tests', 'FortranRecordWriter_test.txt'))

