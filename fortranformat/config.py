# Should all edit descriptor values be returned even if they were not
# written to?
RET_UNWRITTEN_VARS = True
# Should 'None' values be returned when no record is available to read
# from or the FORTRAN 'default'?
RET_UNWRITTEN_VARS_NONE = True


# Processor dependant default for including leading plus or not
PROC_INCL_PLUS = False 
# Option to allow signed binary, octal and hex on input (not a FORTRAN feature)
PROC_ALLOW_NEG_BOZ = False
# Prcessor dependant padding character
PROC_PAD_CHAR = ' '
# Interpret blanks or jsut a negative as a zero, as in ifort behaviour
PROC_NEG_AS_ZERO = True
# Show a sign for zero?
PROC_SIGN_ZERO = False
PROC_MIN_FIELD_WIDTH = 46
PROC_DECIMAL_CHAR = '.'
G0_NO_BLANKS = False
PROC_NO_LEADING_BLANK = False

