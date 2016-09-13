from third import filter_smaller_than_number
import unittest

class FilterTest(unittest.TestCase):
  def test_input_not_list(self):
    self.assertEqual(filter_smaller_than_number(67.6, 5), [])

  def test_some_items_filtered(self):
    self.assertEqual(filter_smaller_than_number([2, 5, 7, 9, 11], 10), [2, 5, 7, 9])

  def test_no_items_filtered(self):
    self.assertEqual(filter_smaller_than_number([2, 5, 7, 9, 11], 17), [2, 5, 7, 9, 11])

  def test_all_items_filtered(self):
    self.assertEqual(filter_smaller_than_number([2, 5, 7, 9, 11], 1), [])

if __name__ == '__main__':
    unittest.main()
