class Colon(object):
    def __init__(self):
        pass
    def input(self, record, state):
        return (None, state)
    def output(self, record, value, state):
        state['repeat_val'] = True
        return (record, state)
    def __repr__(self):
        return '<Colon>'
    
