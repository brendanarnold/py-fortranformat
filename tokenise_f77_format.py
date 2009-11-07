'''
tokenise_f77_format.py

Parse a Forran string according to the FORTRAN 77 specification found at,
http://www.fortran.com/fortran/F77_std/rjcnf0001-sh-13.html
and return a list of parsed token objects
'''

from tokens import *

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
    for i in range(len(format)):
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
        # Throw away spaces and commas
        if c in [' ', ',']:
            continue
        # Test if signed/unsigned integer
        if c in ['-', '+', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
            sring_buffer = string_buffer + c

        # TODO: This is a lot of work