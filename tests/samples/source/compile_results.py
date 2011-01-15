import os

SAMPLE_DIRECTORIES = (
    os.path.join('..', 'ifort', '9,1'),
    # os.path.join('..', 'gfortran', '4-4-0'),
    # os.path.join('..', 'gfortran', '4-3-0_osx_intel'),
    # os.path.join('..', 'gfortran', '4-3-0_osx_intel'),
)

OUTPUT_DOCTEST_FILENAME = os.path.join('..', '..', 'output_test.txt')

output_doctest_fh = open(OUTPUT_DOCTEST_FILENAME, 'w')

for sample_dir in SAMPLE_DIRECTORIES:
    for filename in os.listdir(sample_dir):
        if filename.endswith('-output.test'):
            full_filename = os.path.join(sample_dir, filename)
            test_fh = open(full_filename, 'r')
            fmt = input = result = None
            for line in test_fh:
                if line.startswith('FORMAT:'):
                    if (fmt is not None) and (input is not None) and (result is not None):
                        result = result[:-1]
                        input = input.split(',')
                        input = str(input)
                        input = input.replace("'", '')
                        input = input.replace(".TRUE.", 'True')
                        input = input.replace(".FALSE.", 'False')
                        out = '''>>> eds, reversion_eds = parser(lexer(\'\'\'%s\'\'\'))
>>> vals = %s
>>> print output(eds, reversion_eds, vals)
%s
''' % (fmt, input, result)
                        output_doctest_fh.write(out)
                        fmt = input = result = None
                    # Now read in new format
                    fmt = line[7:-1]
                elif line.startswith('INPUT:'):
                    input = line[6:-1]
                elif (fmt is not None) and (input is not None):
                    if result is None:
                        result = line
                    else:
                        result = result + line

output_doctest_fh.close()
print 'Written to: ' + OUTPUT_DOCTEST_FILENAME
