

import fortranformat as ff
from timeit import default_timer as timer
from datetime import timedelta


RECORDS = 50000

fmt = ff.FortranRecordWriter('5F10.4')

print('Start ...')

start = timer()
for i in range(RECORDS):
    fmt.write([1.123] * 5)
end = timer()

print('End')
print(timedelta(seconds=end-start))
