import unittest

from todo import usage, menu, list_function, add_task, remove_task, check_task, uncheck_task

class tests(unittest.TestCase):
    def test_list_function(self):
        self.assertEqual(list_function(), '')


if __name__ == '__main__':
    unittest.main()
