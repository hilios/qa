"""Write a function that receives two quadratic matrixes of integers, and the
given column  where a particular number appears in each, and return one of the
following:
A) The exact number;
B) The possible numbers;
C) An exception where no matches found.
"""


import unittest
from random import randint


def col(matrix, col):
  c = []
  n = int(len(matrix) ** 0.5)
  for i in range(n):
    c.append(matrix[(col - 1) + (n * i)])

  return c


def predict(matrix1, col1, matrix2, col2):
  p = []
  col1 = col(matrix1, col1)
  col2 = col(matrix2, col2)

  for i in range(len(col1)):
    if col1[i] in col2:
      p.append(col1[i])

  if len(p) == 0:
    raise Exception("No matches found!")

  return p


class MagicTest(unittest.TestCase):

  def random_matrix_helper(self, n=4):
    N = int(n ** 2)
    mtx = []
    while len(mtx) < N:
      num = randint(1, N)
      if not num in mtx:
        mtx.append(num)
    print(mtx)

  def setUp(self):
    self.m1 = [
      10, 14,  9,  3,
       8,  7,  4,  1,
      11, 16,  2, 12,
       5, 13, 15,  6,
    ]

    self.m2 = [
      13,  7, 10,  4,
       6,  5, 14, 12,
       2, 16,  3, 15,
       8, 11,  9,  1,
    ]


  def test_col(self):
    self.assertEqual(col(self.m1, 1), [10, 8, 11, 5])
    self.assertEqual(col(self.m2, 2), [7, 5, 16, 11])


  def test_magic(self):
    self.assertEqual(predict(self.m1, 1, self.m2, 1), [8])
    self.assertEqual(predict(self.m1, 2, self.m2, 3), [14])
    self.assertEqual(predict(self.m1, 2, self.m2, 2), [7, 16])
    # Test error
    self.assertRaises(Exception, predict(self.m1, 2, self.m2, 3))


if __name__ == '__main__':
  unittest.main()
