import math
import itertools
from _edit_descriptors import *
import misc

def output(eds, reversion_eds, values):
    '''
    A function to take a list of valid f77 edit descriptors and respective values
    and output the corresponding string
    '''
    record = ''
    state = {
        'position' : 0,
        'scale' : 0,
        'incl_plus' : False,
        'collapse_blanks' : False,
        'halt_if_no_vals' : False,
    }

    # If format is empty with no values specified, then output blank record -
    # see section 13.3

    # Check that if there is a reversion, that values can be output
    reversion_contains_output_ed = False
    for ed in reversion_eds:
        if isinstance(ed, OUTPUT_EDS):
            reversion_contains_output_ed = True
            break
    # Use iterators
    get_ed = misc.has_next_iterator(eds)
    get_value = misc.has_next_iterator(values)
    get_reversion_ed = itertools.cycle(reversion_eds)
    # Continue until out of edit descriptors or values
    while True:
        # No more edit descriptors, no more values, stop output, 
        # TODO: this will cut short an reversion edit descriptor section - is this right?
        if not get_ed.has_next() and not get_value.has_next():
            break
        # Take a edit descriptor off the queue if there is any
        if get_ed.has_next():
            ed = get_ed.next()
        else:
            if reversion_contains_output_ed == True:
                # Take from reversion edit descriptors if there is a value
                # requiring output still
                ed = get_reversion_ed.next()
                # These edit descriptors are ignored in reversion state
                while isinstance(ed, NON_REVERSION_EDS):
                    ed = get_reversion_ed.next()
            else:
                # Ignore the revsion edit descriptors as cannot output the
                # final value
                break
        # Check if edit descriptor requires a value
        if isinstance(ed, OUTPUT_EDS):
            if get_value.has_next():
                val = get_value.next()
            else:
                # Is a edit descriptor that requires a value but no value
                # TODO: Does it stop gracefully or raise error?
                break   
            if isinstance(ed, I):
                sub_string = _compose_i_string(ed.width, ed.min_digits, state, val)
            elif isinstance(ed, F):
                sub_string = _compose_f_string(ed.width, ed.decimal_places, state, val)
            elif isinstance(ed, E):
                sub_string = _compose_e_string(ed.width, ed.decimal_places, ed.exponent, state, val)
            elif isinstance(ed, D):
                sub_string = _compose_d_string(ed.width, ed.decimal_places, state, val)
            elif isinstance(ed, G):
                sub_string = _compose_g_string(ed.width, ed.decimal_places, ed.exponent, state, val)
            elif isinstance(ed, L):
                sub_string = _compose_l_string(ed.width, state, val)
            elif isinstance(ed, A):
                sub_string = _compose_a_string(ed.width, state, val)
            state['position'], record = _write_string(record, sub_string, state['position'])
        else:
            # Token does not require a value
            if isinstance(ed, (S, SS)):
                state['incl_plus'] = False
            if isinstance(ed, (SP)):
                state['incl_plus'] = True
            elif isinstance(ed, P):
                state['scale'] = ed.scale
            elif isinstance(ed, BN):
                state['collapse_blanks'] = True
            elif isinstance(ed, BZ):
                state['collapse_blanks'] = False
            elif isinstance(ed, Colon):
                state['halt_if_no_vals'] = True
            elif isinstance(ed, Slash):
                state['position'], record = _write_string(record, '\n', state['position'])
            elif isinstance(ed, (X, TR)):
                state['position'] = state['position'] + ed.num_chars
            elif isinstance(ed, TL):
                state['position'] = state['position'] - ed.num_chars
            elif isinstance(ed, T):
                state['position'] = ed.num_chars
            elif isinstance(ed, QuotedString):
                sub_string = ed.char_string
                state['position'], record = _write_string(record, sub_string, state['position'])
    # Output the final record
    return record


def _compose_a_string(w, state, val):
    # F77 spec 13.5.11 covers A editing
    val = str(val)
    if w is None:
        output = val
    elif w >= len(val):
        output = val.rjust(w)
    else:
        output = val[:w]
    return output


def _compose_l_string(w, state, val):
    # F77 spec 13.5.10 covers L editing
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
    sub_string = sub_string.rjust(w)
    return sub_string

def _compose_g_string(w, d, e, state, val): # Hahaha!
    # F77 spec 13.5.9.2.3 covers G editing
    # Be Pythonic in what values to accept, if it looks like a float, then
    # so be it
    try:
        val = float(val)
    except ValueError:
        raise ValueError("Cannot convert '%s' to a float" % str(val))
    N = math.fabs(val)
    # G editing is either E of F editing depending on the value
    max_N = 10**d - 0.5
    min_N = 0.1 - 0.5 * 10**(-d-1)
    if not (((d > 0) and (N == 0)) or \
	    (min_N <= N < max_N)):
        # Output exponential format
        output = _compose_e_string(w, d, e, state, val)
    else:
        # Output a plain decimal number
        if e is None:
            n = 4
        else:
            n = e + 2
        flt_w = w - n
        # Scale factor is ignored
        flt_state = state.copy()
        flt_state['scale'] = 0
        output = _compose_f_string(flt_w, d, flt_state, val)
        # Retry with scale factor if is out of range
        if '*' in output:
            output = _compose_f_string(flt_w, d, state, val)
        # If still short then append asterixes or blanks to make up width
        if '*' in output:
            output = output + ('*' * n)
        else:
            output = output + (' ' * n)
    # Finally if the string is blank, fill with asterixes
    if (output.strip() == '') and (w > 0):
        output = w * '*'
    return output

def _compose_d_string(w, d, state, val):
    return _compose_e_string(w, d, 2, state, val, exp_char='D')

def _compose_e_string(w, d, e, state, val, exp_char='E'):
    # F77 spec 13.5.9.2.2 covers E editing
    sub_asterix = False
    # Be Pythonic in what values to accept, if it looks like a float, then
    # so be it
    try:
        val = float(val)
    except ValueError:
        raise ValueError("Cannot convert '%s' to a float" % str(val))
    k = state['scale']
    # Find integer value of exponent
    if val == 0.0:
        exp_int = 0
    else:
        exp_int = int(math.floor(math.log10(math.fabs(val)))) + 1
    exp_int = exp_int - k
    # Build the exponent string
    if e is None:
        e = 2
    fmt = '%+0' + str(e+1) + 'd' 
    exp_str = exp_char + fmt % exp_int
    if len(exp_str) > (e + 2):
        sub_asterix = True
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
        sub_asterix = True
        sig_d = d
    sig_str = _compose_f_string(sig_w, sig_d, state, sig_val)
    if ('*' in sig_str) or (sig_str == ''):
        sub_asterix = True
    output = sig_str + exp_str
    # If it sub_asterix, then return asterixes
    if (len(output) > w) or (sub_asterix == True):
        output = '*' * w    
    return output


def _compose_f_string(w, d, state, val):
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
        if 0 <= val < 1.0:
            sub_string = sub_string.lstrip('0')
        if val == 0:
            sub_string = sub_string.strip('.')
    # See if the number still fits
    if len(sub_string) > w:
        sub_string = '*' * w
    # Check that it now conforms
##     assert(len(sub_string) <= w)
    return sub_string

def _compose_i_string(w, d, state, val):
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
    if d is not None:
        int_string = int_string.rjust(d, '0')
        # Weird case where if zero width specified and is zero, can have zero space
        if (val == 0) and (d == 0):
            int_string = ''
    # prepend the sign
    int_string = _get_sign(val, state['incl_plus']) + int_string
    # Fill the field with blanks if the number takes more room than the width
    # See F77 spec 13.5.9 remark 5.
    if len(int_string) > w:
        int_string = '*' * w
    else:
        int_string = int_string.rjust(w, ' ')
    return int_string

def _get_sign(val, incl_plus):
    if val >= 0:
        if incl_plus == True:
            return '+'
        else:
            return ''
    else:
        return '-'

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

# Allow for self testing
if __name__ == '__main__':
    import doctest
    import os
    from _parser import parser
    from _lexer import lexer
    globs = {
        '_write_string' : _write_string,
        '_get_sign' : _get_sign,
        'parser' : parser,
        'lexer' : lexer,
        'output' : output
    }
    # Need to normalize whitespace since pasting into VIM converts tabs to
    # spaces
    doctest.testfile(os.path.join('tests', 'output_write_string_test.txt'), \
        globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
    doctest.testfile(os.path.join('tests', 'output_get_sign_test.txt'), \
        globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
    doctest.testfile(os.path.join('tests', 'output_test.txt'), \
        globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)

