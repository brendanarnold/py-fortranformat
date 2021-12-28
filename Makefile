help:
	echo "See the Makefile for possible commands"

buildtests:
	python tests/autogen/generate/build_unittests.py

runtests:
	nosetests tests/autogen/output/ifort/9-1_linux_intel tests/autogen/input/ifort/9-1_linux_intel test/handwritten
