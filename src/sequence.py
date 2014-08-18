"""Write a function that evaluates if a given number is a sequence, i.e.:
- Fibonacci: 1123581321 => 1, 1, 2, 3, 5, 8, 13, 21, ...
- 11314173148 => 11, 3, 14, 17, 31, 48, ...
"""


import unittest


def is_sequence(seq):
  for i in range(1, len(seq)):
    for j in range(i + 1, len(seq)):
      ni = int(seq[0:i])
      nj = int(seq[i:j])
      test = str(ni) + str(nj)
      while len(test) < len(seq):
        next = ni + nj
        ni = nj
        nj = next
        test += str(next)
      if test == seq:
        return True
  return False


class IsSequenceTest(unittest.TestCase):
  def test_is_sequence(self):
    self.assertTrue(is_sequence('1123581321'))
    self.assertTrue(is_sequence('11314173148'))

  def test_is_not_sequence(self):
    self.assertFalse(is_sequence('1111111111'))
    self.assertFalse(is_sequence('1123581322'))


if __name__ == '__main__':
  unittest.main()
