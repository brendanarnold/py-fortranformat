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

    # Split format into raw token strings
    raw_tokens = _split_raw_tokens(format)

    # == Expand repeated format statements
    raw_tokens = _expand_raw_tokens(raw_tokens)

    # == Convert raw tokens to token objects ==
    tokens = []
    state = {
        'multiplier' : 1,
    }
    for i in xrange(len(raw_tokens)):
        # Cache the current and next raw token in the sequence
        raw_token = raw_tokens[i]
        if i < len(raw_tokens) - 1:
            next_raw_token = raw_tokens[i+1]
        else:
            next_raw_token = ''
        if raw_token == '(':

        if isinstance(raw_token, int):
            state['multiplier'] = raw_token


def _split_raw_tokens(format):
    tokens = []
    string_buffer = ''
    state = {
        'quoted' : False,
        'escape' : False,
        'skip_chars' : 0,
    }
    for i in xrange(len(format)):
        # If necessary to skip a character, do so
        if state['skip_chars'] > 0:
            state['skip_chars'] = state['skip_char'] - 1
            continue
        c = format[i]
        # Cache the next character
        if len(format) > c + 1:
            c_next = format[i+1]
        else:
            c_next = ''

        # == Split into tokens ==

        # Start or end a string
        if c == "'":
            # The case of the escaped apostrophe in a string literal
            if state['quoted'] == True and c_next == "'":
                state['skip_chars'] = 1
                string_buffer = string_buffer + c
                continue
            state['quoted'] = not state['quoted']
            # If come to end of string literal, add to buffer
            if state['quoted'] == False:
                raw_tokens.append(string_buffer)
                string_buffer = ''
            continue
        # In a string, add to buffer, important this comes after testing for quote char!
        if state['quoted'] == True:
            string_buffer = string_buffer + c
            continue
        # Test if signed/unsigned integer
        if c in SIGNS + NUMS:
            int_str = read_int(format[i:])
            raw_tokens.append(int(int_str))
            state['skip_chars'] = len(int_str) - 1
            continue
        # Add a double character token
        if c+c_next in F77_EDIT_DESCRIPTORS:
            raw_tokens.append(c+c_next)
            state['skip_chars'] = 1
            continue
        # Add a single character token
        if c in F77_EDIT_DESCRIPTORS + ['.', '(', ')', ':', '/', ',']:
            raw_tokens.append(c)
            continue
        # Throw away unquoted spaces and tabs
        if c in [' ', '\t']:
            continue
        # Anything else also gets thrown away
    return raw_tokens

def _map_token_objects(raw_tokens):
    rt_buffer = []
    token_objects = []
    for rt in raw_tokens:
        if rt in [',', '/', ':']:
            # Dump buffer
            if rt == '/':
                token_objects.append(Slash())
            elif rt == ':':
                token_objects.append(Colon())
        


def _expand_raw_tokens(raw_tokens):
    '''Expands nested repeating format statements into full statements'''
    expanded_tokens = []
    state = {
        'skip' 0,
    }
    num_tokens_in_format = 1
    for i in xrange(len(raw_tokens)):
        # Skip tokens if necessary
        if state['skip']:
            state['skip'] = state['skip'] - 1
            continue
        # Cache the current and next token
        t = raw_tokens[i]
        if i < len(raw_tokens) - 1:
            t_next = raw_tokens[i+1]
        else:
            t_next = ''
        # A format group without a numerical multiplier
        if t == '(':
            state['skip'], tmp_tokens = _expand_raw_tokens(raw_tokens[i+1:])
            expanded_tokens = expanded_tokens + tmp_tokens
        # A format group with a numerical multiplier
        if isinstance(t, int) and t > 0 and t_next == '(':
            state['skip'], tmp_tokens = _expand_raw_tokens(raw_tokens[i+2:])
            expanded_tokens = expanded_tokens + t * _expand_raw_tokens(raw_tokens[i+2:])
            state['skip'] = state['skip'] + 1 # Necessary to skip the multiplier too
        # End the format and return the group
        elif t == ')':
            return (num_tokens_in_format, expanded_tokens)
        # Add the token to the list
        else:
            num_tokens_in_format = num_tokens_in_format + 1
            expanded_tokens.append(t)
    # Fell off the token list without hitting a closing bracket
    return expanded_tokens


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

