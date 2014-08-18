"""Given an array (i.e.: ['aaa', 'aab', 'aaac']) write a function that finds the
common prefix in all items in this array (In the case above 'aa').
"""

import unittest


def find_prefix(lst):
  "Returns the common prefix on a list"
  pfx = lst[0] if len(lst) > 0 else ''

  for i in lst:
    while pfx != i[0:len(pfx)]:
      pfx = pfx[:-1]

  return pfx


class FindPrefixTest(unittest.TestCase):

  def test_find_prefix(self):
    prefix = find_prefix(['aaa', 'aab', 'aaacc'])
    self.assertEqual(prefix, 'aa')


  def test_no_prefix(self):
    prefix = find_prefix(['abc', 'def'])
    self.assertEqual(prefix, '')


  def test_empty_array(self):
    prefix = find_prefix([])
    self.assertEqual(prefix, '')


if __name__ == '__main__':
  unittest.main()
