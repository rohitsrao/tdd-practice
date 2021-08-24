import unittest

class StringCalculator:

    def add(self, inp_str):
        if not inp_str:
            return 0

class StringCalculatorTest(unittest.TestCase):

    def setUp(self):
        self.str_calc = StringCalculator()

    def test_given_empty_string_returns_zero(self):
        result = self.str_calc.add('')
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()

