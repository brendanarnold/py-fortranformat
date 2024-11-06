from .FortranRecordReader import FortranRecordReader
from .FortranRecordWriter import FortranRecordWriter
from ._exceptions import InvalidFormat
from . import config

# Read in the 'version' tag of the installed package
import importlib.metadata
__version__ = importlib.metadata.version("fortranformat")

__all__ = [
    "FortranRecordReader",
    "FortranRecordWriter",
    "InvalidFormat",
    "config",
    "__version__",
]