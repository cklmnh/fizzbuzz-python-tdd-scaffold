import unittest
from FizzBuzz import fizz_buzz


class Tfb(unittest.TestCase):
    def test_input_normal(self):
        self.assertEqual(fizz_buzz(1), "1")

    def test_input_3_5(self):
        self.assertEqual(fizz_buzz(15), "FizzBuzz")

    def test_input_3(self):
        self.assertEqual(fizz_buzz(3), "Fizz")

    def test_input_5(self):
        self.assertEqual(fizz_buzz(5), "Buzz")

if __name__ == "main":
    unittest.main()
