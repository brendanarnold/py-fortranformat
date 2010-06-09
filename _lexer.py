from _edit_descriptors import *

# Some lexer tokens to look out for
DIGITS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
SIGNS = ['+', '-']
COMMA = [',']
DOT = ['.']
WHITESPACE = [' ', '\t', '\n']
QUOTE_CHARS = ['"', "'"]
DOUBLE_EDIT_DESCRIPTORS = ['EN', 'ES', 'TR', 'TL', 'BN', 'BZ', 'SP', 'SS']
SINGLE_EDIT_DESCRIPTORS = ['A', 'B', 'D', 'E', 'F', 'G', 'I', 'L', 'O', 'Z']
H_EDIT_DESCRIPTOR = ['H']
LEFT_PARENS = ['(']
RIGHT_PARENS = [')']

def _lexer(format):
    '''L the FORTRAN format statement into tokens'''
    tokens = []
    s = -1
    h_chars = None
    while True:
        # Get the next set of characters
        s = s + 1
        c0, c1, c2 = _get_chars(format, s)
        # If at end of format, end it all - aieee!
        if c0 is None:
            break
        # Read in an H edit descriptor string
        elif h_chars is not None:
            buff = format[s:s+h_chars]
            tokens.append(Token('H_STRING', buff))
            s = s + (h_chars - 1)
            h_chars = None
        # Skip whitespace
        elif c0 in WHITESPACE:
            continue
        # Read in a quoted string
        elif c0 in QUOTE_CHARS:
            buff = ''
            delim = c0
            while True:
                s = s + 1
                c0, c1, c2 = _get_chars(format, s)
                # Check if an escaped delimiter
                if (c0 == delim) and (c1 == delim):
                    s = s + 1
                    buff = buff + delim
                elif (c0 == delim):
                    break
                elif c0 is None:
                    # Premature end of format
                    raise InvalidFormat('Premature end of quoted string in format')
                else:
                    buff = buff + c0
            tokens.append(Token('QUOTED_STRING', buff))
        # Read in an integer
        elif c0 in DIGITS + SIGNS:
            # Check sign followed by at least one digit
            if (c0 in SIGNS) and (c1 not in DIGITS):
                # TODO: Is whitesapce allowed between sign and digit?
                raise InvalidFormat("Orphaned sign '%s' with no digits at position %d" % (c0, s))
            buff = c0
            while True:
                s = s + 1
                c0, c1, c2 = _get_chars(format, s)
                if (c0 not in DIGITS) or (c0 is None):
                    break
                else:
                    buff = buff + c0
            s = s - 1
            val = int(buff)
            if buff[0] in SIGNS:
                tokens.append(Token('SIGNED_INT', val))
            else:
                tokens.append(Token('UNSIGNED_INT', val))
        # Read in a comma
        elif c0 in COMMA:
            tokens.append(Token('COMMA', None))
        # Read in a dot
        elif c0 in DOT:
            tokens.append(Token('DOT', None))
        # Read in double lettered edit descriptors
        elif (c0 + c1).upper() in DOUBLE_EDIT_DESCRIPTORS:
            tokens.append(Token('EDIT_DESCRIPTOR', (c0 + c1).upper()))
            s = s + 1
        # Read in an H edit descriptor
        elif c0.upper() in H_EDIT_DESCRIPTOR:
            if (len(tokens) > 0) and (tokens[-1].type == 'UNSIGNED_INT'):
                h_chars = tokens[-1].value
                tokens.append(Token('H_EDIT_DESCRIPTOR', c0.upper()))
            else:
                raise InvalidFormat("Missing H descriptor number argument at position %d" % s)
        # Read in single lettered edit descriptors
        elif c0.upper() in SINGLE_EDIT_DESCRIPTORS:
            tokens.append(Token('EDIT_DESCRIPTOR', c0.upper()))
        # Read in left parens
        elif c0 in LEFT_PARENS:
            tokens.append(Token('LEFT_PARENS', None))
        # Read in right parens
        elif c0 in RIGHT_PARENS:
            tokens.append(Token('RIGHT_PARENS', None))
        else:
            raise InvalidFormat('Character %s not recognised at position %d' % (c0, s))
    return tokens

def _parser(tokens):
    # TODO:
    pass

def _get_chars(format, s):
    try:
        c0 = format[s]
    except IndexError:
        c0 = None
    try:
        c1 = format[s+1]
    except IndexError:
        c1 = None
    try:
        c2 = format[s+2]
    except IndexError:
        c2 = None
    return (c0, c1, c2)

class InvalidFormat(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class Token(object):
    def __init__(self, type, value):
        self.type = type
        self.value = value
    def __repr__(self):
        return "\n  Token: type=%s,\tvalue=%s" % (self.type, str(self.value))

class ParserState(object):
    '''Struct-like object to store state'''
    def __init__(self):
        self.quoted = False
        self.pos = 0
        self.new_token = True

def get_token(name):
    name = name.upper()
    if name == 'A':
        return A()
    elif name == 'BN':
        return BN()
    elif name == 'BZ':
        return BZ()
    elif name == ':':
        return Colon()
    elif name == 'D':
        return D()
    elif name == 'E':
        return E()
    elif name == 'F':
        return F()
    elif name == 'G':
        return G()
    elif name == 'H':
        return H()
    elif name == 'I':
        return I()
    elif name == 'L':
        return L()
    elif name == 'P':
        return P()
    elif name =='S':
        return S()
    elif name == '/':
        return Slash()
    elif name == 'SP':
        return SP()
    elif name == 'SS':
        return SS()
    elif name == 'T':
        return T()
    elif name == 'TL':
        return TL()
    elif name == 'TR':
        return TR()
    elif name == 'X':
        return X()
    else:
        return None

if __name__ == '__main__':
    print _lexer("3hdef-3   'df'' \"g\"ggg',(3 )I4 ")

