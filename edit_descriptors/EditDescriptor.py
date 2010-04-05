class EditDescriptor(object):
    def __init__(self, type=None, repeat=None, width=None, \
            decimal_places=None, padding=None, exponent=None, \
            num_chars=None, char_string=None):
        self.type = type
        self.repeat = repeat
        self.width = width
        self.decimal_places = decimal_places
        self.padding = padding
        self.exponent = exponent
        self.num_chars = num_chars
        self.char_string = char_string
