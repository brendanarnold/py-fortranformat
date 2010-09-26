'''
Miscellaneous functions, classes etc
'''

class has_next_iterator(object):
  '''
  A wrapper class for iterators so that the .has_next() method is implemented

  See - http://stackoverflow.com/questions/1966591/hasnext-in-python-iterators
  '''
  def __init__(self, it):
    self.it = iter(it)
    self._has_next = None
  def __iter__(self): return self
  def next(self):
    if self._has_next:
      result = self._the_next
    else:
      result = self.it.next()
    self._has_next = None
    return result
  def has_next(self):
    if self._has_next is None:
      try: self._the_next = self.it.next()
      except StopIteration: self._has_next = False
      else: self._has_next = True
    return self._has_next

