FORTRAN format interpreter for Python
-------------------------------------    

Generates text from some Python variables or will read a line of
text into Python variables according to the format statement passed

This is licensed under the MIT license

To use to read Fortran records,

>>> from fortranformat import FortranRecordReader
>>> header_line = FortranRecordReader('(A15, A15, A15)')
>>> header_line.read('              x              y              z')
['              x', '              y', '              z']
>>> line = FortranRecordReader('(3F15.3)')
>>> line.read('          1.000          0.000          0.500')
[1.0, 0.0, 0.5]
>>> line.read('          1.100          0.100          0.600')
[1.1, 0.1, 0.6]
>>>

To write Fortran records,

>>> from fortranformat import FortranRecordWriter
>>> header_line = FortranRecordWriter('(A15, A15, A15)')
>>> header_line.write(['x', 'y', 'z'])
'              x              y              z'
>>> line = FortranRecordWriter('(3F15.3)')
>>> line.write([1.0, 0.0, 0.5])
'          1.000          0.000          0.500'
>>> line.write([1.1, 0.1, 0.6])
'          1.100          0.100          0.600'

