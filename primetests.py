import unittest
from prime import primenumber


class PrimeTests(unittest.TestCase):
    def test_result(self):
        result = primenumber(10)
        self.assertEqual(result, [0, 1, 2, 3, 5, 7])

    def test_result_is_list(self):
        result = primenumber(10)
        self.assertTrue(result, list)


if __name__ == '__main__':
    unittest.main()
