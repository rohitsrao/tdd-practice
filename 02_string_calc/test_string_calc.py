import unittest

class StringCalculator:

    def add(self, inp_str):
        if isinstance(inp_str, str):
            if not inp_str:
                return 0
            elif len(inp_str) == 1:
                return int(inp_str)
            else:
                a, b = inp_str.split(',')
                return int(a) + int(b)
        else:
            return -1

class StringCalculatorTest(unittest.TestCase):

    def setUp(self):
        self.str_calc = StringCalculator()

    def test_given_non_string_input_return_minus_one(self):
        result = self.str_calc.add(5)
        self.assertEqual(result, -1)

    def test_given_empty_string_returns_zero(self):
        result = self.str_calc.add('')
        self.assertEqual(result, 0)

    def test_given_single_string_input_return_input(self):
        result = self.str_calc.add('3')
        self.assertEqual(result, 3)

    def test_given_two_comma_separated_numbers_as_input_returns_sum(self):
        result = self.str_calc.add('6,5')
        self.assertEqual(result, 11)

if __name__ == '__main__':
    unittest.main()

