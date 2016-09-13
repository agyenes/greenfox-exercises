import unittest
from greeter import greeter

class TestGreeter(unittest.TestCase):

    def test_greeter_no_input(self):
        self.assertEqual(greeter(''), 'Hello, Mr Nobody!')

    def test_greeter_input_string(self):
        self.assertEqual(greeter('Bob'), 'Hello, Bob!')

if __name__ == '__main__':
    unittest.main()
