import math
import itertools
from fortranformat.tokens import *

def _output_from_f77_tokens(tokens, values):
    '''
    A function to take a list of valid f77 tokens and respective values
    and output the corresponding string
    '''
    values.reverse() # Allow to 'pop' values from list
    record = ''
    state = {
        'position' : 0,
        'scale' : 10**0,
        'incl_plus' : False,
        'collapse_blanks' : False,
        'halt_if_no_vals' : False,
    }

    # If format is empty with no values specified, then output blank record -
    # see section 13.3

    # Find the repeated portion of the format if the number of values supplied
    # exceeds the number of values output in the format
    num_repeatable = 0
    overflow_tokens = None
    for token in tokens:
        if isinstance(token, SubFormat):
            overflow_tokens = token
        elif token.is_repeatable:
            num_repeatable += 1
    if overflow_tokens is None:
        overflow_tokens = tokens
    # Ensure that if values are supplied then the format contains a repeatable
    # edit descriptor - see section 13.3
    if (num_repeatable == 0) and (len(values) > 0):
        raise ValueError('If values are specified at least one repeatable edit descriptor must be supplied')
    # Now expand the tokens fully
    tokens = _expand_tokens(tokens)
    overflow_tokens = _expand_tokens(overflow_tokens)
    repeat_in_overflow = False
    # Check there is repeatable edit descriptor in the overflow_tokens so that
    # if the overflow is needed we will know that the extra values can e dealt
    # with - see Section 13.3 F77 Spec.
    for token in overflow_tokens:
        if token.is_repeatable:
            repeat_in_overflow = True
    for token in tokens:
        if isinstance(token, (S, SS)):
            state['incl_plus'] = False
        if isinstance(token, (SP)):
            state['incl_plus'] = True
        elif isinstance(token, P):
            state['scale'] = token.scale
        elif isinstance(token, BN):
            state['collapse_blanks'] = True
        elif isinstance(token, BZ):
            state['collapse_blanks'] = False
        elif isinstance(token, Colon):
            state['halt_if_no_vals'] = True
        elif isinstance(token, Slash):
            state['position'], out = _write_string(record, '\n', state['position'])
        elif isinstance(token, (X, TR)):
            state['position'] = state['position'] + token.num_chars
        elif isinstance(token, TL):
            state['position'] = state['position'] - token.num_chars
        elif isinstance(token, T):
            state['position'] = token.num_chars
        elif isinstance(token, I):
            val = values.pop()
            sub_string = _compose_i_string(token, state, val)
            state['position'], record = _write_string(record, sub_string, state['position'])
        elif isinstance(token, F):
            val = values.pop()
            sub_string = _compose_f_string(token, state, val)
            state['position'], record = _write_string(record, sub_string, state['position'])
        elif isinstance(token, (E, D)):
            val = values.pop()
            sub_string = _compose_f_string(token, state, val)
            state['position'], record = _write_string(record, sub_string, state['position'])
        elif isinstance(token, G):
            val = values.pop()
            sub_string = _compose_f_string(token, state, val)
            state['position'], record = _write_string(record, sub_string, state['position'])
        elif isinstance(token, L):
            val = values.pop()
            sub_string = _compose_l_string(token, state, val)
            state['position'], record = _write_string(record, sub_string, state['position'])
        elif isinstance(token, A):
            sub_string = _compose_a_string(token, state)
            state['position'], record = _write_string(record, sub_string, state['position'])
        elif isinstance(token, (StringLiteral, H)):
            sub_string = token.char_string
            state['position'], record = _write_string(record, sub_string, state['position'])
        else:
            raise ValueError('Unrecognised token: %s' % token)

def _compose_a_string(token, state):
    # TODO
    pass

def _compose_l_string(token, state, val):
    # F77 spec 13.5.10 covers L editing
    try:
        val = bool(val)
    except ValueError:
        raise ValueError("Cannot convert '%s' to a boolean" % str(val))
    # Single T or F
    if val == True:
        sub_string = 'T'
    else
        sub_string = 'F'
    # Now pad to the specified width
    sub_string = sub_string.rjust(token.width)
    return sub_string

def _compose_g_string(token, state, val): # Hahaha!
    # TODO
    pass

def _compose_ed_string(token, state, val):
    # TODO
    pass

def _compose_f_string(token, state, val):
    # F77 spec 13.5.9.2.1 covers F editing
    # TODO: Python float format beyond numbers 9e49 outputs exponential
    # notation - this function does not as yet deal with this
    # TODO: Lots of weird fringe cases give different output to gfortran
    # decide which should emulate
    null_field = False
    # Be Pythonic in what values to accept, if it looks like an integer, then
    # so be it
    try:
        val = float(val)
    except ValueError:
        raise ValueError("Cannot convert '%s' to a float" % str(val))
    # Use alternate form, always includes decimal point
    opt_fmt = '#'
    # Include plus if required
    if (state['incl_plus'] == True):
        opt_fmt = opt_fmt + '+'
    # Create the string
    fmt = '%' + opt_fmt + str(token.width) + '.' + str(token.decimal_places) + 'f'
    sub_string = fmt % val
    # Check to see if need to trim things
    if len(sub_string) > token.width:
        # See if can remove a minus
        if (-1.0 < val <= 0) and (token.decimal_places == 0):
            sub_string = sub_string.replace('-', '', 1)
        # See if can remove leading zero
        if 0 < val < 1.0:
            sub_string = sub_string.lstrip('0')
        if val == 0:
            sub_string.strip('.')
    # See if the number still overflows
    if len(sub_str) > token.width:
        sub_string = '*' * token.width
    # Check that it now conforms
    assert(len(sub_string) <= token.width)
    return sub_string

def _compose_i_string(token, state, val):
    # F77 spec 13.5.9.1 covers integer editing 
    null_field = False
    # Be Pythonic in what values to accept, if it looks like an integer, then
    # so be it
    try:
        val = int(val)
    except ValueError:
        raise ValueError("Cannot convert '%s' to a integer" % str(val))
    if val < 0:
        len_digits = len(str(val)) - 1
    else:
        len_digits = len(str(val))
    sign = _get_sign(val, state['incl_plus'])
    len_num = len(sign + len_digits)
    # Fill the field with blanks if the number takes more room than the width
    # See F77 spec 13.5.9 remark 5.
    if len_num > token.width:
        null_field = True
    else:
        if token.padding is None:
            # Width pads with blanks
            fmt = sign + '%' + str(token.width) + 'd'
            return fmt % val
        else:
            # Width pads with blanks and padding pads with zeros with leading sign
            if len_digits <= token.padding <= len_num <= token.width:
                fmt = sign + '%.' + str(token.padding) + 'd'
                return (fmt % val).rjust(token.width)
            else:
                null_field = True
    if null_field == True:
        return '*' * token.width

def _get_sign(val, incl_plus):
    if val >= 0:
        if incl_plus == True:
            return '+'
        else:
            return =''
    else:
        return = '-'

def _expand_tokens(tokens):
    edit_descriptors = []
    for token in tokens:
        if isinstance(token, SubFormat):
            repeated_format = token.repeat * token.edit_descriptors
            edit_descriptors.extend(expand_tokens(repeated_format))
        else:
            edit_descriptors.append(token)

def _write_string(record, sub_string, pos):
    new_pos = pos + len(sub_string)
    # Pad if required with blanks - i.e. input after a TR edit descriptor - see
    # F77 format sec. 13.5.3
    if pos > len(record):
        record = record.ljust(pos, ' ')
        out =  record + sub_string
    elif pos == len(record):
        out = record + sub_string
    elif pos < len(record):
        out = record[:pos] + sub_string + record[new_pos:]
    return (new_pos, out)
