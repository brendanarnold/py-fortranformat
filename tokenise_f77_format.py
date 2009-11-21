'''
tokenise_f77_format.py

Parse a Forran string according to the FORTRAN 77 specification found at,
http://www.fortran.com/fortran/F77_std/rjcnf0001-sh-13.html
and return a list of parsed token objects
'''

from tokens import *
from exceptions import InvalidFortranFormat
from CONSTANTS import *


def tokenise_f77_format(format):
    '''
    Parse a Forran string according to the FORTRAN 77 specification found at,
    http://www.fortran.com/fortran/F77_std/rjcnf0001-sh-13.html
    and return a list of parsed token objects
    '''
    '''Takes a FORTRAN 77 FORMAT string and tokenises it into various objects'''

    # First need to tokenise the format string
    # First parse off the chaff - see 13.1.2
    format = format.split('(')[1].split(')')[0]
    tokens = []
    string_buffer = ''
    flag = {
        'quoted' : False,
        'escape' : False,
        'skip_chars' : 0,
    }
    for i in xrange(len(format)):
        # If necessary to skip a character, do so
        if flag['skip_chars'] > 0:
            flag['skip_chars'] = flag['skip_char'] - 1
            continue
        c = format[i]
        if len(format) > c + 1:
            c_next = format[i+1]
        else:
            c_next = ''
        # Start or end a string
        if c == "'":
            # The case of the escaped apostrophe in a string literal
            if flag['quoted'] == True and c_next == "'":
                flag['skip_chars'] = 1
                string_buffer = string_buffer + c
                continue
            flag['quoted'] = not flag['quoted']
            # If come to end of string literal, add to buffer
            if flag['quoted'] == False:
                tokens.append(string_buffer)
                string_buffer = ''
            continue
        # In a string, add to buffer, important this comes after testing for quote char!
        if flag['quoted'] == True:
            string_buffer = string_buffer + c
            continue
        # Test if signed/unsigned integer
        if c in SIGNS + NUMS:
            int_str = read_int(format[i:])
            tokens.append(int_str)
            flag['skip_chars'] = len(int_str) - 1
            continue
        # Add a double character token
        if c+c_next in F77_EDIT_DESCRIPTORS:
            tokens.append(c+c_next)
            flag['skip_chars'] = 1
            continue
        # Add a single character token
        if c in F77_EDIT_DESCRIPTORS + ['.', '(', ')', ':', '/']:
            tokens.append(c)
            continue
        # Throw away spaces and commas
        if c in [' ', ',']:
            continue

    


def read_int(str, is_signed=True):
    '''Continues reading in a signed/un-signed integer from a string until it ceases to be an integer'''
    for i, c in enumerate(str):
        if c in SIGNS:
            if i != 0 or is_signed == False:
                raise InvalidFortranFormat('Parsed an invalid integer')
        elif c not in NUMS:
            i = i - 1
            break
    int_str = str[:i+1]
    if int_str in SIGNS:
        raise InvalidFortranFormat('Parsed an invalid integer')
    else:
        return int_str

