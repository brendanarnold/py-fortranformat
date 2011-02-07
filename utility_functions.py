__all__ = ['read_fortran_float', 'read_fortran_integer', 'read_fortran_bool']

import re

def read_fortran_float(substring, ignore_blanks=False, scale=0):
    '''
    Actually also reads a FORTRAN double as well as a float from the start of a
    record
    '''
    # TODO: Test for asterixes
    # Adapted from http://perldoc.perl.org/perlretut.html
    float_regex = r'[+-]?\ *(?:\d+(?:\.\d*)?|\.\d+)([eEdD][+-]?\d+)?'
    end_position = None
    if ignore_blanks == True:
        end_position = len(substring)
        substring = substring.translate(None, ' \t')
        substring = substring.rjust(end_position)
    m = re.search(float_regex, substring)
    if end_position == None:
        end_position = len(m.group(0))
    float_num = float(m.group(0))
    # If exponent is not specified then scale (F77 Spec 13.5.7.1)
    if (m.group(1) == '') and (scale != 0):
        float_num = float_num * 10**scale
    return (float_num, end_position)

def read_fortran_integer(substring, ignore_blanks=False):
    # TODO: Test for asterixes
    integer_regex = r'[+-]?\d+'
    end_position = None
    if ignore_blanks == True:
        end_position = len(substring)
        substring = substring.translate(None, ' \t')
        substring = substring.rjust(end_position)
    m = re.search(integer_regex, substring)
    if end_position == None:
        end_position = len(m.group(0))
    integer_num = float(m.group(0))
    return (integer_num, end_position)

def read_fortran_bool(substring, ignore_blanks=False):
    end_position = None
    if ignore_blanks == True:
        end_position = len(substring)
        substring = substring.translate(None, ' \t')
        substring = substring.rjust(end_position)
    if substring.lstrip().startswith('.TRUE.'):
        value = True
        end_position = end_position or (position + 6)
    elif substring.lstrip().startswith('T'):
        value = True
        end_position = end_position or (position + 1)
    elif substring.lstrip().startswith('.T'):
        value = True
        end_position = end_position or (position + 2)
    elif substring.lstrip().startswith('.FALSE.'):
        value = True
        end_position = end_position or (position + 7)
    elif substring.lstrip().startswith('F'):
        value = True
        end_position = end_position or (position + 1)
    elif substring.lstrip().startswith('.F'):
        value = True
        end_position = end_position or (position + 2)
    else:
        # TODO: Raise a more appropriate exception
        raise Exception()
    return (value, end_position)
