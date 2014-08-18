"""Given a function which produces a random integer in the range 1 to 5, write a
function which produces a random integer in the range 1 to 7.
"""

import unittest
from random import randint


def rand5():
  "Returns a random number betwen 1 and 5"
  return randint(1, 5)


def rand7():
  "Returns a random number betwen 1 and 7"
  while True:
    # Generate a int from 0 to 8
    i = (rand5() - 1) + (rand5() - 1)
    # If the int is less than 7 return the value otherwise
    # repeat the calculation.
    if i < 7:
      return i + 1


class TestRand(unittest.TestCase):

  def _sum(self, a_list):
    return reduce(lambda x, y: x+y, a_list)


  def _iterate(self, func, times):
    results = []
    while len(results) < times:
      value = func()
      if value not in results:
        results.append(value)
    return sorted(results)


  def test_rand5(self):
    results = self._iterate(rand5, 5)
    self.assertEqual(len(results), 5)
    self.assertEqual(self._sum(results), 15)


  def test_rand7(self):
    results = self._iterate(rand7, 7)
    self.assertEqual(len(results), 7)
    self.assertEqual(self._sum(results), 28)


if __name__ == '__main__':
    unittest.main()
