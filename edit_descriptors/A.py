class A(object):
    def __init__(self):
        self.repeat = None
        self.width = None
    def input(self, record, state):
        position = state['position']
        if self.width == None:
            # Since the length of the input string is unknown from the format
            # alone, the width must be specified separately
            # TODO: Work out warning/error system
            raise Exception()
        final_position = position + self.width
        value = record[position:final_position]
        state['position'] = final_position
        return (value, state)
    def output(self, record, char_string, state):
        position = state['position']
        if self.width == None:
            self.width = len(char_string)
        char_string = char_string[:self.width].rjust(self.width)
        final_position = position + len(char_string)
        if final_position >= len(record):
            record = record[:position] + char_string
        else:
            record = record[:position] + char_string + record[final_position:]
        state['position'] = final_position
        return (record, state)
    def __repr__(self):
        return '<A repeat=' + str(self.repeat) + \
                ' width=' + str(self.width) + \
                '>'
    
