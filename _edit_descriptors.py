# All the tokens defined in the F77 specification unless specified

class A(object):
    def __init__(self):
        self.repeat = None
        self.width = None
    def __repr__(self):
        return '<A repeat=' + str(self.repeat) + \
                ' width=' + str(self.width) + '>'

class Apostrophe(object):
    def __init__(self):
        self.char_string = None
    def __repr__(self):
        return '<Apostrophe char_string=' + str(self.char_string) + '>'

# Only in F95
class B(object):
    def __init__(self):
        self.repeat = None
        self.width = None
        self.min_digits = None
    def __repr__(self):
        return '<B repeat=' + str(self.repeat) + \
                ' width=' + str(self.width) + \
                ' min_digits=' + str(self.min_digits) + '>'
    
class BN(object):
    def __init__(self):
        pass
    def __repr__(self):
        return '<BN>'

class BZ(object):
    def __init__(self):
        pass
    def __repr__(self):
        return '<BZ>'

class Colon(object):
    def __init__(self):
        pass
    def __repr__(self):
        return '<Colon>'
    
class D(object):
    def __init__(self):
        self.repeat = None
        self.width = None
        self.decimal_places = None
    def __repr__(self):
        return '<D repeat=' + str(self.repeat) + \
                ' width=' + str(self.width) + \
                ' decimal_places=' + str(self.decimal_places) + '>'

class E(object):
    def __init__(self):
        self.repeat = None
        self.width = None
        self.decimal_places = None
        self.exponent = None
    def __repr__(self):
        return '<E repeat=' + str(self.repeat) + \
                ' width=' + str(self.width) + \
                ' decimal_places=' + str(self.decimal_places) + \
                ' exponent=' + str(self.exponent) + '>'
    
# Only in F95
class EN(object):
    def __init__(self):
        self.repeat = None
        self.width = None
        self.decimal_places = None
        self.exponent = None
    def __repr__(self):
        return '<EN repeat=' + str(self.repeat) + \
                ' width=' + str(self.width) + \
                ' decimal_places=' + str(self.decimal_places) + \
                ' exponent=' + str(self.exponent) + '>'

# Only in F95
class ES(object):
    def __init__(self):
        self.repeat = None
        self.width = None
        self.decimal_places = None
        self.exponent = None
    def __repr__(self):
        return '<ES repeat=' + str(self.repeat) + \
                ' width=' + str(self.width) + \
                ' decimal_places=' + str(self.decimal_places) + \
                ' exponent=' + str(self.exponent) + '>'

class F(object):
    def __init__(self):
        self.repeat = None
        self.width = None
        self.decimal_places = None
    def __repr__(self):
        return '<F repeat=' + str(self.repeat) + \
                ' width=' + str(self.width) + \
                ' decimal_places=' + str(self.decimal_places) + '>'
    
class FormatGroup(object):
    pass

class G(object):
    def __init__(self):
        self.repeat = None
        self.width = None
        self.decimal_places = None
        self.exponent = None
    def __repr__(self):
        return '<G repeat=' + str(self.repeat) + \
                ' width=' + str(self.width) + \
                ' decimal_places=' + str(self.decimal_places) + \
                ' exponent=' + str(self.exponent) + '>'

# Only in F77
class H(object):
    def __init__(self):
        self.num_chars = None
        self.char_string = None
    def __repr__(self):
        return '<H num_chars=' + str(self.num_chars) + \
                ' char_string=' + str(self.char_string) + '>'
    
class I(object):
    def __init__(self):
        self.repeat = None
        self.width = None
        self.min_digits = None
    def __repr__(self):
        return '<I repeat=' + str(self.repeat) + \
                ' width=' + str(self.width) + \
                ' min_digits=' + str(self.min_digits) + '>'
    
class L(object):
    def __init__(self):
        self.repeat = None
        self.width = None
    def __repr__(self):
        return '<L repeat=' + str(self.repeat) + \
                ' width=' + str(self.width) + '>'

# Only in F95
class O(object):
    def __init__(self):
        self.repeat = None
        self.width = None
        self.min_digits = None
    def __repr__(self):
        return '<O repeat=' + str(self.repeat) + \
                ' width=' + str(self.width) + \
                ' min_digits=' + str(self.min_digits) + '>'

class P(object):
    def __init__(self):
        self.scale = None
    def __repr__(self):
        return '<P scale=' + str(self.scale) + '>'
    
class S(object):
    def __init__(self):
        pass
    def __repr__(self):
        return '<S>'
    
class Slash(object):
    def __init__(self):
        pass
    def __repr__(self):
        return '<Slash>'
    
class SP(object):
    def __init__(self):
        pass
    def __repr__(self):
        return '<SP>'
    
class SS(object):
    def __init__(self):
        pass
    def __repr__(self):
        return '<SS>'
    
class T(object):
    def __init__(self):
        self.num_chars = None
    def __repr__(self):
        return '<T num_chars=' + str(self.num_chars) + '>'
    
class TL(object):
    def __init__(self):
        self.num_chars = None
    def __repr__(self):
        return '<TL num_chars=' + str(self.num_chars) + '>'
    
class TR(object):
    def __init__(self):
        self.num_chars = None
    def __repr__(self):
        return '<TR num_chars=' + str(self.num_chars) + '>'

class X(object):
    def __init__(self):
        self.num_chars = None
    def __repr__(self):
        return '<X num_chars=' + str(self.num_chars) + '>'

# Only in F95
class Z(object):
    def __init__(self):
        self.repeat = None
        self.width = None
        self.min_digits = None
    def __repr__(self):
        return '<Z repeat=' + str(self.repeat) + \
                ' width=' + str(self.width) + \
                ' min_digits=' + str(self.min_digits) + '>'

