
def parse_f77_format(format, text):
    '''
    Parse a Forran string according to the FORTRAN 77 specification found at,
    http://www.fortran.com/fortran/F77_std/rjcnf0001-sh-13.html
    and return a list of parsed values
    '''
    # First need to tokenise the format string
    flags['']
    # First parse off the chaff - see 13.1.2
    format = format.split('(')[1].split(')')[0]
    tokens = []
    string_buffer = ''
    flag = {
        'quoted' : False,
        'escape' : False,
        'skip_chars' : 0,
    }
    for i in range(len(format)):
        # If necessary to skip a character, do so
        if flag['skip_chars'] > 0:
            flag['skip_chars'] = flag['skip_char'] - 1
            continue
        c = format[i]
        if len(format) > c + 1:
            c_next = format[i+1]
        else:
            c_next = ''
        # Start or end a string
        if c == "'":
            # The case of the escaped apostrophe in a string literal
            if flag['quoted'] == True and c_next == "'":
                flag['skip_chars'] = 1
                string_buffer = string_buffer + c
                continue
            flag['quoted'] = not flag['quoted']
            # If come to end of string literal, add to buffer
            if flag['quoted'] == False: 
                tokens.append(string_buffer)
                string_buffer = ''
            continue
        # In a string, add to buffer, important this comes after testing for quote char!
        if flag['quoted'] == True:
            string_buffer = string_buffer + c
            continue
        
            
        # TODO: This is a lot of work
        
        