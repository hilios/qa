"""Implement division (without using the divide operator, obviously).
"""

import unittest


def remainder(num, div):
  while num >= div:
    num = num - div
  return num


def div(num, div):
  i = 0
  while num >= div:
    i += 1
    div += i

  return i


class DivisionTest(unittest.TestCase):

  def test_division(self):
    self.assertEqual(div(4, 2), 4 / 2)
    self.assertEqual(div(8, 2), 8 / 2)

  def test_remainder(self):
    self.assertEqual(remainder(4, 3), 4 / 3)
    self.assertEqual(remainder(8, 3), 8 / 3)


if __name__ == '__main__':
  unittest.main()
