"""Given a array of numbers, output the array like this:
a1 <= a2 >= a3 <= a4 >= a5...
"""


import unittest


def print_list(alist):
  out = ''

  for i in range(len(alist)):
    if i > 0:
      out += (' <' if i % 2 else ' >') + '= '

    out += str(alist[i])

  return out


class OutputTest(unittest.TestCase):

  def setUp(self):
    self.array = range(1, 5 + 1)

  def test_output(self):
    output = print_list(self.array)
    self.assertEqual(output, '1 <= 2 >= 3 <= 4 >= 5')


if __name__ == '__main__':
  unittest.main()
