I = dict()
I['formats'] = [
  "I1", "I2", "I3", "I4", "I5", "I6", "I7", "I8", "I9", "I10",
  "I1.0", "I2.0", "I3.0", "I4.0", "I5.0", "I6.0", "I7.0", "I8.0", "I9.0", "I10.0",
  "I1.1", "I2.1", "I3.1", "I4.1", "I5.1", "I6.1", "I7.1", "I8.1", "I9.1", "I10.1",
  "I2.2", "I3.2", "I4.2", "I5.2", "I6.2", "I7.2", "I8.2", "I9.2", "I10.2",
  "I3.3", "I4.3", "I5.3", "I6.3", "I7.3", "I8.3", "I9.3", "I10.3",
  "I5.5", "I6.5", "I7.5", "I8.5", "I9.5", "I10.5",
  "1I1", "1I2", "1I3", "1I5", "1I10",
  "2I1", "2I2", "2I3", "2I5", "2I10",
  "3I1", "3I2", "3I3", "3I5", "3I10",
  "1I1.0", "1I2.0", "1I3.0", "1I5.0", "1I10.0",
  "1I3.3", "1I5.3", "1I10.3",
  "3I1.0", "3I2.0", "3I3.0", "3I5.0", "3I10.0",
  "3I3.3", "3I5.3", "3I10.3"
]
I['inputs'] = [
  "0", "-0", "1", "-1", "3", "-3", "10", "-10", "100", "-100", "1000", "-1000", "10000", "-10000", "100000", "-100000", "123456789"
]
I['name'] = 'i'
I['filestem'] = 'i-edit-descriptor-output'

F = dict()
F['formats'] = [
  "F1.0", "F2.0", "F3.0", "F4.0", "F5.0", "F10.0",
  "F1.1", "F2.1", "F3.1", "F4.1", "F5.1", "F10.1",
  "F2.2", "F3.2", "F4.2", "F5.2", "F10.2",
  "F3.3", "F4.3", "F5.3", "F10.3",
  "F4.4", "F5.4", "F10.4",
  "F5.5", "F10.5",
  "F10.10"
]
F['inputs'] = [
  "3.", "-3.", "10.", "-10.", "100.", "-100.", "1000.", "-1000.",
  "10000.", "-10000.", "100000.", "-100000.", "123456789.",
  "0.1", "-0.1", "0.01", "-0.01", "0.001", "-0.001", "0.0001",
  "-0.0001",
  "-1.96e-16", "3.14159"
]
F['name'] = 'f'
F['filestem'] = 'f-edit-descriptor-output'

E = dict()
E['formats'] = [
  "E1.1", "E2.1", "E3.1", "E4.1", "E5.1", "E10.1",
  "E2.2", "E3.2", "E4.2", "E5.2", "E10.2",
  "E3.3", "E4.3", "E5.3", "E10.3",
  "E4.4", "E5.4", "E10.4",
  "E5.5", "E10.5",
  "E10.10",
  "E1.1E1", "E2.1E1", "E3.1E1", "E4.1E1", "E5.1E1", "E10.1E1",
  "E2.2E1", "E3.2E1", "E4.2E1", "E5.2E1", "E10.2E1",
  "E3.3E1", "E4.3E1", "E5.3E1", "E10.3E1",
  "E4.4E1", "E5.4E1", "E10.4E1",
  "E5.5E1", "E10.5E1",
  "E10.10E1",
  "E1.1E3", "E2.1E3", "E3.1E3", "E4.1E3", "E5.1E3", "E10.1E3",
  "E2.2E3", "E3.2E3", "E4.2E3", "E5.2E3", "E10.2E3",
  "E3.3E3", "E4.3E3", "E5.3E3", "E10.3E3",
  "E4.4E3", "E5.4E3", "E10.4E3",
  "E5.5E3", "E10.5E3",
  "E10.10E3",
  "E1.1E4", "E2.1E4", "E3.1E4", "E4.1E4", "E5.1E4", "E10.1E4",
  "E2.2E4", "E3.2E4", "E4.2E4", "E5.2E4", "E10.2E4",
  "E3.3E4", "E4.3E4", "E5.3E4", "E10.3E4",
  "E4.4E4", "E5.4E4", "E10.4E4",
  "E5.5E4", "E10.5E4",
  "E10.10E4",
  "E1.1E5", "E2.1E5", "E3.1E5", "E4.1E5", "E5.1E5", "E10.1E5",
  "E2.2E5", "E3.2E5", "E4.2E5", "E5.2E5", "E10.2E5",
  "E3.3E5", "E4.3E5", "E5.3E5", "E10.3E5",
  "E4.4E5", "E5.4E5", "E10.4E5",
  "E5.5E5", "E10.5E5",
  "E10.10E5"
]
E['inputs'] = [
  "3.", "-3.", "10.", "-10.", "100.", "-100.", "1000.", "-1000.",
  "10000.", "-10000.", "100000.", "-100000.", "123456789.",
  "0.1", "-0.1", "0.01", "-0.01", "0.001", "-0.001", "0.0001",
  "-0.0001",
  "-1.96e-16", "3.14159"
]
E['name'] = 'e'
E['filestem'] = 'e-edit-descriptor-output'


D = dict()
D['formats'] = [
  "D1.1", "D2.1", "D3.1", "D4.1", "D5.1", "D10.1",
  "D2.2", "D3.2", "D4.2", "D5.2", "D10.2",
  "D3.3", "D4.3", "D5.3", "D10.3",
  "D4.4", "D5.4", "D10.4",
  "D5.5", "D10.5",
  "D10.10",
]
D['inputs'] = [
  "3.", "-3.", "10.", "-10.", "100.", "-100.", "1000.", "-1000.",
  "10000.", "-10000.", "100000.", "-100000.", "123456789.",
  "0.1", "-0.1", "0.01", "-0.01", "0.001", "-0.001", "0.0001",
  "-0.0001",
  "-1.96e-16", "3.14159"
]
D['name'] = 'd'
D['filestem'] = 'd-edit-descriptor-output'

# L Edit descriptor
L = dict()
L['formats'] = [
  "L1", "L2", "L3", "L4", "L5", "L6", "L7", "L8", "L9", "L10"
]
L['inputs'] = [
  ".TRUE.", ".FALSE."
]
L['name'] = 'l'
L['filestem'] = 'l-edit-descriptor-output'

# G Edit descriptor
G = dict()
G['formats'] = [
  "G1.1", "G2.1", "G3.1", "G4.1", "G5.1", "G10.1",
  "G2.2", "G3.2", "G4.2", "G5.2", "G10.2",
  "G3.3", "G4.3", "G5.3", "G10.3",
  "G4.4", "G5.4", "G10.4",
  "G5.5", "G10.5",
  "G10.10",
  "G1.1E1", "G2.1E1", "G3.1E1", "G4.1E1", "G5.1E1", "G10.1E1",
  "G2.2E1", "G3.2E1", "G4.2E1", "G5.2E1", "G10.2E1",
  "G3.3E1", "G4.3E1", "G5.3E1", "G10.3E1",
  "G4.4E1", "G5.4E1", "G10.4E1",
  "G5.5E1", "G10.5E1",
  "G10.10E1",
  "G1.1E3", "G2.1E3", "G3.1E3", "G4.1E3", "G5.1E3", "G10.1E3",
  "G2.2E3", "G3.2E3", "G4.2E3", "G5.2E3", "G10.2E3",
  "G3.3E3", "G4.3E3", "G5.3E3", "G10.3E3",
  "G4.4E3", "G5.4E3", "G10.4E3",
  "G5.5E3", "G10.5E3",
  "G10.10E3",
  "G1.1E4", "G2.1E4", "G3.1E4", "G4.1E4", "G5.1E4", "G10.1E4",
  "G2.2E4", "G3.2E4", "G4.2E4", "G5.2E4", "G10.2E4",
  "G3.3E4", "G4.3E4", "G5.3E4", "G10.3E4",
  "G4.4E4", "G5.4E4", "G10.4E4",
  "G5.5E4", "G10.5E4",
  "G10.10E4",
  "G1.1E5", "G2.1E5", "G3.1E5", "G4.1E5", "G5.1E5", "G10.1E5",
  "G2.2E5", "G3.2E5", "G4.2E5", "G5.2E5", "G10.2E5",
  "G3.3E5", "G4.3E5", "G5.3E5", "G10.3E5",
  "G4.4E5", "G5.4E5", "G10.4E5",
  "G5.5E5", "G10.5E5",
  "G10.10E5"
]
G['inputs'] = [
  "3.", "-3.", "10.", "-10.", "100.", "-100.", "1000.", "-1000.",
  "10000.", "-10000.", "100000.", "-100000.", "123456789.",
  "0.1", "-0.1", "0.01", "-0.01", "0.001", "-0.001", "0.0001",
  "-0.0001",
  "-1.96e-16", "3.14159"
]
G['name'] = 'g'
G['filestem'] = 'g-edit-descriptor-output'

A = dict()
A['formats'] = [
  "'The quick brown fox jumps the lazy dog.'",
  "'\"It doesn''t matter anyway\" - said Alice'",
  "''''''"
]
A['inputs'] = [""]
A['name'] = 'a'
A['filestem'] = 'a-edit-descriptor-output'



def gen_test(formats, inputs, name):
    lbl = 0
    format_str = ''
    write_str = ''
    for fmt in formats:
        lbl = lbl + 100
        # Construct the FORMAT statemnts
        buff = "%-6dFORMAT (A, /, A, /, %s)" % (lbl, fmt)
        # Continue the lines if necessary
        while len(buff) > 72:
            format_str = format_str + buff[:72] + '\n'
            buff = '     +' + buff[72:]
        format_str = format_str + buff[:72] + '\n'
        # Construct the WRITE statements
        for inp in inputs:
            # Quote the input so FORTRAN displays correctly
            quoted_fmt = fmt.replace("'", "''")
            if inp == '':
                buff = "      WRITE (1, %d) 'FORMAT:(%s)', 'INPUT:'" % (lbl, quoted_fmt)
            else:
                buff = "      WRITE (1, %d) 'FORMAT:(%s)', 'INPUT:%s', %s" % (lbl, quoted_fmt, inp, inp)
            # Continue the lines if necessary
            while len(buff) > 72:
                write_str = write_str + buff[:72] + '\n'
                buff = '     +' + buff[72:]
            write_str = write_str + buff[:72] + '\n'
    # Output the file
    out = ""
    out = out + "      PROGRAM %sEDIT\n" % name
    out = out + "\n"
    out = out + "      OPEN(UNIT=1, FILE='%s-edit-descriptor-output.test')\n" % name
    out = out + "\n"
    out = out + write_str
    out = out + "\n"
    out = out + "      CLOSE (1)\n"
    out = out + "\n"
    out = out + format_str
    out = out + "\n"
    out = out + "      STOP\n"
    out = out + "      END\n"
    return out

if __name__ == '__main__':
    import sys
    import os
    compile_str = sys.argv[1]
##    for edit_desc in [A]:
    for edit_desc in [L, F, E, G, D, I, A]:
        stem = edit_desc['filestem']
        fh = open(edit_desc['filestem'] + '.f', 'w')
        print 'Generating %s tests ...' % edit_desc['name'].upper()
        fh.write(gen_test(edit_desc['formats'], edit_desc['inputs'], edit_desc['name']))
        fh.close()
        print '  FORTRAN written to %s' % stem + '.f'
        print '  Running %s' % compile_str % (stem + '.f', stem + '.exe')
        os.system(compile_str % (stem + '.f', stem + '.exe'))
        print '  FORTRAN compiled'
        print '  Executing %s ...' % (stem + '.exe')
        os.system(stem + '.exe')
