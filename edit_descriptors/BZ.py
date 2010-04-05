class BZ(object):
    def __init__(self):
        pass
    def input(self, record, state):
        state['ignore_blanks'] = False
        return (None, state)
    def output(self, record, char_string, state):
        state['repeat_val'] = True
        state['ignore_blanks'] = False
        # No effect on ouptut
        return (record, state)
