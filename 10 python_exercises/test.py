import unittest
import extend

class TestExtend(unittest.TestCase):
    def setUp(self):
        pass

    def test_add_2_and_4_is_5(self):
        self.assertEqual(extend.add(2, 4), 6)

    def test_add_4_and_1_is_5(self):
        self.assertEqual(extend.add(4, 1), 5)

    def test_max_of_three_first(self):
        self.assertEqual(extend.max_of_three(5, 4, 6), 6)

    def test_max_of_three_third(self):
        self.assertEqual(extend.max_of_three(3, 7, 5), 7)

    def test_median_four(self):
        self.assertEqual(extend.median([7,5,3,8]), 6.5)

    def test_median_five(self):
        self.assertEqual(extend.median('derrr'), '')

    def test_is_vovel_a(self):
        self.assertEqual(extend.is_vovel('7'), False)

    def test_is_vovel_u(self):
        self.assertEqual(extend.is_vovel('[5, 8, 2]'), False)

    def test_translate_bemutatkozik(self):
        self.assertEqual(extend.translate('7'), '7')

    def test_translate_kolbice(self):
        self.assertEqual(extend.translate('kölbice'), 'kövölbiviceve')

if __name__ == '__main__':
    unittest.main()
