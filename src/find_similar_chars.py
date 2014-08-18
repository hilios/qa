"""Write a function f(a, b) which takes two character string arguments and
returns a string containing only the characters found in both strings in the
order of a. Write a version which is order N-squared and one which is order N.
"""


import unittest


def find_similar_chars_n_sqr(str1, str2):
  """Returns a string containing only the characters found in both strings
  Complexity: O(N^2)
  """
  similars = []

  for char1 in str1:
    for char2 in str2:
      if char1 is char2:
        similars.append(char1)

  return ''.join(sorted(similars))


def find_similar_chars_n(str1, str2):
  """Returns a string containing only the characters found in both strings
  Complexity: O(N)
  """
  return ''.join(sorted([char1 for char1 in str1 if char1 in str2]))


def find_similar_chars_set(str1, str2):
  """Returns a string containing only the characters found in both strings
  Complexity: O(N)
  """
  return ''.join(sorted(set(str1) & set(str2)))


class FindSimilarChars(unittest.TestCase):

  def test_find_chars_n_sqr(self):
    similars = find_similar_chars_n_sqr('abcd', 'bcde')
    self.assertEqual(similars, 'bcd')


  def test_find_chars_n(self):
    similars = find_similar_chars_n('abcd', 'bcde')
    self.assertEqual(similars, 'bcd')


  def test_find_chars_n(self):
    similars = find_similar_chars_set('abcd', 'bcde')
    self.assertEqual(similars, 'bcd')


  def test_sorting(self):
    ordered = find_similar_chars_n_sqr('bacd', 'bacd')
    self.assertEqual(ordered, 'abcd')

    ordered = find_similar_chars_n('bacd', 'bacd')
    self.assertEqual(ordered, 'abcd')

    ordered = find_similar_chars_set('bacd', 'bacd')
    self.assertEqual(ordered, 'abcd')


  def test_no_find(self):
    n_sqr = find_similar_chars_n_sqr('abc', 'def')
    self.assertEqual(n_sqr, '')

    n = find_similar_chars_n('abc', 'def')
    self.assertEqual(n, '')

    aset = find_similar_chars_set('abc', 'def')
    self.assertEqual(aset, '')


if __name__ == '__main__':
    unittest.main()
