Add current directory to pythonpath e.g. on windows

set PYTHONPATH=%cd%

Then run e.g.

nosetests -w "tests\autogen\input\ifort\9-1_linux_intel"


Note some of the Z input edit descriptor tests fail because in FORTRAN they overflow whereas Python can handle arbitrarily large integers

Some of the F output edit descriptors fail due to precision issues