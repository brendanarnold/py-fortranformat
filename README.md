# FORTRAN format interpreter for Python

Generates text from a Python list of variables or will read a line of text into Python variables according  to the FORTRAN format statement passed.

Licensed under the MIT license

The library is extensively unit-tested against the Intel FORTRAN compiler on a Linux platform. Differences between platforms/compilers are generally minor.

To read Fortran records,

```
import fortranformat as ff
header_line = FortranRecordReader('(A15, A15, A15)')
header_line.read('              x              y              z')
['              x', '              y', '              z']
line = FortranRecordReader('(3F15.3)')
line.read('          1.000          0.000          0.500')
# Returns [1.0, 0.0, 0.5]
line.read('          1.100          0.100          0.600')
# Returns [1.1, 0.1, 0.6]
```

To write Fortran records,

```
import fortranformat as ff
header_line = FortranRecordWriter('(A15, A15, A15)')
header_line.write(['x', 'y', 'z'])
# Results in '              x              y              z'
line = FortranRecordWriter('(3F15.3)')
line.write([1.0, 0.0, 0.5])
# Results in '          1.000          0.000          0.500'
line.write([1.1, 0.1, 0.6])
# Results in '          1.100          0.100          0.600'
```

For more detailed usage, see [the guide](https://github.com/brendanarnold/py-fortranformat/blob/master/docs/wiki/guide.md).

## Notes

 * At present the library mimics the IO of the Intel FORTRAN compiler
   v.9.1 run on a Linux system. Differences to other FORTRAN compilers
   and platforms are generally minor.
 * The library should run on Python versions from at least 2.7


## Development

### Generating the tests for a FORTRAN compiler

The bulk of the tests are auto generated using Python scripts located in `tests/autogen/generate`. The tests were generated as follows ...

  1. Configure `gen_input_tests.py` for your particular FORTRAN compiler
  2. Run the above scripts to generate the `.test` files in the relevant `raw` directory under the `tests/autogen/input` directory. These generate, compile and execute hundreds of combinations of edit descriptor in the FORTRAN compiler under test and saves the results in the `.test` files
  3. Repeat for the 'output' tests
  4. Run `build_unittests.py` to generate Python test files based on the generated `.test` files

### Running tests

Make sure that nose tests is installed and run using

`sh scripts/runtests.sh`

Note some of the Z input edit descriptor tests fail because in FORTRAN they overflow whereas Python can handle arbitrarily large integers

Some of the F output edit descriptors fail due to precision issues

### Deploying a new package version

Update versions in `setup.py` and `__init__.py`

To create a local build to test run ...

`python setup.py build sdist --formats=gztar bdist_wininst`

To upload a version to PyPI run ...

`python setup.py sdist --formats=gztar bdist_wininst upload`

## Bugs

Although the library has a large body of automatically generated test
code behind it, it has not been extensively user tested. Bug reports are
welcome!

Please report bugs to,

https://github.com/brendanarnold/py-fortranformat/issues



