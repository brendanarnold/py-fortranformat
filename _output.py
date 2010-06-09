import math
import itertools
from _tokens import *

def _output(tokens, values):
    '''
    A function to take a list of valid f77 tokens and respective values
    and output the corresponding string
    '''
    values.reverse() # Allow to 'pop' values from list
    record = ''
    state = {
        'position' : 0,
        'scale' : 1,
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
        if isinstance(token, FormatGroup):
            overflow_tokens = token
        elif _is_repeatable(token):
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
        if _is_repeatable(token) and (not isinstance(token, FormatGroup)):
            repeat_in_overflow = True
    tokens.reverse() # Allow to 'pop' tokens from list
    overflow_tokens = itertools.cycle(overflow_tokens)
    use_overflow = False
    # Continue until out of tokens or values
    while True:
        # No more tokens, no more values, stop output, 
        # TODO: this will cut short an overflow token section - is this right?
        if len(tokens) == len(values) == 0:
            break
        # Take a token off the queue if there is any
        if len(tokens) > 0:
            token = tokens.pop()
        else:
            # Take from overflow tokens if there is a value requiring token
            assert(len(values) > 0)
            if repeat_in_overflow == True:
                token = overflow_tokens.next()
            else:
                # Is values in queue, but no tokens and no overflow tokens that
                # output a value
                # TODO: Does it stop gracefully or raise error?
                break
        # Check if token requires a value
        if isinstance(token, (I, F, E, D, G, L, A, B, EN, ES, O, Z)):
            if len(values) > 0:
                val = values.pop()
            else:
                # Is a token that requires a value but no value
                # TODO: Does it stop gracefully or raise error?
                break   
            if isinstance(token, I):
                sub_string = _compose_i_string(token, state, val)
            elif isinstance(token, F):
                sub_string = _compose_f_string(token, state, val)
            elif isinstance(token, (E, D)):
                sub_string = _compose_f_string(token, state, val)
            elif isinstance(token, G):
                sub_string = _compose_f_string(token, state, val)
            elif isinstance(token, L):
                sub_string = _compose_l_string(token, state, val)
            elif isinstance(token, A):
                sub_string = _compose_a_string(token, state, val)
            state['position'], record = _write_string(record, sub_string, state['position'])
        else:
            # Token does not require a value
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
                state['position'], record = _write_string(record, '\n', state['position'])
            elif isinstance(token, (X, TR)):
                state['position'] = state['position'] + token.num_chars
            elif isinstance(token, TL):
                state['position'] = state['position'] - token.num_chars
            elif isinstance(token, T):
                state['position'] = token.num_chars
            elif isinstance(token, (StringLiteral, H)):
                sub_string = token.char_string
                state['position'], record = _write_string(record, sub_string, state['position'])
    # Output the final record
    return record


def _compose_a_string(token, state, val):
    # F77 spec 13.5.11 covers A editing
    val = str(val)
    w = token.width
    if w is None:
        output = val
    elif w >= len(val):
        output = val.rjust(w)
    else:
        output = val[:w]
    return output


def _compose_l_string(token, state, val):
    # F77 spec 13.5.10 covers L editing try:
    try:
        val = bool(val)
    except ValueError:
        raise ValueError("Cannot convert '%s' to a boolean" % str(val))
    # Single T or F
    if val == True:
        sub_string = 'T'
    else:
        sub_string = 'F'
    # Now pad to the specified width
    sub_string = sub_string.rjust(token.width)
    return sub_string

def _compose_g_string(token, state, val): # Hahaha!
    # F77 spec 13.5.9.2.3 covers G editing
    # Be Pythonic in what values to accept, if it looks like a float, then
    # so be it
    try:
        val = float(val)
    except ValueError:
        raise ValueError("Cannot convert '%s' to a float" % str(val))
    w = token.width
    d = token.decimal_places
    e = token.exponent
    N = math.fabs(val)
    # G editing is either E of F editing depending on magnitude of val
    if (N < 0.1) or (N >= 10**d):
        # Output exponential format
        output = _compose_ed_string_without_token(w, d, e, 'E', state, val)
    else:
        # Output a plain decimal number
        if e is None:
            n = 4
        else:
            n = e + 2
        flt_w = w - n
        flt_d = d - int(math.ceil(math.log10(N)))
        # Scale factor is ignored
        flt_state = state.copy()
        flt_state['scale'] = 0
        output = _compose_ed_string_without_token(flt_w, flt_d, flt_state, val)
        # Retry with scale factor if is out of range
        if output[0] == '*':
            output = _compose_ed_string_without_token(flt_w, flt_d, state, val)
        # If still overflow then append asterixes to make up width
        if output[0] == '*':
            output = output + ('*' * n)
        else:
            output = output + (' ' * n)
    return output


def _compose_ed_string(token, state, val):
    # A wrapper so that formatting can be called without a E or D token
    if isinstance(token, D):
        type = 'D'
    else:
        type = 'E'
    return _compose_ed_string_without_token(token.width, token.decimal_places, \
      token.exponent, type, state, val)

def _compose_ed_string_without_token(w, d, e, type, state, val):
    # F77 spec 13.5.9.2.2 covers E,D editing
    overflow = False
    # Be Pythonic in what values to accept, if it looks like a float, then
    # so be it
    try:
        val = float(val)
    except ValueError:
        raise ValueError("Cannot convert '%s' to a float" % str(val))
    k = state['scale']
    exp_char = type
    # Find integer value of exponent
    if val == 0.0:
        exp_int = 0
    else:
        exp_int = int(math.floor(math.log10(math.fabs(val))))
    exp_int = exp_int - k
    # Build the exponent string
    if e is None:
        exp_str = exp_char + ('%+04d' % math.fabs(exp_int))
        if len(exp_str) > 5:
            raise ValueError('Exponent value not specified in E/D descriptor when exponent (after scale factor) has mre than 3 digits')
    else:
        fmt = '%+0' + str(e) + 'd'
        exp_str = exp_char + fmt % math.fabs(exp_int)
        if len(exp_str) > e + 2:
            overflow = True
    # Calculate the width of the exponent string
    # Adjust the value according to the scale factor
    val = val * 10**k
    # Use the f edit descriptor routine to construct significand
    sig_val = val / (10 ** exp_int)
    sig_w = w - len(exp_str)
    if -d < k <= 0:
        sig_d = d
    elif 0 < k < (d + 2):
        sig_d = d - k + 1
    else:
        # TODO what to do here?
        overflow = True
        sig_d = d
    sig_str = _compose_f_string_without_token(sig_w, sig_d, state, sig_val)
    output = sig_str + exp_str
    # If it overflows, then return asterixes
    if (len(output) > w) or (overflow == True):
        output = '*' * w    
    return output


def _compose_f_string(token, state, val):
    # A wrapper to allow the routine to be called from E, D editing routine
    return _compose_f_string_without_token(token.width, token.decimal_places, state, val)

def _compose_f_string_without_token(w, d, state, val):
    # F77 spec 13.5.9.2.1 covers F editing
    # TODO: Python float format beyond numbers 9e49 outputs exponential
    # notation - this function does not as yet deal with this
    # TODO: Lots of weird fringe cases give different output to gfortran
    # would prefer to emulate Intel compiler
    null_field = False
    # Be Pythonic in what values to accept, if it looks like a float, then
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
    fmt = '%' + opt_fmt + str(w) + '.' + str(d) + 'f'
    sub_string = fmt % val
    # Check to see if need to trim things
    if len(sub_string) > w:
        # See if can remove a minus
        if (-1.0 < val <= 0) and (d == 0):
            sub_string = sub_string.replace('-', '', 1)
        # See if can remove leading zero
        if 0 < val < 1.0:
            sub_string = sub_string.lstrip('0')
        if val == 0:
            sub_string.strip('.')
    # See if the number still overflows
    if len(sub_string) > w:
        sub_string = '*' * w
    # Check that it now conforms
    assert(len(sub_string) <= w)
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
    # Get the basic string without sign etc.
    int_string = '%d' % int(round(math.fabs(val)))
    # Pad if necessary
    if token.min_digits is not None:
        int_string = int_string.rjust(token.min_digits, '0')
        # Weird case where if zero width specified and is zero, can have zero space
        if (val == 0) and (token.min_digits == 0):
            int_string = ''
    # prepend the sign
    int_string = _get_sign(val, state['incl_plus']) + int_string
    # Fill the field with blanks if the number takes more room than the width
    # See F77 spec 13.5.9 remark 5.
    if len(int_string) > token.width:
        int_string = '*' * token.width
    else:
        int_string = int_string.rjust(token.width, ' ')
    return int_string

def _get_sign(val, incl_plus):
    if val >= 0:
        if incl_plus == True:
            return '+'
        else:
            return ''
    else:
        return '-'

def _expand_tokens(tokens):
    edit_descriptors = []
    for token in tokens:
        if isinstance(token, FormatGroup):
            repeated_format = token.repeat * token.edit_descriptors
            edit_descriptors.extend(expand_tokens(repeated_format))
        else:
            edit_descriptors.append(token)
    return edit_descriptors

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

def _is_repeatable(token):
    # Is the edit descriptor specified as repeatable?
    return isinstance(token, (A, B, D, O, L, I, G, E, F, EN, ES, Z, FormatGroup))

# Allow for self testing
if __name__ == '__main__':
    from _parser import _build_parser
    parser = _build_parser()
    import pdb
    tokens = parser.parse('D9.3')
    vals = [3.14159]
    print _output(tokens, vals)
