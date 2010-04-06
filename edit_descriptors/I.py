class I(object):
    def __init__(self):
        self.repeat = None
        self.width = None
        self.padding = None
    def input(self):
        pass
    def output(self, var=None):
        pass
    def __repr__(self):
        return '<I repeat=' + str(self.repeat) + \
                ' width=' + str(self.width) + \
                ' padding=' + str(self.padding) + \
                '>'
    
