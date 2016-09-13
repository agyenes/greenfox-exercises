from third import filter_smaller_than_number
import unittest

class FilterTest(unittest.TestCase):
  def test_input_not_a_list(self):
    self.assertEqual(filter_smaller_than_number(67.6, 5), [])

  def test_all_list_elements_are_smaller_than_number(self):
    self.assertEqual(filter_smaller_than_number([2, 5, 7, 9, 11], 10), [2, 5, 7, 9])

  def test_some_list_elements_are_smaller_than_number(self):
    self.assertEqual(filter_smaller_than_number([2, 5, 7, 9, 11], 17), [2, 5, 7, 9, 11])

  def test_no_list_elements_are_smaller_than_number(self):
    self.assertEqual(filter_smaller_than_number([2, 5, 7, 9, 11], 1), [])

  def test_filter_smaller_than_a_letter(self):
    self.assertEqual(filter_smaller_than_number([2, 5, 7, 9, 11], 'f'), TypeError)

if __name__ == '__main__':
    unittest.main()
