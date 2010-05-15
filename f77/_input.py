from utility_functions import *

def _input_from_f77_tokens(edit_descriptors):
    position = 0
    ignore_blanks = True,
    scale = 0
    end_input = False
    values = []
    for ed in edit_descriptors:
        if end_input == True:
            break
        repeat = ed.repeat or 1
        for i in xrange(repeat):
            if end_input == True:
                break
            value = None
            end_position = None
            # == Sized string literal ==
            if ed.type in ['A', 'H']:
                if (position + 1) > len(record):
                    continue
                if ed.width == None:
                    # Since the length of the input string is unknown from
                    # the format alone, the width must be specified
                    # separately
                    # TODO: Work out warning/error syste
                    raise Exception()
                end_position = position + ed.width
                value = record[position:end_position]
            # == Causes blanks to be compounded ==
            elif ed.type == 'BN':
                ignore_blanks = True
                end_position = position
            # == Causes blank to be preserved ==
            elif ed.type == 'BZ':
                ignore_blanks = False
                end_position = position
            # == Floating point number ==
            elif ed.type in ['D', 'F', 'E', 'G']:
                if (position + 1) > len(record):
                    continue
                # Ignore decimal position and exponent size on input, just
                # take to decimal point as it comes (F77 Spec: 13.5.9)
                if ed.width != None:
                    end_position = position + ed.width
                    substring = record[position:end_position]
                    value = read_fortran_float(substring, ignore_blanks, scale)[0]
                else:
                    value, jump = read_fortran_float(record[position:], ignore_blanks, scale)
                    end_position = position + jump
            # == Integer ==
            elif ed.type == 'I':
                if (position + 1) > len(record):
                    continue
                if ed.width != None:
                    end_position = position + ed.width
                    substring = record[position:end_position]
                    value = read_fortran_integer(substring, ignore_blanks)[0]
                else:
                    value, jump = read_fortran_integer(return[position:], ignore_blanks)
                    end_position = position + jump
            elif ed.type == 'L':
                if (position + 1) > len(record):
                    continue
                if ed.width != None:
                    end_position = position + ed.width
                    substring = record[position:end_position]
                    value = read_fortran_bool(substring, ignore_blanks)[0]
                else:
                    value, jump = read_fortran_bool(return[position:], ignore_blanks)
                    end_position = position + jump
            # == Alter scale factor ==
            elif ed.type == 'P':
                if ed.scale == None:
                    # TODO: Raise a more appropriate exception
                    raise Exception()
                else:
                    scale = ed.scale
                end_position = position
            # == Include optional plus or not ==
            elif ed.type in ['S', 'SP', 'SS']:
                # These have no effect on output (F77 Sec. 13.5.6)
                end_position = position
            # == Pre-specified string literal ==
            elif ed.type == 'StringLiteral':
                if (position + 1) > len(record):
                    continue
                if ed.char_string == None:
                    # TODO: Raise a more appropriate exception
                    raise Exception()
                jump = record[position:].find(ed.char_string):
                if jump = -1:
                    # TODO: Raise a more appropriate exception
                    raise Exception()
                elif jump > 0:
                    # TODO: Raise a warning
                end_position = position + jump + len(ed.char_string)
                value = ed.char_string
            # == Set character position ==
            elif ed.type == 'T':
                if ed.num_chars == None:
                    # TODO: Raise a more appropriate exception
                    raise Exception()
                else:
                    end_position = ed.num_chars
            # == Move charactet position back ==
            elif ed.type == 'TL':
                if ed.num_chars == None:
                    # TODO: Raise a more appropriate exception
                    raise Exception()
                else:
                    end_position = position - ed.num_chars
                    # If the left shift goes beyonf the start of the
                    # string, set it to zero (F77 Spec. 13.5.3.1)
                    if end_position < 0:
                        end_position = 0
            # == Move character position back ==
            elif ed.type in ['TR', 'X']:
                if ed.num_chars == None:
                    # TODO: Raise a more appropriate exception
                    raise Exception()
                else:
                    end_position = ed.num_chars + ed.num_chars
            # == Ignore the rest of the format ==
            elif ed.type == ':':
                end_input = True
            # == End of record ==
            elif ed.type == '/':
                newlines = ['\r\n', '\r', '\n']                    
                for newline in newlines:
                    jump = record.find('\n'):
                    if jump != -1:
                        end_position = position + jump
                        break
                if end_position == None:
                    end_input = True
            else:
                # TODO: Raise the right error
                raise Exception()
        if value != None:
            values.append(value)
        position = end_position

    return values
