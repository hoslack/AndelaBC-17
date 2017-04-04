import unittest
from prime import primenumber


class PrimeTests(unittest.TestCase):
    def test_result(self):
        result = primenumber(10)
        self.assertEqual(result, [0, 1, 2, 3, 5, 7])

    def test_result_is_list(self):
        result = primenumber(10)
        self.assertTrue(result, list)

    def test_integer(self):
        result = primenumber(str)
        self.assertTrue(result, TypeError)

    def test_negative(self):
        result = primenumber(-98)
        self.assertTrue(result, ValueError)

    def test_large_number(self):
        result = primenumber(100000)
        self.assertTrue(result, ValueError)


if __name__ == '__main__':
    unittest.main()
