import unittest

class NegativeNumberException(Exception):

    def __init__(self, negative_num_list):
       self.msg = 'negative numbers not allowed - ' + str(negative_num_list)
       super().__init__(self.msg)

def compute_sum(num_int_list):
    sum = 0
    for num in num_int_list:
        if num < 1000:
            sum += num
    return sum

def convert_str_list_to_int(inp_str):
    return [int(num) for num in inp_str.split(',')]

def extract_custom_delimiter(inp_str):
    delimiter_str, num_str = inp_str.split('\n')
    delimiter_str = delimiter_str[2:]
    delimiters = []
    if ']' in delimiter_str:
        delimiter_str_split = delimiter_str.split(']')
        del delimiter_str_split[-1]
        for delimiter in delimiter_str_split:
            delimiters.append(delimiter[1:])
    else: 
        delimiters.append(delimiter_str)
    return delimiters, num_str

def replace_delimiter_with_comma(num_str, delimiters):
    for delimiter in delimiters:
        num_str = num_str.replace(delimiter, ',')
    return num_str

def filter_negative_numbers(num_int_list):
    negative_num_list = [num for num in num_int_list if num < 0]
    return negative_num_list

def add(inp_str):
    if not inp_str:
        return 0
    else: 
        num_str_list = None
        
        if inp_str[0:2] == '//':
            delimiters, num_str_list = extract_custom_delimiter(inp_str)
            num_str_list = replace_delimiter_with_comma(num_str_list, delimiters)
        else:
            num_str_list = replace_delimiter_with_comma(inp_str, '\n')
        
        num_int_list = convert_str_list_to_int(num_str_list)
        negative_num_list = filter_negative_numbers(num_int_list)
        if negative_num_list:
            raise NegativeNumberException(negative_num_list)
        else:
            return compute_sum(num_int_list)

class TestStringCalc(unittest.TestCase):

    def test_given_empty_string_returns_0(self):
        self.assertEqual(add(''), 0)

    def test_given_one_as_input_return_one(self):
        self.assertEqual(add('1'), 1)

    def test_given_two_as_input_return_two(self):
        self.assertEqual(add('2'), 2)

    def test_given_two_comma_separated_numbers_return_sum(self):
        self.assertEqual(add('2,3'), 5)

    def test_given_multiple_comma_separated_numbers_return_sum(self):
        self.assertEqual(add('1,2,3,4,5'), 15)

    def test_given_newline_separated_values_return_sum(self):
        self.assertEqual(add('45\n50'), 95)

    def test_give_two_custom_delimiter_separated_value_return_sum(self):
        self.assertEqual(add('//;\n13;14;15'), 42)

    def test_given_single_negative_number_raise_NegativeNumberException(self):
        self.assertRaises(NegativeNumberException, add, '-1')

    def test_given_multiple_negative_numbers_raise_NegativeNumberException(self):
        self.assertRaises(NegativeNumberException, add, '-23,-56,-77')

    def test_give_mix_of_positive_and_negative_numbers_raises_NegativeNumberException(self):
        self.assertRaises(NegativeNumberException, add, '-1,1,-2,2')

    def test_computes_sum_by_ignoring_numbers_greater_than_1000(self):
        self.assertEqual(add('1500,3'), 3)

    def test_custom_delimiters_of_random_length(self):
        self.assertEqual(add('//****\n20****30****40****10'), 100)

    def test_computes_sum_given_multiple_delimiters(self):
        self.assertEqual(add('//[,][;]\n1,2,3;4'), 10)

    def test_given_multiple_custom_delimiters_of_different_length_computes_sum(self):
        self.assertEqual(add('//[,][///][*****][;]\n43,22,55///99*****33///11'), 263)

    def test_given_multiple_custom_leimiters_with_negative_values_raises_NegativeNumberException(self):
        self.assertRaises(NegativeNumberException, add, '//[,][///][*****][;]\n43,22,55///99*****33///-11')

if __name__ == '__main__':
    unittest.main()
