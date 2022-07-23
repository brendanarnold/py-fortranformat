'''
Run this on cloning the source which only contains the Fortran *.test results

This will generate the unittest *_test_*.py files that are stored in the test hierarchy
'''

import os
import re
from gen_input_tests import write_unittest as write_input_unittest
from gen_output_tests import write_unittest as write_output_unittest

INPUT_DIR = r'./tests/autogen/input'
OUTPUT_DIR = r'./tests/autogen/output'
# Minimal tests are a reduced set of tests used for when resources are limited e.g. pipelines
MINIMAL_TESTS_DIR = r'./tests/minimal'
MINIMAL_TEST_LIMIT = 10
# Input tests are 'batched' hence the integer at the end
INPUT_TEST_FILESTEM = r'(\w+)-ed-input-(\d+)\.test'
# Output tests may have one or two edit descriptors hence the weird
# prefix
OUTPUT_TEST_FILESTEM = r'((\w+-)?\w+)-ed-output\.test'
INPUT_UNITTEST_FILESTEM = 'test_%s_input_%d.py'
OUTPUT_UNITTEST_FILESTEM = 'test_%s_output.py'

# Start with the input tests
for filepath, subdirs, dummy in os.walk(INPUT_DIR):
    # Identify by the raw subdirectory
    if 'raw' not in subdirs:
        continue
    raw_filepath = os.path.join(filepath, 'raw')
    platform = os.path.split(filepath)[-1]
    # Raw subdirectory contains the Fortran output
    for fn in os.listdir(raw_filepath):
        res = re.match(INPUT_TEST_FILESTEM, fn)
        if not res:
            continue
        name = res.group(1)
        batch = int(res.group(2))
        infile = os.path.join(raw_filepath, fn)
        outfile = os.path.join(
            filepath, INPUT_UNITTEST_FILESTEM % (name, batch))
        write_input_unittest(infile, outfile, batch, name,
                             platform)
        minimal_outfile = os.path.join(
            MINIMAL_TESTS_DIR, INPUT_UNITTEST_FILESTEM % (name, batch))
        write_input_unittest(infile, minimal_outfile, batch, name,
                             platform, test_limit=MINIMAL_TEST_LIMIT)

# Now output tests
for filepath, subdirs, dummy in os.walk(OUTPUT_DIR):
    # Identify by the raw subdirectory
    if 'raw' not in subdirs:
        continue
    raw_filepath = os.path.join(filepath, 'raw')
    platform = os.path.split(filepath)[-1]
    # Raw subdirectory contains the Fortran output
    for fn in os.listdir(raw_filepath):
        res = re.match(OUTPUT_TEST_FILESTEM, fn)
        if not res:
            continue
        name = res.group(1)
        infile = os.path.join(raw_filepath, fn)
        outfile = os.path.join(filepath, OUTPUT_UNITTEST_FILESTEM % name)
        write_output_unittest(infile, outfile, name,
                              platform)
        minimal_outfile = os.path.join(
            MINIMAL_TESTS_DIR, OUTPUT_UNITTEST_FILESTEM % name)
        write_output_unittest(infile, minimal_outfile, name,
                              platform, test_limit=MINIMAL_TEST_LIMIT)
