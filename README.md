# FORTRAN format interpreter for Python

Generates text from a Python list of variables or will read a line of text into Python variables according to the FORTRAN format statement passed.

To read Fortran records,

```pycon
>>> from fortranformat import FortranRecordReader
>>> header_line = FortranRecordReader('(A15, A15, A15)')
>>> header_line.read('              x              y              z')
['              x', '              y', '              z']
>>> line = FortranRecordReader('(3F15.3)')
>>> line.read('          1.000          0.000          0.500')
[1.0, 0.0, 0.5]
>>> line.read('          1.100          0.100          0.600')
[1.1, 0.1, 0.6]
```

To write Fortran records,

```pycon
>>> from fortranformat import FortranRecordWriter
>>> header_line = FortranRecordWriter('(A15, A15, A15)')
>>> header_line.write(['x', 'y', 'z'])
'              x              y              z'
>>> line = FortranRecordWriter('(3F15.3)')
>>> line.write([1.0, 0.0, 0.5])
'          1.000          0.000          0.500'
>>> line.write([1.1, 0.1, 0.6])
'          1.100          0.100          0.600'
```

For more detailed usage, see [the guide](https://github.com/brendanarnold/py-fortranformat/blob/master/docs/wiki/guide.md).

## Notes

- At present the library mimics the IO of the Intel FORTRAN compiler
  v.9.1 run on a Linux system. Differences to other FORTRAN compilers
  and platforms are generally minor.
- The library should run on Python versions from at least 3.6

## Development

### Installing locally

```
cd path/to/fortranformat
# Make and activate a virtual environment (recommended)
python3 -m venv .venv
source .venv/bin/activate
# Install the project locally, with the optional test and build dependencies
pip install '.[test,build]'
# Run pytest and make sure these pass
pytest
```

### Generating the tests for a FORTRAN compiler

Characterisations for a selection of FORTRAN compilers already exists, but if you want to characterise a new compiler, do the following ...

1. Configure the compile string under `compilertests` target for your particular FORTRAN compiler e.g. `gfortran %s -o %s` where `%s` is the input and output file placeholders respectively
2. Configure the compiler tag under `compilertests` e.g. `gfortran_10_2_0_osx_intel` this is just used for naming although would advise to sticking to alphanumerics and underscores
3. Run `make compilertests`. This generates, compiles and executes hundreds of combinations of edit descriptor in the FORTRAN compiler under test and saves the results in the `.test` files under the build directories.
4. Move the `.test` files to an appropriate new location under `tests/autogen/[input/output]` into directories named `raw`
5. Run `make buildtests` to generate Python test files based on the generated `.test` files

### Running tests

Build the tests using

```
make buildtests
```

Make sure that pytest is installed then run using

```
make runtests
```

Note that some of the F output edit descriptors fail due to limitations in floating point number representation

To run a reduced test suite where time and resources are limited, use the following

```
make runminimaltests
```

To run a performance test, which currently only covers the reading and writing of floats, use the following

```
make runperformancetests
```

### Deploying a new package version

Update version in `__init__.py`

Update `CHANGELOG.md`

To create a local build to test run ...

```
# Build a local distribution
python -m build
# Make a new virtual environment
python -m venv test_env
# Activate the test_env
source ./test_env/bin/activate
# Install the local build into the test_env
pip install $(find ./dist -name "*.whl")
# Make and enter a tempdir so import fortranformat doesn't find the fortranformat directory
mkdir tmp_dir && cd tmp_dir
# Try run a simple command to make sure that the project installed correctly.
python -c "from fortranformat import FortranRecordReader as FReader; assert FReader(f"(2f10.5)").read("1.0000000 2.0000000")== [1.0, 2.0]"
```

To upload a version to PyPI, create a semantic versioned Git tag for the commit.
This will trigger a Github pipeline publish to PyPI.

## Bugs

Although the library has a large body of automatically generated test
code behind it, it has not been extensively user tested. Bug reports are
welcome!

Please report bugs to,

https://github.com/brendanarnold/py-fortranformat/issues
