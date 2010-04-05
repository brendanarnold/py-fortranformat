class FortranRecordReader(object):
    '''
    Generate a reader object for FORTRAN format strings
    '''
    def __init__(self, version='f77', format=None):
        self.format = format
        self.version = version
        self._lexer = None
        self._parser = None

    def parse(self, record, format=None):
        if format == None:
            if self.format == None:
                raise ValueError('Need to define a FORTRAN format statement')
            else:
                format = self.format
        edit_descriptors = self._parser(format, lexer=self._lexer)
        values = self._input_from_tokens(edit_descriptors)
        return values

    def get_version(self):
        return self._version

    def set_version(self, version):
        self._version = version
        if self.version == 'f77':
            from _build_f77_lexer_parser import _build_f77_lexer_parser
            self._lexer, self._parser = _build_f77_lexer_parser()
            from _input_from_f77_tokens import _input_from_f77_tokens
            self._input_from_tokens = _input_from_f77_tokens
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
