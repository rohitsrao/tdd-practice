import unittest
import random

def add(inp_str):
    if not inp_str:
        return 0
    elif len(inp_str) == 1:
        return int(inp_str)
    else:
        if inp_str[0:2] == '//':
            delimiter_str, num_str_list = inp_str.split(';')
            delimiter = delimiter_str[2:]
            num_list = [int(num) for num in num_str_list.split(delimiter)]
            negative_num_list = [num for num in num_list if num < 0]
            if negative_num_list:
                raise Exception('negatives not allowed - '.join(negative_num_list))
            return sum(num_list)
        else:
            if '\n' in inp_str:
                inp_str = inp_str.replace('\n',',')
            num_list = [int(num) for num in inp_str.split(',')]
            negative_num_list = [num for num in num_list if num < 0]
            if negative_num_list:
                raise Exception('negatives not allowed - '.join(negative_num_list))
            return sum(num_list)

class StringCalculatorTest(unittest.TestCase):

    def test_given_empty_string_returns_zero(self):
        self.assertEqual(add(''), 0)

    def test_given_one_as_input_returns_one(self):
        self.assertEqual(add('1'), 1)

    def test_given_two_as_input_returns_two(self):
        self.assertEqual(add('2'), 2)

    def test_given_one_and_two_as_input_returns_three(self):
        self.assertEqual(add('1,2'), 3)

    def test_given_any_two_numbers_as_input_returns_sum(self):
        self.assertEqual(add('300, 270'), 570)

    def test_given_three_numbers_as_input_return_sum(self):
        self.assertEqual(add('1,2,3'), 6)

    def test_give_7_numbers_as_input_return_sum(self):
        self.assertEqual(add('1,2,3,4,5,6,7'), 28)

    def test_given_two_newline_separted_values_return_sum(self):
        self.assertEqual(add('1\n2'), 3)

    def test_given_two_custom_delimiter_separated_values_return_sum(self):
        self.assertEqual(add('//>;1>2>3>4>5'), 15)

    def test_given_single_digit_negative_number_throw_exception(self):
        self.assertRaises(Exception, add, '-1')

    def test_given_minus_as_custom_delimiter_returns_sum(self):
        self.assertEqual(add('//-;1-2-3-4'), 10)

    def test_given_double_digit_negative_number_throw_exception(self):
        self.assertRaises(Exception, add, '-11')

if __name__ == '__main__':
    unittest.main()

