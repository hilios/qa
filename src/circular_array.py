import unittest


def binary_search(lst, q):

  low, high = 0, len(lst) - 1

  while low <= high:
    mid = int((low + high) / 2)

    if q == lst[mid]:
      return mid

    if lst[mid] <= lst[high]:
      if lst[mid] < q <= lst[high]:
        low = mid + 1
      else:
        high = mid - 1
    else:
      if lst[low] < q <= lst[mid]:
        high = mid + 1
      else:
        low = mid - 1

  return -1


class CircularBinarySearch(unittest.TestCase):

  def setUp(self):
    self.circ = [38, 40, 55, 89, 6, 13, 20, 23, 36]


  def test_find_index(self):
    i = binary_search(self.circ, 13)
    self.assertEqual(self.circ[i], 13)
    self.assertEqual(i, 5)


  def test_not_found(self):
    i = binary_search(self.circ, 0)
    self.assertEqual(i, -1)


if __name__ == '__main__':
  unittest.main()
