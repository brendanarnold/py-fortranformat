class BN(object):
    def __init__(self):
        pass
    def input(self, record, state):
        state['ignore_blanks'] = True
        return (None, state)
    def output(self, record, char_string, state):
        state['repeat_val'] = True
        state['ignore_blanks'] = True
        # No effect on ouptut
        return (record, state)
    def __repr__(self):
        return '<BN>'

