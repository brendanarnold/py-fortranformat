import os
from setuptools import setup

HERE = os.path.dirname(os.path.abspath(__file__))
README = ''
with open(HERE + '/readme.md') as fh:
    README = fh.read()

setup(
    name = 'fortranformat',
    packages = ['fortranformat'],
    version = '1.0.0',
    description = 'Mimics Fortran textual IO in Python',
    author = 'Brendan Arnold',
    author_email = 'brendanarnold@gmail.com',
    url = 'https://github.com/brendanarnold/py-fortranformat',
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
    long_description = README,
    long_description_content_type = "text/markdown"
)
