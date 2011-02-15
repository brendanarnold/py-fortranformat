from _edit_descriptors import *
import re

WIDTH_OPTIONAL_EDS = [A]
NON_WIDTH_EDS = [BN, BZ, P, SP, SS, S, X, T, TR, TL, Colon, Slash]

# Processor dependant default for including leading plus or not
PROC_INCL_PLUS = False 
# Option to allow signed binary, octal and hex on input (not a FORTRAN feature)
PROC_ALLOW_NEG_BOZ = False
# Prcessor dependant padding character
PROC_PAD_CHAR = ' '

# Some problems without pre written input vars:
#   Cannot say when reversion conditions are met
#   Cannot determine width of A edit descriptor
#   Cannot determine complex input
#   Cannot determine proper input for G edit descriptors


def input(eds, reversion_eds, records, num_vals=None):

    state = { \
        'position' : 0,
        'scale' : 0,
        'incl_plus' : False,
        'collapse_blanks' : True,
        'halt_if_no_vals' : False,
        'exception_on_fail' : True,
    }
    
    # Assume one-to-one correspondance between edit descriptors and output
    # values if number of output values is not defined 
    num_out_eds = 0
    for ed in eds:
        if ed in OUTPUT_EDS:
            num_out_eds += 1
    num_rev_out_eds = 0
    if num_vals is None:
        num_vals = num_out_eds
    for ed in reversion_eds:
        if ed in OUTPUT_EDS:
            num_rev_out_eds += 1
    
    # Will loop forever is no output edit descriptors
    if (num_out_eds == 0) and (num_vals > 0):
        return []
    # Will loop forever if no output eds in reversion format and is more values
    # requested than in the format
    if (num_vals > num_out_eds) and (num_rev_out_eds == 0):
        raise ValueError('Not enough output edit descriptors in reversion format to output %d values' % num_vals)

    # May need to process multiple records, down to a higher function to supply
    # appropriate string for format
    if not hasattr(records, 'next'):
        records = iter(re.split('\r\n|\r|\n', records))
    record = _next(records, None)
    
    # if a_widths is not None:
    #     a_widths = itertools.cycle(a_widths)

    vals = []
    finish_up = False
    ed_ind = -1
    while True:
        ed_ind += 1
        # Signal to stop when Colon edit descriptor or end of format or end of
        # reversion format reached. Also not to output any more data
        if len(vals) >= num_vals:
            finish_up = True
        # Select the appropriate edit descriptor
        if ed_ind < len(eds):
            ed = eds[ed_ind]
        else:
            rev_ed_ind = (ed_ind - len(eds)) % len(reversion_eds)
            # Reversion begun and has been instructed to halt
            if finish_up and (rev_ed_ind == 0):
                break
            ed = reversion_eds[rev_ed_ind]

        if isinstance(ed, QuotedString):
            raise InvalidFormat('Cannot have string literal in an input format')
        elif ed in CONTROL_EDS:
            if isinstance(ed, BN):
                state['collapse_blanks'] = True
            elif isinstance(ed, BZ):
                state['collapse_blanks'] = True
            elif isinstance(ed, P):
                state['scale'] = ed.scale
            elif isinstance(ed, SP):
                state['incl_plus'] = True
            elif isinstance(ed, SS):
                state['incl_plus'] = False
            elif isinstance(ed, S):
                state['incl_plus'] = PROC_INCL_PLUS
            elif isinstance(ed, (X, TR)):
                state['position'] += ed.num_chars
            elif isinstance(ed, TL):
                state['position'] = max(state['position'] - ed.num_chars, 0)
            elif isinstance(ed, T):
                state['position'] = max(ed.num_chars, 0)
            elif isinstance(ed, Slash):
                # End of record
                record = _next(records, None)
                if record is None:
                    break
            elif isinstance(ed, Colon):
                # Break if input value satisfied
                if finish_up:
                    break
        elif ed in OUTPUT_EDS:
            if isinstance(ed, A) and (ed.width is None):
                # Cannot get width of A edit descripor from allocated input
                # array so must use specified widths, or failing that the rest
                # of the record
                # if a_widths is not None:
                #     ed.width = _next(a_widths, None)
                # if ed.width is None:
                #     ed.width = max(len(record) - state['position'], 0)
                raise NotImplemented('Cannot guess width of character input for A edit descriptor, please supply the width')
            substr, state = _get_substr(ed.width, record, state)
            if isinstance(ed, (Z, O, B, I)):
                if ('-' in substr) and (not PROC_ALLOW_NEG_BOZ) and isinstance(ed, (Z, O, B)):
                    if state['exception_on_fail']:
                        raise ValueError('Negative numbers not permitted for binary, octal or hex')
                    else:
                        vals.append(None)
                        continue
                if isinstance(ed, Z):
                    base = 16
                elif isinstance(ed, I):
                    base = 10
                elif isinstance(ed, O):
                    base = 8
                elif isinstance(ed, B):
                    base = 2
                teststr = _interpret_blanks(substr, state)
                try:
                    val = int(teststr, base)
                except ValueError:
                    if state['exception_on_fail']:
                        raise ValueError('%s is not a valid input for one of integer, octal, hex or binary' % substr)
                    else:
                        vals.append(None)
                        continue
                vals.append(val)
            elif isinstance(ed, A):
                vals.append(substr.rjust(PROC_PAD_CHAR))
            elif isinstance(ed, L):
                # Remove preceding whitespace and take the first two letters as
                # uppercase for testing
                teststr = substr.upper().lstrip().lstrip('.')[0]
                if teststr == 'T':
                    vals.append(True)
                elif teststr == 'F':
                    vals.append(False)
                else:
                    if state['exception_on_fail']:
                        raise ValueError('%s is not a valid boolean input' % substr)
                    else:
                        vals.append(None)
            elif isinstance(ed, (E, D, EN, ES)):
                teststr = _interpret_blanks(substr, state)
                # Python only understands 'E' as an exponential letter
                teststr = teststr.upper().replace('D', 'E')
                # Prepend an exponential letter if only a '-' or '+' denotes an exponent
                if 'E' not in teststr:
                    teststr = teststr[0] + teststr[1:].replace('+', 'E+').replace('-', 'E-')
                try:
                    val = float(teststr)
                except ValueError:
                    if state['exception_on_fail']:
                        raise ValueError('%s is not a valid input as for an E, ES, EN or D edit descriptor' % substr)
                    else:
                        vals.append(None)
                        continue
                # Special cases: insert a decimal if none specified
                if ('.' not in teststr) and (ed.decimal_places is not None):
                    val = val / 10 ** ed.decimal_places
                # Apply scale factor if exponent not supplied
                if 'E' not in teststr:
                    val = val / 10 ** state['scale'] 
                vals.append(val) 
            elif isinstance(ed, G):
                # Difficult to know what wanted since do not know type of input variable
                raise NotImplemented('G edit descriptor not implemented for input as cannot guess input type from predifined variable: Use Aw edit descriptor instead and process the string manually')
    return vals[:num_vals]

def _interpret_blanks(substr, state):
    # Save leading blanks
    if state['collapse_blanks']:
        # TODO: Are tabs blank characters?
        substr = substr.replace(' ', '')
    else:
        substr = substr.lstrip(' ')
        substr = substr.replace(' ', '0')
    return substr

def _get_substr(w, record, state):
    start = max(state['position'], 0)
    end = start + w
    if end > len(record):
        substr = ''
        # TODO: test if no chars transmitted, then poition does not change
        w = 0
    else:
        substr = record[start:end]
    state['position'] += w
    return substr, state


def _next(it, default=None):
    try:
        val = it.next()
    except StopIteration:
        val = default
    return default


if __name__ == '__main__':
    import doctest
    import os
    from _parser import parser
    from _lexer import lexer
    from _output import output
    # TEST_PATH = os.path.join('tests', 'samples', 'gfortran', '4-2-1_osx_intel', 'input')
    TEST_PATH = os.path.join('tests', 'samples', 'source')
    globs = {
        'A' : A,
        'E' : E,
        'I' : I,
        'parser' : parser,
        'lexer' : lexer,
        'input' : input,
        'output' : output,
    }
    # doctest.testfile(os.path.join(TEST_PATH, 'bn-input-test-1.txt'), \
    #     globs=globs)
    # doctest.testfile(os.path.join(TEST_PATH, 'bz-input-test-1.txt'), \
    #     globs=globs)
    # doctest.testfile(os.path.join(TEST_PATH, 'slash-input-test-1.txt'), \
    #     globs=globs)
    # doctest.testfile(os.path.join(TEST_PATH, 'sp-input-test-1.txt'), \
    #     globs=globs)
    # doctest.testfile(os.path.join(TEST_PATH, 'ss-input-test-1.txt'), \
    #     globs=globs)
    # doctest.testfile(os.path.join(TEST_PATH, 't-input-test-1.txt'), \
    #     globs=globs)
    # doctest.testfile(os.path.join(TEST_PATH, 'tl-input-test-1.txt'), \
    #     globs=globs)
    # doctest.testfile(os.path.join(TEST_PATH, 'tr-input-test-1.txt'), \
    #     globs=globs)
    # doctest.testfile(os.path.join(TEST_PATH, 'x-input-test-1.txt'), \
    #     globs=globs)
    # doctest.testfile(os.path.join(TEST_PATH, 'colon-input-test-1.txt'), \
    #     globs=globs)
    # doctest.testfile(os.path.join(TEST_PATH, 'a-input-test-1.txt'), \
    #     globs=globs)
    doctest.testfile(os.path.join(TEST_PATH, 'b-input-test-1.txt'), \
        globs=globs)
    # doctest.testfile(os.path.join(TEST_PATH, 'b-input-test-2.txt'), \
    #     globs=globs)
    # doctest.testfile(os.path.join(TEST_PATH, 'd-input-test-1.txt'), \
    #     globs=globs)
    # doctest.testfile(os.path.join(TEST_PATH, 'en-input-test-1.txt'), \
    #     globs=globs)
    # doctest.testfile(os.path.join(TEST_PATH, 'en-input-test-2.txt'), \
    #     globs=globs)
    # doctest.testfile(os.path.join(TEST_PATH, 'en-input-test-3.txt'), \
    #     globs=globs)
    # doctest.testfile(os.path.join(TEST_PATH, 'en-input-test-4.txt'), \
    #     globs=globs)
    # doctest.testfile(os.path.join(TEST_PATH, 'es-input-test-1.txt'), \
    #     globs=globs)
    # doctest.testfile(os.path.join(TEST_PATH, 'es-input-test-2.txt'), \
    #     globs=globs)
    # doctest.testfile(os.path.join(TEST_PATH, 'es-input-test-3.txt'), \
    #     globs=globs)
    # doctest.testfile(os.path.join(TEST_PATH, 'es-input-test-4.txt'), \
    #     globs=globs)
    # doctest.testfile(os.path.join(TEST_PATH, 'e-input-test-1.txt'), \
    #     globs=globs)
    # doctest.testfile(os.path.join(TEST_PATH, 'e-input-test-2.txt'), \
    #     globs=globs)
    # doctest.testfile(os.path.join(TEST_PATH, 'e-input-test-3.txt'), \
    #     globs=globs)
    # doctest.testfile(os.path.join(TEST_PATH, 'e-input-test-4.txt'), \
    #     globs=globs)
    # doctest.testfile(os.path.join(TEST_PATH, 'f-input-test-1.txt'), \
    #     globs=globs)
    # doctest.testfile(os.path.join(TEST_PATH, 'g-input-test-1.txt'), \
    #     globs=globs)
    # doctest.testfile(os.path.join(TEST_PATH, 'g-input-test-2.txt'), \
    #     globs=globs)
    # doctest.testfile(os.path.join(TEST_PATH, 'g-input-test-3.txt'), \
    #     globs=globs)
    # doctest.testfile(os.path.join(TEST_PATH, 'g-input-test-4.txt'), \
    #     globs=globs)
    # doctest.testfile(os.path.join(TEST_PATH, 'i-input-test-1.txt'), \
    #     globs=globs)
    # doctest.testfile(os.path.join(TEST_PATH, 'i-input-test-2.txt'), \
    #     globs=globs)
    # doctest.testfile(os.path.join(TEST_PATH, 'l-input-test-1.txt'), \
    #     globs=globs)
    # doctest.testfile(os.path.join(TEST_PATH, 'o-input-test-1.txt'), \
    #     globs=globs)
    # doctest.testfile(os.path.join(TEST_PATH, 'o-input-test-2.txt'), \
    #     globs=globs)
    # doctest.testfile(os.path.join(TEST_PATH, 'z-input-test-1.txt'), \
    #     globs=globs)
    # doctest.testfile(os.path.join(TEST_PATH, 'z-input-test-2.txt'), \
    #     globs=globs)
    
