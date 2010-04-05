class StringLiteral(object):
    def __init__(self):
        self.char_string = None
    def input(self, record, state):
        if self.char_string == None:
            # TODO: Raise a better error
            raise Exception()
        position = state['position']
        final_position = position + len(self.char_string)
        value = record[position:final_position]
        if value != self.char_string:
            # TODO: Raise a better error
            raise Exception()
        state['position'] = final_position
        return (value, state)
    def output(self, record, value, state):
        if self.char_string == None:
            # TODO: Raise a better error
            raise Exception()
        position = state['position']
        final_position = position + len(self.char_string)
        if final_position >= len(record):
            record = record[:position] + self.char_string
        else:
            record = record[:position] + self.char_string + record[final_position:]
        state['position'] = final_position
        state['repeat_val'] = True
        return (record, state)
        
