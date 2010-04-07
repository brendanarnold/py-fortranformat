class FortranRecordReader(object):
    '''
    Generate a reader object for FORTRAN format strings
    '''
    def __init__(self, format=None, version='f77'):
        self.format = format
        self.version = version
        self._parser = None
        self._edit_descriptors = []

    def __eq__(self, other):
        if type(other) == str:
            return self.match(other) 
        else:
            return object.__eq__(self, other)

    def match(self, record):
        try:
            self.read(record)
        except RecordError:
            return False
        else:
            return True

    def read(self, record):
        state = {
            'position' : 0,
            'repeat_val' : False,
            'scale' : None,
            'ignore_blanks' : False,
        }
        values = []
        for edit_desc in self._edit_descriptors:
            value, state = edit_desc.input(record, state)

    def write(self, values):
        state = {
            'position' : 0,
            'repeat_val' : False,
            'scale' : None,
            'ignore_blanks' : False,
        }
        out = ''
        i = 0
        len_eds = len(self._edit_descriptors)
        for value in values:
            edit_descriptor = self._edit_descriptors[i % len_eds]
            out, state = out + edit_descriptor(out, value, state)
            # Some edit descriptors contain their own values (i.e. 
            # StringLiteral)
            while state['repeat_val'] == True:
                i = i + 1
                edit_descriptor = self._edit_descriptors[i % len_eds]
                out, state = out + edit_descriptor(out, value, state)
            i = i + 1

    def get_format(self):
        return self._format

    def set_format(self, format):
        self._format = format
        self._edit_descriptors = self._parser(format)

    format = property(get_format, set_format)

    def get_version(self):
        return self._version

    def set_version(self, version):
        self._version = version
        if self.version == 'f77':
            from _build_f77_lexer_parser import _build_f77_lexer_parser
            self._parser = _build_f77_lexer_parser()
##             from _input_from_f77_tokens import _input_from_f77_tokens
##             self._input_from_tokens = _input_from_f77_tokens
        elif self.version == 'f90':
            # TODO version f90
            pass
        elif self.version == 'f95':
            # TODO version f95
            pass
        elif self.version == 'f2003':
            # TODO version f2003
            pass
        else:
            raise ValueError('Unknown FORTRAN version specified')

    version = property(get_version, set_version)


if __name__ == '__main__':
    import doctest
    import os
    doctest.testmod()
    doctest.testfile(os.path.join('tests', 'FortranRecordReader_test.txt'))
