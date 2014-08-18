"""Write a function (with helper functions if needed) called to Excel that takes
an excel column value (A,B,C,D,...,AA,AB,AC,..., AAA...) and returns a corresponding
integer value (A=1,B=2,..., AA=26).
"""

import unittest

A = ord('A') - 1
Z = ord('Z')

def col2int(col):
  "Calculates the index of an Excel column"
  sum, i = 0, 0

  for char in col[::-1]:
    sum += (ord(char) - A) * pow(Z - A, i)
    i += 1

  return sum


class Col2intTest(unittest.TestCase):

  def test_function(self):
    self.assertEqual(col2int('A'), 1)
    self.assertEqual(col2int('B'), 2)
    self.assertEqual(col2int('C'), 3)
    self.assertEqual(col2int('Z'), 26)
    self.assertEqual(col2int('AA'), 27)
    self.assertEqual(col2int('AB'), 28)
    self.assertEqual(col2int('AC'), 29)
    self.assertEqual(col2int('AZ'), 52)
    self.assertEqual(col2int('BA'), 53)
    self.assertEqual(col2int('BB'), 54)
    self.assertEqual(col2int('BC'), 55)
    self.assertEqual(col2int('AAA'), 703)
    self.assertEqual(col2int('AAB'), 704)
    self.assertEqual(col2int('ABA'), 729)
    self.assertEqual(col2int('ABB'), 730)
    self.assertEqual(col2int('BBB'), 1406)
    self.assertEqual(col2int('BBB'), 1406)
    self.assertEqual(col2int('BET'), 1502)


if __name__ == '__main__':
  unittest.main()
