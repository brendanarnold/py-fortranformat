help:
	@echo "See the Makefile for possible commands"

compilertests:
	cd tests/autogen/generate; \
	python gen_input_tests.py "gfortran %s -o %s" "10_2_0_osx_intel"; \
	python gen_output_tests.py "gfortran %s -o %s" "10_2_0_osx_intel"; \
	cd ../../..

buildtests:
	python tests/autogen/generate/build_unittests.py

runtests:
  # This takes a few minutes to run
	python -m pytest tests/handwritten
	python -m pytest tests/autogen/input/ifort/9_1_linux_intel
	python -m pytest tests/autogen/output/ifort/9_1_linux_intel

runminimaltests:
	# A reduced test suite run for when resources are limited e.g. in pipeline builds
	python -m pytest tests/handwritten
	python -m pytest tests/minimal
