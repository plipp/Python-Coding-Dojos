# test with: python -m unittest unittest_sample.py
import unittest


def divide(a, b):
    return a / b


class BasicArithmeticTest(unittest.TestCase):
    def test_divide(self):
        self.assertEqual(divide(10, 5), 2)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)


# ... and much more: see https://docs.python.org/3/library/unittest.html#module-unittest
