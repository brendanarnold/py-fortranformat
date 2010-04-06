class D(object):
    def __init__(self):
        self.repeat = None
        self.width = None
        self.decimal_places = None
    def input(self):
        pass
    def output(self, var=None):
        pass
    def __repr__(self):
        return '<D repeat=' + str(self.repeat) + \
                ' width=' + str(self.width) + \
                ' decimal_places=' + str(self.decimal_places) + \
                '>'
