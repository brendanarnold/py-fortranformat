from fortranformat import FortranRecordWriter, FortranRecordReader
from datetime import datetime

import numpy as np


def test_read_write_array():
    nx = 1000
    ny = 200
    array = np.linspace(0, 1, nx * ny).reshape((nx, ny))
    writer = FortranRecordWriter("(5f17.9)")
    text = writer.write(array.flatten("F"))

    reader = FortranRecordReader("(5f17.9)")
    for line in text.splitlines():
        new_array = reader.read(line)



if __name__ == "__main__":
    startTime = datetime.now()
    test_read_write_array()
    print(datetime.now() - startTime)