import unittest

class NegativeNumberException(Exception):

    def __init__(self):
        self.message = 'Negative Number Detected'
    
class StringCalculator:

    def check_and_filter_negative_numbers(self, list_of_num):
        negative_num_list = []
        for num in list_of_num:
            if num < 0:
                raise NegativeNumberException()
                negative_num_list.append(num)
                list_of_num.remove(num)
        if not negative_num_list: 
            print(negative_num_list)
        return list_of_num, negative_num_list

    def splitByDelimiter(self, input_list, delimiter):
        list_of_num = input_list.split(delimiter)
        list_of_num = [int(num_str) for num_str in list_of_num]
        positive_num_list, negative_num_list = self.check_and_filter_negative_numbers(list_of_num)
        return positive_num_list

    def add(self, inp_str):
        if isinstance(inp_str, str):
            if not inp_str:
                return 0
            elif len(inp_str) == 1:
                return int(inp_str)
            else:
                if (inp_str[0:2] == '//'):
                    delimiter_str, list_of_num = inp_str.split('\n', 1)
                    delimiter = delimiter_str[2:]
                    positive_num_list = self.splitByDelimiter(list_of_num, delimiter)
                    return sum(positive_num_list)
                else:
                    if(',' in inp_str):
                        positive_num_list = self.splitByDelimiter(inp_str, ',')
                        return sum(positive_num_list)
                    if('\n' in inp_str):
                        positive_num_list = self.splitByDelimiter(inp_str, '\n')
                        return sum(positive_num_list)
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

    def test_given_two_comma_separated_numbers_returns_sum(self):
        result = self.str_calc.add('6,5')
        self.assertEqual(result, 11)

    def test_given_three_comma_separated_numbers_return_sum(self):
        result = self.str_calc.add('1,2,3')
        self.assertEqual(result, 6)

    def test_given_seven_comma_separated_numbers_return_sum(self):
        result = self.str_calc.add('1,2,3,4,5,6,7')
        self.assertEqual(result, 28)

    def test_given_two_newline_separated_numbers_return_sum(self):
        result = self.str_calc.add('1\n2')
        self.assertEqual(result, 3)

    def test_given_give_newline_separated_numbers_return_sum(self):
        result = self.str_calc.add('10\n20\n30\n40\n50')
        self.assertEqual(result, 150)

    def test_given_two_numbers_separted_with_custom_delimiter_return_sum(self):
        result = self.str_calc.add('//;\n1;2')
        self.assertEqual(result, 3)

    def test_when_one_input_number_is_negative_throws_NegativeNumberException(self):
        self.assertRaises(NegativeNumberException, self.str_calc.add, '2,-5')


if __name__ == '__main__':
    unittest.main()

