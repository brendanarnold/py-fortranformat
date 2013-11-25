from distutils.core import setup

setup(
    name = 'fortranformat',
    packages = ['fortranformat'],
    version = '0.2.3',
    description = 'Mimics Fortran textual IO in Python',
    author = 'Brendan Arnold',
    author_email = 'brendanarnold@gmail.com',
    url = 'http://bitbucket.org/brendanarnold/py-fortranformat',
    download_url = 'https://bitbucket.org/brendanarnold/py-fortranformat/downloads/fortranformat-0.2.4.tar.gz',
    keywords = ['fortran', 'io', 'interface', 'format'],
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Fortran',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Text Processing :: General',
        'Topic :: Software Development :: Interpreters',
        'Topic :: Scientific/Engineering',
    ],
    long_description = '''
FORTRAN format interpreter for Python
-------------------------------------    

Generates text from a Python list of variables or will read a line of text into Python variables according  to the FORTRAN format statement passed.

Licensed under the MIT license

The library is extensively unit-tested (but not yet extensively user-tested, `please report bugs <https://bitbucket.org/brendanarnold/py-fortranformat/issues>`_!) against the Intel FORTRAN compiler on a Linux platform. Differences between platforms/compilers are generally minor.

The following is a quistart, full docs are found at `the project page wiki <https://bitbucket.org/brendanarnold/py-fortranformat/wiki/Home>`_!.

To read Fortran records,:

  >>> import fortranformat as ff
  >>> header_line = ff.FortranRecordReader('(A15, A15, A15)')
  >>> header_line.read('              x              y              z')
    ['              x', '              y', '              z']
  >>> line = FortranRecordReader('(3F15.3)')
  >>> line.read('          1.000          0.000          0.500')
    [1.0, 0.0, 0.5]
  >>> line.read('          1.100          0.100          0.600')
    [1.1, 0.1, 0.6]

To write Fortran records,:

  >>> import fortranformat as ff
  >>> header_line = ff.FortranRecordWriter('(A15, A15, A15)')
  >>> header_line.write(['x', 'y', 'z'])
    '              x              y              z'
  >>> line = FortranRecordWriter('(3F15.3)')
  >>> line.write([1.0, 0.0, 0.5])
    '          1.000          0.000          0.500'
  >>> line.write([1.1, 0.1, 0.6])
    '          1.100          0.100          0.600'
'''
)
