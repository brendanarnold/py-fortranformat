# call with
# python gen_tests.py 'COMPILER %s -o %s'
# where first %s is the input file and the second is the output 

import itertools
import os


# MODIFIER_EDS = ['SP']
# OUTPUT_EDS = ['F']
EDS = ['BN', 'BZ', 'Slash', 'SP', 'SS', 'T', 'TL', 'TR', 'X', 'Colon', 'A', 'B', 'D', 'EN', 'ES', 'E', 'F', 'G', 'I', 'L', 'O', 'Z']
MODIFIER_EDS = ['BN', 'BZ', 'Slash', 'SP', 'SS', 'T', 'TL', 'TR', 'X', 'Colon']
OUTPUT_EDS = ['A', 'B', 'D', 'EN', 'ES', 'E', 'F', 'G', 'I', 'L', 'O', 'Z', 'Slash']
SOURCE_FILESTEM = '%s-ed-output.f'
EXECUTABLE_FILESTEM = '%s-ed-output.exe'
RESULT_FILESTEM = '%s-ed-output.test'
DOCTEST_FILESTEM = '%s-output-test.pytest'
BUILD_DIR = r'build-output-tests'

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

# L Edit descriptor
L = dict()
L['formats'] = [
  "L1", "L2", "L3", "L4", "L5", "L6", "L7", "L8", "L9", "L10"
]
L['inputs'] = [
  ".TRUE.", ".FALSE."
]
L['name'] = 'l'

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

A = dict()
A['formats'] = [
  "A", "A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "A9", "A10", "A25", "A50", "A100"
]
A['inputs'] = [
  "'The quick brown fox jumps the lazy dog.'",
  "'\"It doesn''t matter anyway\" - said Alice'",
  "''''''"
]
A['name'] = 'a'

StringLiteral = dict()
StringLiteral['formats'] = [
  "'The quick brown fox jumps the lazy dog.'",
  "'\"It doesn''t matter anyway\" - said Alice'",
  "''''''"
]
StringLiteral['inputs'] = [""]
StringLiteral['name'] = 'stringliteral'

EN = dict()
EN['formats'] = [
  "EN1.1", "EN2.1", "EN3.1", "EN4.1", "EN5.1", "EN10.1",
  "EN2.2", "EN3.2", "EN4.2", "EN5.2", "EN10.2",
  "EN3.3", "EN4.3", "EN5.3", "EN10.3",
  "EN4.4", "EN5.4", "EN10.4",
  "EN5.5", "EN10.5",
  "EN10.10",
  "EN1.1E1", "EN2.1E1", "EN3.1E1", "EN4.1E1", "EN5.1E1", "EN10.1E1",
  "EN2.2E1", "EN3.2E1", "EN4.2E1", "EN5.2E1", "EN10.2E1",
  "EN3.3E1", "EN4.3E1", "EN5.3E1", "EN10.3E1",
  "EN4.4E1", "EN5.4E1", "EN10.4E1",
  "EN5.5E1", "EN10.5E1",
  "EN10.10E1",
  "EN1.1E3", "EN2.1E3", "EN3.1E3", "EN4.1E3", "EN5.1E3", "EN10.1E3",
  "EN2.2E3", "EN3.2E3", "EN4.2E3", "EN5.2E3", "EN10.2E3",
  "EN3.3E3", "EN4.3E3", "EN5.3E3", "EN10.3E3",
  "EN4.4E3", "EN5.4E3", "EN10.4E3",
  "EN5.5E3", "EN10.5E3",
  "EN10.10E3",
  "EN1.1E4", "EN2.1E4", "EN3.1E4", "EN4.1E4", "EN5.1E4", "EN10.1E4",
  "EN2.2E4", "EN3.2E4", "EN4.2E4", "EN5.2E4", "EN10.2E4",
  "EN3.3E4", "EN4.3E4", "EN5.3E4", "EN10.3E4",
  "EN4.4E4", "EN5.4E4", "EN10.4E4",
  "EN5.5E4", "EN10.5E4",
  "EN10.10E4",
  "EN1.1E5", "EN2.1E5", "EN3.1E5", "EN4.1E5", "EN5.1E5", "EN10.1E5",
  "EN2.2E5", "EN3.2E5", "EN4.2E5", "EN5.2E5", "EN10.2E5",
  "EN3.3E5", "EN4.3E5", "EN5.3E5", "EN10.3E5",
  "EN4.4E5", "EN5.4E5", "EN10.4E5",
  "EN5.5E5", "EN10.5E5",
  "EN10.10E5"
]
EN['inputs'] = [
  "3.", "-3.", "10.", "-10.", "100.", "-100.", "1000.", "-1000.",
  "10000.", "-10000.", "100000.", "-100000.", "123456789.",
  "0.1", "-0.1", "0.01", "-0.01", "0.001", "-0.001", "0.0001",
  "-0.0001",
  "-1.96e-16", "3.14159"
]
EN['name'] = 'en'

ES = dict()
ES['formats'] = [
  "ES1.1", "ES2.1", "ES3.1", "ES4.1", "ES5.1", "ES10.1",
  "ES2.2", "ES3.2", "ES4.2", "ES5.2", "ES10.2",
  "ES3.3", "ES4.3", "ES5.3", "ES10.3",
  "ES4.4", "ES5.4", "ES10.4",
  "ES5.5", "ES10.5",
  "ES10.10",
  "ES1.1E1", "ES2.1E1", "ES3.1E1", "ES4.1E1", "ES5.1E1", "ES10.1E1",
  "ES2.2E1", "ES3.2E1", "ES4.2E1", "ES5.2E1", "ES10.2E1",
  "ES3.3E1", "ES4.3E1", "ES5.3E1", "ES10.3E1",
  "ES4.4E1", "ES5.4E1", "ES10.4E1",
  "ES5.5E1", "ES10.5E1",
  "ES10.10E1",
  "ES1.1E3", "ES2.1E3", "ES3.1E3", "ES4.1E3", "ES5.1E3", "ES10.1E3",
  "ES2.2E3", "ES3.2E3", "ES4.2E3", "ES5.2E3", "ES10.2E3",
  "ES3.3E3", "ES4.3E3", "ES5.3E3", "ES10.3E3",
  "ES4.4E3", "ES5.4E3", "ES10.4E3",
  "ES5.5E3", "ES10.5E3",
  "ES10.10E3",
  "ES1.1E4", "ES2.1E4", "ES3.1E4", "ES4.1E4", "ES5.1E4", "ES10.1E4",
  "ES2.2E4", "ES3.2E4", "ES4.2E4", "ES5.2E4", "ES10.2E4",
  "ES3.3E4", "ES4.3E4", "ES5.3E4", "ES10.3E4",
  "ES4.4E4", "ES5.4E4", "ES10.4E4",
  "ES5.5E4", "ES10.5E4",
  "ES10.10E4",
  "ES1.1E5", "ES2.1E5", "ES3.1E5", "ES4.1E5", "ES5.1E5", "ES10.1E5",
  "ES2.2E5", "ES3.2E5", "ES4.2E5", "ES5.2E5", "ES10.2E5",
  "ES3.3E5", "ES4.3E5", "ES5.3E5", "ES10.3E5",
  "ES4.4E5", "ES5.4E5", "ES10.4E5",
  "ES5.5E5", "ES10.5E5",
  "ES10.10E5"
]
ES['inputs'] = [
  "3.", "-3.", "10.", "-10.", "100.", "-100.", "1000.", "-1000.",
  "10000.", "-10000.", "100000.", "-100000.", "123456789.",
  "0.1", "-0.1", "0.01", "-0.01", "0.001", "-0.001", "0.0001",
  "-0.0001",
  "-1.96e-16", "3.14159"
]
ES['name'] = 'es'

O = dict()
O['formats'] = [
  "O1", "O2", "O3", "O4", "O5", "O6", "O7", "O8", "O9", "O10",
  "O1.0", "O2.0", "O3.0", "O4.0", "O5.0", "O6.0", "O7.0", "O8.0", "O9.0", "O10.0",
  "O1.1", "O2.1", "O3.1", "O4.1", "O5.1", "O6.1", "O7.1", "O8.1", "O9.1", "O10.1",
  "O2.2", "O3.2", "O4.2", "O5.2", "O6.2", "O7.2", "O8.2", "O9.2", "O10.2",
  "O3.3", "O4.3", "O5.3", "O6.3", "O7.3", "O8.3", "O9.3", "O10.3",
  "O5.5", "O6.5", "O7.5", "O8.5", "O9.5", "O10.5",
  "1O1", "1O2", "1O3", "1O5", "1O10",
  "2O1", "2O2", "2O3", "2O5", "2O10",
  "3O1", "3O2", "3O3", "3O5", "3O10",
  "1O1.0", "1O2.0", "1O3.0", "1O5.0", "1O10.0",
  "1O3.3", "1O5.3", "1O10.3",
  "3O1.0", "3O2.0", "3O3.0", "3O5.0", "3O10.0",
  "3O3.3", "3O5.3", "3O10.3"
]
O['inputs'] = [
  "0", "-0", "1", "-1", "3", "-3", "10", "-10", "100", "-100", "1000", "-1000", "10000", "-10000", "100000", "-100000", "123456789"
]
O['name'] = 'o'

Z = dict()
Z['formats'] = [
  "Z1", "Z2", "Z3", "Z4", "Z5", "Z6", "Z7", "Z8", "Z9", "Z10",
  "Z1.0", "Z2.0", "Z3.0", "Z4.0", "Z5.0", "Z6.0", "Z7.0", "Z8.0", "Z9.0", "Z10.0",
  "Z1.1", "Z2.1", "Z3.1", "Z4.1", "Z5.1", "Z6.1", "Z7.1", "Z8.1", "Z9.1", "Z10.1",
  "Z2.2", "Z3.2", "Z4.2", "Z5.2", "Z6.2", "Z7.2", "Z8.2", "Z9.2", "Z10.2",
  "Z3.3", "Z4.3", "Z5.3", "Z6.3", "Z7.3", "Z8.3", "Z9.3", "Z10.3",
  "Z5.5", "Z6.5", "Z7.5", "Z8.5", "Z9.5", "Z10.5",
  "1Z1", "1Z2", "1Z3", "1Z5", "1Z10",
  "2Z1", "2Z2", "2Z3", "2Z5", "2Z10",
  "3Z1", "3Z2", "3Z3", "3Z5", "3Z10",
  "1Z1.0", "1Z2.0", "1Z3.0", "1Z5.0", "1Z10.0",
  "1Z3.3", "1Z5.3", "1Z10.3",
  "3Z1.0", "3Z2.0", "3Z3.0", "3Z5.0", "3Z10.0",
  "3Z3.3", "3Z5.3", "3Z10.3"
]
Z['inputs'] = [
  "0", "-0", "1", "-1", "3", "-3", "10", "-10", "100", "-100", "1000", "-1000", "10000", "-10000", "100000", "-100000", "123456789"
]
Z['name'] = 'z'

B = dict()
B['formats'] = [
  "B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8", "B9", "B10",
  "B1.0", "B2.0", "B3.0", "B4.0", "B5.0", "B6.0", "B7.0", "B8.0", "B9.0", "B10.0",
  "B1.1", "B2.1", "B3.1", "B4.1", "B5.1", "B6.1", "B7.1", "B8.1", "B9.1", "B10.1",
  "B2.2", "B3.2", "B4.2", "B5.2", "B6.2", "B7.2", "B8.2", "B9.2", "B10.2",
  "B3.3", "B4.3", "B5.3", "B6.3", "B7.3", "B8.3", "B9.3", "B10.3",
  "B5.5", "B6.5", "B7.5", "B8.5", "B9.5", "B10.5",
  "1B1", "1B2", "1B3", "1B5", "1B10",
  "2B1", "2B2", "2B3", "2B5", "2B10",
  "3B1", "3B2", "3B3", "3B5", "3B10",
  "1B1.0", "1B2.0", "1B3.0", "1B5.0", "1B10.0",
  "1B3.3", "1B5.3", "1B10.3",
  "3B1.0", "3B2.0", "3B3.0", "3B5.0", "3B10.0",
  "3B3.3", "3B5.3", "3B10.3"
]
B['inputs'] = [
  "0", "-0", "1", "-1", "3", "-3", "10", "-10", "100", "-100", "1000", "-1000", "10000", "-10000", "100000", "-100000", "123456789"
]
B['name'] = 'b'

# These edit descriptors do not output values as such, instead they must be
# used in combination with other edit descriptors to have an effect

BN = {}
BN['formats'] = ['BN']
BN['name'] = 'bn'
BN['inputs'] = []

BZ = {}
BZ['formats'] = ['BZ']
BZ['name'] = 'bz'
BZ['inputs'] = []

Colon = {}
Colon['formats'] = [':']
Colon['name'] = 'colon'
Colon['inputs'] = []

P = {}
P['formats'] = [
    '-100P', '-99P', '-50P', '-25P', '-10P', '-9P', '-8P', '-7P', '-6P', '-5P', '-4P', '-3P', '-2P', '-1P', '0P', '1P', '2P', '3P', '4P', '5P', '6P', '7P', '8P', '9P', '10P', '25P', '50P', '99P', '100P'
]
P['name'] = 'p'
P['inputs'] = []

Slash = {}
Slash['formats'] = ['/']
Slash['name'] = 'slash'
Slash['inputs'] = []

S = {}
S['formats'] = ['S']
S['name'] = 's'
S['inputs'] = []

SS = {}
SS['formats'] = ['SS']
SS['name'] = 'ss'
SS['inputs'] = []

SP = {}
SP['formats'] = ['SP']
SP['name'] = 'sp'
SP['inputs'] = []

T = {}
T['formats'] = ['T1', 'T2', 'T3', 'T4', 'T5', 'T6', 'T7', 'T8', 'T9', 'T10', 'T25', 'T50', 'T100']
T['name'] = 't'
T['inputs'] = []

TR = {}
TR['formats'] = ['TR1', 'TR2', 'TR3', 'TR4', 'TR5', 'TR6', 'TR7', 'TR8', 'TR9', 'TR10', 'TR25', 'TR50', 'TR100']
TR['name'] = 'tr'
TR['inputs'] = []

TL = {}
TL['formats'] = ['TL1', 'TL2', 'TL3', 'TL4', 'TL5', 'TL6', 'TL7', 'TL8', 'TL9', 'TL10', 'TL25', 'TL50', 'TL100']
TL['name'] = 'tl'
TL['inputs'] = []

X = {}
X['formats'] = ['1X', '2X', '3X', '4X', '5X', '6X', '7X', '8X', '9X', '10X', '25X', '50X', '100X']
X['name'] = 'x'
X['inputs'] = []

SPECIAL = {}
SPECIAL['formats'] = []
SPECIAL['name'] = 'special'
SPECIAL['inputs'] = []

def output_calling_code():
    '''Outputs to conosle the Python necessary to call all the tests from
    _output.py'''
    for name in names():
        doctest_filename = DOCTEST_FILESTEM % name
        snippet = '''        doctest.testfile(os.path.join(TEST_PATH, '%s'), \\
            globs=globs)''' % doctest_filename
        print snippet
        

def write_py_source():
    '''Converts the test output to a doctestable text file'''
    for name in names():
        doctest_filename = os.path.join(BUILD_DIR, DOCTEST_FILESTEM % name)
        filename = os.path.join(BUILD_DIR, RESULT_FILESTEM % name)
        out_fh = open(doctest_filename, 'w')
        print 'Pythonising %s into %s ...' % (filename, doctest_filename)
        in_fh = open(filename, 'r')
        fmt = inpt = result = None
        for line in in_fh:
            if line.startswith('FORMAT:'):
                if (fmt is not None) and (inpt is not None) and (result is not None):
                    result = result[:-1]
                    # inpt = inpt.split(',')
                    inpt = str(inpt)
                    if inpt[0] == inpt[-1] == "'":
                        inpt = "'" + inpt[1:-1].replace("''", "\\'") + "'"
                    else:
                        inpt = inpt.replace("''", "\\'")
                    inpt = inpt.replace(".TRUE.", 'True')
                    inpt = inpt.replace(".FALSE.", 'False')
                    out = '''>>> eds, reversion_eds = parser(lexer(\'\'\'%s\'\'\'))
>>> vals = [%s]
>>> print '[' + output(eds, reversion_eds, vals) + ']'
[%s]
''' % (fmt, inpt, result)
                    out_fh.write(out)
                    fmt = inpt = result = None
                # Now read in new format
                fmt = line[7:-1]
            elif line.startswith('INPUT:'):
                inpt = line[6:-1]
            elif (fmt is not None) and (inpt is not None):
                # If line is empty, input doctests <BLANKLINE> statement
                if line[:-1] == '':
                    if (result is not None) and (len(result) > 0):
                        line = '<BLANKLINE>\n'
                    else:
                        line = '\n'
                if result is None:
                    result = line
                else:
                    result = result + line
        in_fh.close()
        out_fh.close()


def compile_tests(compile_str):
    '''Compiles the tests'''
    for name in names():
        infile = os.path.join(BUILD_DIR, SOURCE_FILESTEM % name)
        outfile = os.path.join(BUILD_DIR, EXECUTABLE_FILESTEM % name)
        print 'Compiling %s to %s ...' % (infile, outfile)
        os.system(compile_str % (infile, outfile))

def execute_tests():
    '''Executes the compiled tests and directs the output to .test files'''
    for name in names():
        executable_file = os.path.join(BUILD_DIR, EXECUTABLE_FILESTEM % name)
        result_file = os.path.join(BUILD_DIR, RESULT_FILESTEM % name)
        print 'Executing %s > %s' % (executable_file, result_file)
        os.system('%s > %s' % (executable_file, result_file))

def write_fortran_source(formats, inputs, name):
    filename = os.path.join(BUILD_DIR, SOURCE_FILESTEM % name)
    print 'Generating %s ...' % filename
    fh = open(filename, 'w')
    if name == 'special':
        # Generate one-to-one
        assert(len(inputs) == len(formats))
        fmt_inp_pairs = itertools.izip(enumerate(formats), inputs)
    else:
        # Generate all the combinations
        fmt_inp_pairs = product(enumerate(formats), inputs)
    # Output the start of the source file
    fh.write("      PROGRAM %sEDIT\n\n\n" % name.upper().replace('-', '_'))
    for fmt_tup, inp in fmt_inp_pairs:
        lbl = fmt_tup[0] + 1
        # Quote the format so FORTRAN displays correctly
        quoted_fmt = fmt_tup[1].replace("'", "''")
        # Quote the input so FORTRAN displays correctly
        quoted_inp = inp.replace("'", "''")
        if inp == '':
            line = """      WRITE (*, %d) 'FORMAT:(%s)', 'INPUT:'""" % (lbl, quoted_fmt)
        else:
            line = """      WRITE (*, %d) 'FORMAT:(%s)', 'INPUT:%s', %s""" % (lbl, quoted_fmt, quoted_inp, inp)
        # Continue the lines if necessary
        while len(line) > 72:
            fh.write(line[:72] + '\n')
            line = '     +' + line[72:]
        fh.write(line[:72] + '\n')
    # Output the format statements
    fh.write("\n")
    for ind, fmt in enumerate(formats):
        lbl = ind + 1
        fh.write("%-6dFORMAT (A, /, A, /, %s)\n" % (lbl, fmt))
    # Ouptut the closing source
    fh.write("\n      STOP\n      END\n")
    fh.close()


def gen_tests():
    '''Generates the FORTRAN source for the tests in separates files'''
    names = []
    # First generate tests for each edit descriptor on its own
    for ed in EDS:
        formats = globals()[ed]['formats']
        name = globals()[ed]['name']
        inputs = globals()[ed]['inputs']
        write_fortran_source(formats, inputs, name)
        # Store the name for later compilation
        names.append(name)
    # Then do combinations of two edit descriptors for modifier edit descriptors
    for ed in MODIFIER_EDS:
        mod_formats = globals()[ed]['formats']
        mod_name = globals()[ed]['name']
        for out_ed in OUTPUT_EDS:
            out_formats = globals()[out_ed]['formats']
            out_name = globals()[out_ed]['name']
            out_inputs = globals()[out_ed]['inputs']
            name = mod_name + '-' + out_name
            inputs = out_inputs
            # Need to combine the formats appropriately
            formats = []
            for mfmt in mod_formats:
                for ofmt in out_formats:
                    formats.append(mfmt + ', ' + ofmt)
            write_fortran_source(formats, inputs, name)
            # Store the name for later compilation
            names.append(name)
    # Finally write the special case extra tests, there should be one to one
    # relationship between the formats and the inputs
    write_fortran_source(SPECIAL['formats'], SPECIAL['inputs'], 'special')
    names.append('special')
    return names
        
def names():
    '''Generates a list of all the names'''
    names = []
    for ed in EDS:
        ed = globals()[ed]
        yield ed['name']
    for ed in MODIFIER_EDS:
        ed = globals()[ed]
        mod_name = ed['name']
        for out_ed in OUTPUT_EDS:
            out_ed = globals()[out_ed]
            out_name = out_ed['name']
            yield mod_name + '-' + out_name


def product(*args, **kwds):
    '''Substitute for itertools.product which does not appear in Python 2.3'''
    pools = map(tuple, args) * kwds.get('repeat', 1)
    result = [[]]
    for pool in pools:
        result = [x + [y] for x in result for y in pool]
    for prod in result:
        yield tuple(prod)

if __name__ == '__main__':
    import sys
    compile_str = sys.argv[1]
    gen_tests()
    compile_tests(compile_str)
    execute_tests()
    # write_py_source()
    # output_calling_code()


# Note: test comma-less p use
