import math
import itertools
from _edit_descriptors import *
import misc
import sys

SIGN_ZERO = False # Show a sign at all for zero?
OPTIONAL_PLUS = False # If not specified, show the plus sign?
MIN_FIELD_WIDTH = 46
DECIMAL_CHAR = '.'
G0_NO_BLANKS = False


def output(eds, reversion_eds, values):
    '''
    a function to take a list of valid f77 edit descriptors and respective values
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

    # if format is empty with no values specified, then output blank record -
    # see section 13.3

    # check that if there is a reversion, that values can be output
    reversion_contains_output_ed = False
    for ed in reversion_eds:
        if isinstance(ed, OUTPUT_EDS):
            reversion_contains_output_ed = True
            break
    # use iterators
    get_ed = misc.has_next_iterator(eds)
    get_value = misc.has_next_iterator(values)
    get_reversion_ed = itertools.cycle(reversion_eds)
    # continue until out of edit descriptors or values
    while True:
        # no more edit descriptors, no more values, stop output, 
        # todo: this will cut short an reversion edit descriptor section - is this right?
        if not get_ed.has_next() and not get_value.has_next():
            break
        # take a edit descriptor off the queue if there is any
        if get_ed.has_next():
            ed = get_ed.next()
        else:
            if reversion_contains_output_ed == True:
                # take from reversion edit descriptors if there is a value
                # requiring output still
                ed = get_reversion_ed.next()
                # these edit descriptors are ignored in reversion state
                while isinstance(ed, NON_REVERSION_EDS):
                    ed = get_reversion_ed.next()
            else:
                # ignore the revsion edit descriptors as cannot output the
                # final value
                break
        # check if edit descriptor requires a value
        if isinstance(ed, OUTPUT_EDS):
            if get_value.has_next():
                val = get_value.next()
            else:
                # is a edit descriptor that requires a value but no value
                # todo: does it stop gracefully or raise error?
                break   
            if isinstance(ed, I):
                sub_string = _compose_i_string(ed.width, ed.min_digits, state, val)
            elif isinstance(ed, B):
                w = ed.width
                m = ed.min_digits
                sub_string = _compose_boz_string(w, m, state, val, 'B')
            if isinstance(ed, O):
                w = ed.width
                m = ed.min_digits
                sub_string = _compose_boz_string(w, m, state, val, 'O')
            if isinstance(ed, Z):
                w = ed.width
                m = ed.min_digits
                sub_string = _compose_boz_string(w, m, state, val, 'Z')
            elif isinstance(ed, F):
                w = ed.width
                e = None
                d = ed.decimal_places
                sub_string = _compose_float_string(w, e, d, state, val, 'F')
            elif isinstance(ed, E):
                w = ed.width
                e = ed.exponent
                d = ed.decimal_places
                sub_string = _compose_float_string(w, e, d, state, val, 'E')
            elif isinstance(ed, D):
                w = ed.width
                e = None
                d = ed.decimal_places
                sub_string = _compose_float_string(w, e, d, state, val, 'D')
            elif isinstance(ed, G):
                w = ed.width
                e = ed.exponent
                d = ed.decimal_places
                sub_string = _compose_float_string(w, e, d, state, val, 'G')
            elif isinstance(ed, EN):
                w = ed.width
                e = ed.exponent
                d = ed.decimal_places
                sub_string = _compose_float_string(w, e, d, state, val, 'EN')
            elif isinstance(ed, ES):
                w = ed.width
                e = ed.exponent
                d = ed.decimal_places
                sub_string = _compose_float_string(w, e, d, state, val, 'ES')
            elif isinstance(ed, L):
                sub_string = _compose_l_string(ed.width, state, val)
            elif isinstance(ed, A):
                sub_string = _compose_a_string(ed.width, state, val)
            state['position'], record = _write_string(record, sub_string, state['position'])
        else:
            # token does not require a value
            if isinstance(ed, (S, SS)):
                state['incl_plus'] = False
            if isinstance(ed, SP):
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
    # output the final record
    return record

def _compose_nan_string(w, ftype):
    if ftype in ['B', 'O', 'Z']:
        return ''
    else:
        # Allow at least 'NaN' to be printed
        if w == 0:
            w = 4 # n.b. this is what is set in Gfortran 4.4.0
        if w < 3:
            return '*' * w
    return 'NaN'.rjust(w)

def _compose_inf_string(w, ftype, sign_bit):
    if ftype in ['B', 'O', 'Z']:
        return ''
    else:
        sign = '+'
        # Allow at least 'Inf' to be printed
        if w == 0:
            w = 4
        if w < 3:
            return '*' * w
        # Change sign if negative
        if sign_bit:
            sign = '-'
            # Require sign if negative, if no space then overflow
            if w == 3:
                return '*' * w
        # Output long version if long enough
        if w > 8:
            return (sign + 'Infinity').rjust(w)
        # Output shortened version with sign if long enough
        elif w > 3:
            return (sign + 'Inf').rjust(w)
        # Should only output short version with no sign if positive
        else:
            return 'Inf'
                

def _compose_float_string(w, e, d, state, val, ftype):
    '''
    Adapted from code in glibfortran which is written in C so is somwhat
    'bit-pushy' in nature. Writes the value to an initial string (buffer)
    and then pulls the subsequent strings from that
    '''
    if (d < 0) or (d is None):
        raise InvalidFormat('Unspecified precision')
    # Make sure they are ints
    d = int(round(d))
    if e is not None:
        e = int(round(e))
    if w is not None:
        w = int(round(w))
    # ==== write_float ==== (function)
    edigits = 4 # Largest number of exponent digits expected
    if (ftype in ['F', 'EN', 'G']) or \
        ((ftype in ['D', 'E']) and (state['scale'] != 0)):
        # Convert with full possible precision
        ndigits = MIN_FIELD_WIDTH - 4 - edigits
    else:
        # Otherwise convert knowing what the required precision is (i.e. knowing d)
        if ftype == 'ES':
            ndigits = d + 1
        else:
            ndigits = d
        if ndigits > (MIN_FIELD_WIDTH - 4 - edigits):
            ndigits = MIN_FIELD_WIDTH - 4 - edigits
    # ==== WRITE_FLOAT ==== (macro)
    # Determine sign of value
    if val == 0.0:
        sign_bit = '-' in str(val)
    else:
        sign_bit = val < 0
    # handle the nan and inf cases
    if math.isnan(val):
        return _compose_nan_string(w, ed)
    if math.isinf(val):
        return _compose_inf_string(w, ed, sign_bit)
    tmp = abs(val)
    # Round the input if the input is less than 1
    if (ftype == 'F') and (d == state['scale']) and (d == 0):
        if tmp < 1.0:
            tmp = round(tmp)
    zero_flag = (tmp == 0)
    # === DTOA === (macro)
    # write the tmp value to the string buffer
    # sprintf seems to allow negative number of decimal places, need to correct for this
    if ndigits <= 0:
        fmt = '%+-#' + str(MIN_FIELD_WIDTH) + 'e'
    else:
        fmt = '%+-#' + str(MIN_FIELD_WIDTH) + '.' + str(ndigits - 1) + 'e'
    buff = fmt % tmp
    # === WRITE_FLOAT === (macro)
    if ftype != 'G':
        return  _output_float(w, d, e, state, ftype, buff, sign_bit, zero_flag, ndigits, edigits)
    else:
        # Perform different actions for G edit descriptors depending on value
        #
        # Generate corresponding I/O format for FMT_G and output.
        # The rules to translate FMT_G to FMT_E or FMT_F from DEC fortran
        # LRM (table 11-2, Chapter 11, "I/O Formatting", P11-25) is:
        # 
        # Data Magnitude                              Equivalent Conversion
        # 0< m < 0.1-0.5*10**(-d-1)                   Ew.d[Ee]
        # m = 0                                       F(w-n).(d-1), n' '
        # 0.1-0.5*10**(-d-1)<= m < 1-0.5*10**(-d)     F(w-n).d, n' '
        # 1-0.5*10**(-d)<= m < 10-0.5*10**(-d+1)      F(w-n).(d-1), n' '
        # 10-0.5*10**(-d+1)<= m < 100-0.5*10**(-d+2)  F(w-n).(d-2), n' '
        # ................                           ..........
        # 10**(d-1)-0.5*10**(-1)<= m <10**d-0.5       F(w-n).0,n(' ')
        # m >= 10**d-0.5                              Ew.d[Ee]
        # 
        # notes: for Gw.d ,  n' ' means 4 blanks
        #        for Gw.dEe, n' ' means e+2 blanks
        nb = 0
        save_scale_factor = state['scale']
        exp_d = 10 ** d
        if (0.0 < tmp < (0.1 - 0.05 / exp_d)) or \
            (tmp >= (exp_d - 0.5)):
            ftype = 'E'
        elif tmp == 0.0:
            pass
        else:
            mag = int(abs(round(math.log10(tmp))))
            low = lambda mag, d : 10 ** (mag - 1) - 5 * 10 ** (-d - 1 + mag) 
            high = lambda mag, d : 10 ** mag - 0.5 * 10 ** (-d + mag)
            while tmp < low(mag, d):
                mag = mag - 1
            while tmp >= high(mag, d):
                mag = mag + 1
            assert(low(mag, d) <= tmp < high(mag, d))
            if e < 0:
                nb = 4
            else:
                nb = e + 2
            ftype = 'F'
            w = w - nb
            if tmp == 0.0:
                d = d - 1
            else:
                d = d - mag
                # d = -(mid - d - 1)
            state['scale'] = 0
        out = _output_float(w, d, e, state, ftype, buff, sign_bit, zero_flag, ndigits, edigits)
        state['scale'] = save_scale_factor
        # TODO: this may not be right ...
        if nb > 0:
            if '*' in out:
                out = out + ('*' * nb)
            else:
                out = out + (' ' * nb)
        if len(out) > (w + nb):
            out = '*' * (w + nb)
        return out
        

def _output_float(w, d, e, state, ft, buff, sign_bit, zero_flag, ndigits, edigits):

    # nbefore - number of digits before the decimal point
    # nzero - number of zeros after the decimal point
    # nafter - number of digits after the decimal point
    # nzero_real - number of zeros after the decimal point regardles of the precision

    # Some hacks to change None to -1 (C convention)
    if w is None:
        w = -1
    if e is None:
        e = -1
    nzero_real = -1
    sign = _calculate_sign(state, sign_bit)
    # Some debug
    if d != 0:
        assert(buff[2] in ['.', ','])
        assert(buff[ndigits + 2] == 'e')
    # Read in the exponent
    ex = int(buff[ndigits + 3:]) + 1
    # Handle zero case
    if zero_flag:
        ex = 0
        if SIGN_ZERO:
            sign = _calculate_sign(state, sign_bit)
        else:
            sign = _calculate_sign(state, False)
        # Handle special case
        if w == 0:
            w = d + 2
        # This case does not include a decimal point
        if (w == 1) and (ft == 'F'):
            return '.' # CHANGED: Was '0'
    # Get rid of the decimal and the initial sign i.e. normalise the digits
    digits = buff[1] + buff[3:]
    # Find out where to place the decimal point
    if ft == 'F':
        nbefore = ex + state['scale']
        if nbefore < 0:
            nzero = -nbefore
            nzero_real = nzero
            if nzero > d:
                nzero = d
            nafter = d - nzero
            nbefore = 0
        else:
            nzero = 0
            nafter = d
        expchar = None
    elif ft in ['E', 'D']:
        i = state['scale']
        if (d <= 0) and (i == 0):
            raise InvalidFormat("Precision not greater than zero in format specifier 'E' or 'D'")
        if (i <= -d) or (i >= (d + 2)):
            raise InvalidFormat("Scale factor out of range in format specifier 'E' or 'D'")
        if not zero_flag:
            ex = ex - i
        if i < 0:
            nbefore = 0
            nzero = -i;
            nafter = d + i
        elif i > 0:
            nbefore = i
            nzero = 0
            nafter = (d - i) + 1
        else:
            nbefore = 0
            nzero = 0
            nafter = d
        expchar = ft
    elif ft == 'EN':
        # Exponent must be a multiple of 3 with 1-3 digits before the d.p
        if not zero_flag:
            ex = ex - 1
        if ex >= 0:
            nbefore = ex % 3
        else:
            nbefore = (-ex) % 3
            if nbefore != 0:
                nbefore = 3 - nbefore
        ex = ex - nbefore
        nbefore = nbefore + 1
        nzero = 0
        nafter = d
        expchar = 'E'
    elif ft == 'ES':
        if not zero_flag:
            ex = ex - 1
        nbefore = 1
        nzero = 0
        nafter = d
        expchar = 'E'
    # Round the value
    if (nbefore + nafter) == 0:
        ndigits = 0
        if (nzero_real == d) and (int(digits[0]) >= 5): # n.b. character comparison not very pythonic!
            # We rounded to zero but shouldn't have
            nzero = nzero - 1
            nafter = 1
            digits = '1' + digits[1:]
            ndigits = 1
    elif (nbefore + nafter) < ndigits:
        ndigits = nbefore + nafter
        i = ndigits
        if int(digits[i]) >= 5:
            # Propagate the carry
            i = i - 1
            while i >= 0:
                digit = int(digits[i])
                if digit != 9:
                    digits = _swapchar(digits, i, str(digit + 1))
                    break
                else:
                    digits = _swapchar(digits, i, '0')
                i = i - 1
            # Did the carry overflow?
            if i < 0:
                digits = '1' + digits
                if ft == 'F':
                    if nzero > 0:
                        nzero = nzero - 1
                        nafter = nafter + 1
                    else:
                        nbefore = nbefore + 1
                elif ft == 'EN':
                    nbefore = nbefore + 1
                    if nbefore == 4:
                        nbefore = 1
                        ex = ex + 3
                else:
                    ex = ex + 1
    # Calculate the format of the exponent field
    if expchar is not None:
        # i = abs(ex)
        # while i >= 10:
        #     edigits = edigits + 1
        #     i = i / 10.0
        if e < 0:
            # Width not specified, must be no more than 3 digits
            if (ex > 999) or (ex < -999):
                edigits = -1
            else:
                edigits = 4
                if (ex > 99) or (ex < -99):
                    expchar = ' '
        else:
            assert(isinstance(ex, int))
            edigits = len(str(abs(ex)))
            # Exponenet width specified, check it is wide enough
            if edigits > e:
                edigits = -1
            else:
                edigits = e + 2
    else:
        edigits = 0
    # Zero values always output as positive, even if the value was egative before rounding
    i = 0
    while i < ndigits:
        if digits[i] != '0':
            break
        i = i + 1
    if i == ndigits:
        # The output is zero so set sign accordingly
        if SIGN_ZERO:
            sign = _calculate_sign(state, sign_bit)
        else:
            sign = _calculate_sign(state, False)
    # Pick a field size if none was specified
    if w <= 0:
        w = nbefore + nzero + nafter + 1 + len(sign)
    # Work out how much padding is needed
    nblanks = w - (nbefore + nzero + nafter + edigits + 1)
    if sign != '':
        nblanks = nblanks - 1
    # TODO: Find out what this is
    if G0_NO_BLANKS: # dtp->u.p.g0_no_blanks
        w = w - nblanks
        nblanks = 0
    # Check value fits in specified width
    if (nblanks < 0) or (edigits == -1): 
        return '*' * w
    # See if we have space for a zero before the decimal point
    if (nbefore == 0) and (nblanks > 0):
        leadzero = True
        nblanks = nblanks - 1
    else:
        leadzero = False
    out = ''
    # Pad to full field width
    if (nblanks > 0) and not state['collapse_blanks']: # dtp->u.p.no_leading_blank
        out = out + ' ' * nblanks
    # Attach the sign
    out = out + sign
    # Add the lead zero if necessary
    if leadzero:
        out = out + '0'
    # Output portion before the decimal point padded with zeros
    if nbefore > 0:
        if nbefore > ndigits:
            out = out + digits[:ndigits] + (' ' * (nbefore - ndigits))
            digits = digits[ndigits:]
            ndigits = 0
        else:
            i = nbefore
            out = out + digits[:i]
            digits = digits[i:]
            ndigits = ndigits - i
    # Output the decimal point
    out = out + DECIMAL_CHAR
    # Output the leading zeros after the decimal point
    if nzero > 0:
        out = out + ('0' * nzero)
    # Output the digits after the decimal point, padded with zeros
    if nafter > 0:
        if nafter > ndigits:
            i = ndigits
        else:
            i = nafter
        zeros = '0' * (nafter - i)
        out = out + digits[:i] + zeros
        digits = digits[nafter:]
        ndigits = ndigits - nafter
    # Output the exponent
    if expchar is not None:
        if expchar != ' ':
            out = out + expchar
            edigits = edigits - 1
        fmt = '%+0' + str(edigits) + 'd'
        tmp_buff = fmt % ex
        if not state['collapse_blanks']:
            tmp_buf = tmp_buff + (nblanks * ' ')
        out = out + tmp_buff
    return out


def _calculate_sign(state, negative_flag):
    s = ''
    if negative_flag:
        s = '-'
    elif state['incl_plus']:
        s = '+'
    else:
        s = ''
    return s

def _swapchar(s, ind, newch):
    '''
    Helper function to make chars in a string mutableish
    '''
    if 0 < ind >= len(s):
        raise IndexError('index out of range')
    return s[:ind] + newch + s[ind+1:]
    

def _compose_a_string(w, state, val):
    # f77 spec 13.5.11 covers a editing
    val = str(val)
    if w is None:
        output = val
    elif w >= len(val):
        output = val.rjust(w)
    else:
        output = val[:w]
    return output


def _compose_l_string(w, state, val):
    # f77 spec 13.5.10 covers l editing
    try:
        val = bool(val)
    except ValueError:
        raise ValueError("cannot convert '%s' to a boolean" % str(val))
    # single t or f
    if val == True:
        sub_string = 'T'
    else:
        sub_string = 'F'
    # now pad to the specified width
    sub_string = sub_string.rjust(w)
    return sub_string


def _compose_i_string(w, d, state, val):
    # f77 spec 13.5.9.1 covers integer editing 
    null_field = False
    # be pythonic in what values to accept, if it looks like an integer, then
    # so be it
    try:
        val = int(val)
    except ValueError:
        raise ValueError("cannot convert '%s' to a integer" % str(val))
    # get the basic string without sign etc.
    int_string = '%d' % int(round(math.fabs(val)))
    # pad if necessary
    if d is not None:
        int_string = int_string.rjust(d, '0')
        # weird case where if zero width specified and is zero, can have zero space
        if (val == 0) and (d == 0):
            int_string = ''
    # prepend the sign
    int_string = _get_sign(val, state['incl_plus']) + int_string
    # fill the field with blanks if the number takes more room than the width
    # see f77 spec 13.5.9 remark 5.
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

def _compose_boz_string(w, m, state, val, ftype):
    try:
        val = int(val)
    except ValueError:
        raise ValueError("Cannot convert %s to an integer" % str(val))
    # Special case for zero
    if val == 0:
        if m is None:
            return '0'.rjust(w)
        elif w == m == 0:
            return ' '
        elif m == 0:
            return w * ' '
        else:
            s = '0'.rjust(m, '0').rjust(w, ' ')
            if len(s) > w:
                return w * '*'
    # Normal cases
    s = ''
    if ftype == 'B':
        # Binary case
        if val < 0:
            return '*' * w
        while val > 0:
            s = str(val % 2) + s
            val = val >> 1
    elif ftype == 'O':
        # Octal case
        if val < 0:
            return '*' * w
        s = '%o' % val
    elif ftype == 'Z':
        # Hex case
        # Fortran uses Two's complement to represent negative numbers, this
        # restricts hex values to sys.maxint, if greater than this overflow,
        # however this is not perfoect as sys.maxint is Pythons build maximum
        # rather than the systems bit size which is difficult to find reliably
        # across platforms
        if abs(val) > sys.maxint:
            return '*' * w
        if val < 0:
            s = '%X' % ((sys.maxint * 2) + 2 + val)
        else:
            s = '%X' % val
    if m is None:
        s = s.rjust(w)
    else:
        s = s.rjust(m, '0').rjust(w)
    if len(s) > w:
        return w * '*'
    else:
        return s

def _write_string(record, sub_string, pos):
    '''Function that actually writes the generated strings to a 'stream'''''
    new_pos = pos + len(sub_string)
    # pad if required with blanks - i.e. input after a tr edit descriptor - see
    # f77 format sec. 13.5.3
    if pos > len(record):
        record = record.ljust(pos, ' ')
        out =  record + sub_string
    elif pos == len(record):
        out = record + sub_string
    elif pos < len(record):
        out = record[:pos] + sub_string + record[new_pos:]
    return (new_pos, out)


# allow for self testing
if __name__ == '__main__':
    # from IPython.Debugger import Tracer; here = Tracer()
    import doctest
    import os
    from _parser import parser
    from _lexer import lexer
    FULL_DEBUG = True
    TEST_PATH = os.path.join('tests', 'samples', 'gfortran', '4-4-1_osx_intel')
    globs = {
        '_write_string' : _write_string,
        '_get_sign' : _get_sign,
        'parser' : parser,
        'lexer' : lexer,
        'output' : output,
    }
    # need to normalize whitespace since pasting into vim converts tabs to
    # spaces
    if FULL_DEBUG:
        # Manually coded tests
        doctest.testfile(os.path.join('tests', 'output_write_string_test.txt'), \
            globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        doctest.testfile(os.path.join('tests', 'output_get_sign_test.txt'), \
            globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # Automatically generated tests
        # doctest.testfile(os.path.join(TEST_PATH, 'bn-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'bz-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'slash-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'sp-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'ss-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 't-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'tl-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'tr-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'x-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'colon-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'a-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        doctest.testfile(os.path.join(TEST_PATH, 'b-output-test.txt'), \
            globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'd-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'en-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'es-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'e-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'f-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'g-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'i-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'l-output-test.txt'), \
            # globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        doctest.testfile(os.path.join(TEST_PATH, 'o-output-test.txt'), \
            globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        doctest.testfile(os.path.join(TEST_PATH, 'z-output-test.txt'), \
            globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'bn-a-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'bn-b-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'bn-d-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'bn-en-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'bn-es-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'bn-e-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'bn-f-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'bn-g-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'bn-i-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'bn-l-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'bn-o-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'bn-z-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'bn-slash-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'bz-a-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'bz-b-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'bz-d-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'bz-en-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'bz-es-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'bz-e-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'bz-f-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'bz-g-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'bz-i-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'bz-l-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'bz-o-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'bz-z-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'bz-slash-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'slash-a-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'slash-b-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'slash-d-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'slash-en-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'slash-es-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'slash-e-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'slash-f-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'slash-g-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'slash-i-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'slash-l-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'slash-o-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'slash-z-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'slash-slash-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'sp-a-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'sp-b-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'sp-d-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'sp-en-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'sp-es-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'sp-e-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'sp-f-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'sp-g-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'sp-i-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'sp-l-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'sp-o-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'sp-z-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'sp-slash-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'ss-a-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'ss-b-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'ss-d-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'ss-en-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'ss-es-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'ss-e-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'ss-f-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'ss-g-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'ss-i-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'ss-l-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'ss-o-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'ss-z-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'ss-slash-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 't-a-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 't-b-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 't-d-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 't-en-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 't-es-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 't-e-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 't-f-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 't-g-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 't-i-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 't-l-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 't-o-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 't-z-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 't-slash-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'tl-a-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'tl-b-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'tl-d-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'tl-en-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'tl-es-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'tl-e-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'tl-f-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'tl-g-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'tl-i-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'tl-l-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'tl-o-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'tl-z-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'tl-slash-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'tr-a-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'tr-b-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'tr-d-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'tr-en-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'tr-es-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'tr-e-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'tr-f-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'tr-g-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'tr-i-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'tr-l-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'tr-o-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'tr-z-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'tr-slash-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'x-a-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'x-b-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'x-d-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'x-en-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'x-es-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'x-e-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'x-f-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'x-g-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'x-i-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'x-l-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'x-o-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'x-z-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'x-slash-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'colon-a-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'colon-b-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'colon-d-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'colon-en-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'colon-es-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'colon-e-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'colon-f-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'colon-g-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'colon-i-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'colon-l-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'colon-o-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'colon-z-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
        # doctest.testfile(os.path.join(TEST_PATH, 'colon-slash-output-test.txt'), \
        #     globs=globs, optionflags=doctest.NORMALIZE_WHITESPACE)
    else:
        e, res = parser(lexer('''(G10.5E5)'''))
        vals = [-0.0001]
        here()
        print "[" + output(e, res, vals) + "]"

