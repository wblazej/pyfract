import unittest
from pyfract.fraction import Fraction

class FractionTests(unittest.TestCase):
    def setUp(self) -> None:
        self.f1 = Fraction(1, 2)
        self.f2 = Fraction(1, 4)

    def test_addition(self):
        self.assertEqual(self.f1 + self.f2, Fraction(3, 4))
        self.assertEqual(self.f1 + 2, Fraction(5, 2))

    def test_subtraction(self):
        self.assertEqual(self.f1 - self.f2, Fraction(1, 4))
        self.assertEqual(self.f1 - 2, Fraction(-3, 2))

    def test_multiplication(self):
        self.assertEqual(self.f1 * self.f2, Fraction(1, 8))
        self.assertEqual(self.f1 * 2, Fraction(1, 1))

    def test_division(self):
        self.assertEqual(self.f1 / self.f2, Fraction(2, 1))
        self.assertEqual(self.f1 / 2, Fraction(1, 4))

    def test_less_than(self):
        self.assertEqual(self.f1 < self.f2, False)
        self.assertEqual(self.f1 < 2, True)
        self.assertEqual(self.f1 < 0.5, False)

    def test_less_or_equal(self):
        self.assertEqual(self.f1 <= self.f2, False)
        self.assertEqual(self.f1 <= 2, True)
        self.assertEqual(self.f1 <= 0.5, True)

    def test_greater_than(self):
        self.assertEqual(self.f1 > self.f2, True)
        self.assertEqual(self.f1 > 2, False)
        self.assertEqual(self.f1 > 0.5, False)

    def test_greater_or_equal(self):
        self.assertEqual(self.f1 >= self.f2, True)
        self.assertEqual(self.f1 >= 2, False)
        self.assertEqual(self.f1 >= 0.5, True)

    def test_equal(self):
        self.assertEqual(self.f1 == self.f2, False)
        self.assertEqual(self.f1 == self.f1, True)
        self.assertEqual(self.f1 == 0.5, True)

    def test_not_equal(self):
        self.assertEqual(self.f1 != self.f2, True)
        self.assertEqual(self.f1 != self.f1, False)
        self.assertEqual(self.f1 != 0.5, False)

    def test_from_float(self):
        testcases = [[1, 3], [18, 29], [6, 10], [24, 11], [192, 3920], [3901, 890934], [190383, 1093293]]

        for testcase in testcases:
            x = testcase[0]
            y = testcase[1]

            f = Fraction.from_float(x / y)
            self.assertEqual(f, Fraction(x, y))

    def test_from_float_accurately(self):
        testcases = [[1, 3], [18, 29], [6, 10], [24, 11], [192, 3920], [3901, 890934], [190383, 1093293]]

        for testcase in testcases:
            x = testcase[0]
            y = testcase[1]

            f = Fraction.from_float_accurately(x / y, accuracy=12)
            self.assertEqual(f, Fraction(x, y))

    def test_to_float(self):
        x = self.f1.to_float()
        self.assertEqual(x, 0.5)
        self.assertEqual(type(x), float)

        x = self.f2.to_float()
        self.assertEqual(x, 0.25)
        self.assertEqual(type(x), float)

if __name__ == "__main__":
    unittest.main()
