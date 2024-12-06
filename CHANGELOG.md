# Changelog

## [Unreleased]

- Cleanup: [pull 33](https://github.com/brendanarnold/py-fortranformat/pull/33) Remove unused setup.cfg - @davidsch
- Cleanup: [pull 34](https://github.com/brendanarnold/py-fortranformat/pull/34) Remove dependency on nose - @davidsch
- Cleanup: [pull 36](https://github.com/brendanarnold/py-fortranformat/pull/36) Remove extra files from repo - @mwtoews
- Cleanup: [pull 37](https://github.com/brendanarnold/py-fortranformat/pull/37) Fix typos, fix Markdown formatting, refactor examples - @mwtoews
- Feature: [pull 39](https://github.com/brendanarnold/py-fortranformat/pull/39) Add `poetry` build tool and Github Action for deployment - @tbody-cfs

## V 2.0.0

- Feature: [Issue 6](https://github.com/brendanarnold/py-fortranformat/issues/6) Improve performance of reading and writing of `F` format by x10 - @ZedThree
- BREAKING: Python 3.6 now required

## V 1.2.2

- Bug: [Issue 28](https://github.com/brendanarnold/py-fortranformat/issues/28) Fix a bug where crash occurs on outputting infinity or NaN for a floating point number type.

## V 1.2.1

- Feature: [Issue 25](https://github.com/brendanarnold/py-fortranformat/issues/25) Include a minimal test suite for use where resources are limited e.g. pipeline builds

## V 1.2.0

- Bug: [Issue 21](https://github.com/brendanarnold/py-fortranformat/issues/21) Now outputs FORTRAN default values when `None` is passed.

## V 1.1.1

- Bug: [Issue 15](https://github.com/brendanarnold/py-fortranformat/issues/15) Fix hanging when no suitable edit descriptor specified for `G_INPUT_TRIAL_EDS`. Now raises `ValueError`

## V 1.1.0

- Bug: Fixed overflow behaviour in tests, in particular fixing the PROC_MAXINT behaviour
- Bug: [Issue 17](https://github.com/brendanarnold/py-fortranformat/issues/17) Properly outputs zero dp floating point numbers
- Migrated to development on Python 3 (non-test code still compatible with Python 2)
- Generally used more standard project structure as detailed at [https://docs.python-guide.org/writing/structure/](https://docs.python-guide.org/writing/structure/)

## V 1.0.1

- Bug: Incorrect case on filename prevented `setup.py` executing on case-sensitive filesystems

## V 1.0.0

- **BREAKING** No longer uses `eval` for importing modules - `eval` was originally used to support very early versions of Python (2.3+) but it now means that modern packaging systems cannot understand `fortranformat` module structure. Since the latter is a more likely use-case the `eval` statements have now been dropped. It has been tested with Python 2.7+ and likely still works with earlier versions
- Migrated and recreated docs on Git/Github from Mercurial/Bitbucket
- Fixed issue where decimal values of G and E edit descriptors were causing exceptions on output
- The `config.RECORD_SEPARATOR` is not reset properly when calling `config.reset()`
- Tests for more of the edge cases
- Edit descriptors now output quoted strings even when there are no more values to output

## V 0.2.3

- Fixed issue 10 - Edit descriptor reversion now starts a new record
