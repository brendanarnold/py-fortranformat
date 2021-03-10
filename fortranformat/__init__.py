__version__ = '0.2.5'

import sys
IS_PYTHON3 = sys.version_info[0] >= 3

if IS_PYTHON3:
    from .FortranRecordReader import FortranRecordReader
    from .FortranRecordWriter import FortranRecordWriter
    from . import config
else:
    from FortranRecordReader import FortranRecordReader
    from FortranRecordWriter import FortranRecordWriter
    import config


