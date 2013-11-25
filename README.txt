FORTRAN format interpreter for Python
-------------------------------------    

Generates text from a Python list of variables or will read a line of text into Python variables according  to the FORTRAN format statement passed.

Licensed under the MIT license

The library is extensively unit-tested (but not yet extensively user-tested, please report bugs at https://bitbucket.org/brendanarnold/py-fortranformat/issues) against the Intel FORTRAN compiler on a Linux platform. Differences between platforms/compilers are generally minor.

The following is a quistart, full docs are found at the project page wiki  at https://bitbucket.org/brendanarnold/py-fortranformat/wiki/Home

To read Fortran records,

>>> import fortranformat as ff
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

>>> import fortranformat as ff
>>> header_line = FortranRecordWriter('(A15, A15, A15)')
>>> header_line.write(['x', 'y', 'z'])
'              x              y              z'
>>> line = FortranRecordWriter('(3F15.3)')
>>> line.write([1.0, 0.0, 0.5])
'          1.000          0.000          0.500'
>>> line.write([1.1, 0.1, 0.6])
'          1.100          0.100          0.600'


More details on usage, in particlar the configuration options are
found at,

https://bitbucket.org/brendanarnold/py-fortranformat/wiki/Home


Notes
-----

 * At present the library mimics the IO of the Intel FORTRAN compiler
   v.9.1 run on a Linux system. Differences to other FORTRAN compilers
   and platforms are generally minor.
 * The library should run on Python versions from at least 2.3 up to
   3 and above.


Bugs
----

Although the library has a large body of automatically generated test
code behind it, it has not been extensively user tested. Bug reports are
welcome!

Please report bugs to,

https://bitbucket.org/brendanarnold/py-fortranformat/issues

Changelog
---------

Version 0.2.3
 * Fixed issue 10 - Edit descriptor reversion now starts a new record

