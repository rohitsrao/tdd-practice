import unittest

letters = {
    1: {
        1: 'I',
        5: 'V'
    },
    2: {
        1: 'X',
        5: 'L'
    },
    3: {
        1: 'C',
        5: 'D'
    },
    4: {
        1: 'M'
    }
}

def repeat_numeral(start_str, numeral_to_repeat, num_repeat):
    updated_num = start_str
    for i in range(num_repeat):
        updated_num += numeral_to_repeat
    return updated_num 

def extract_digits(num):
    digits = [int(str_digit) for str_digit in str(num)]
    return digits

def extract_remaining_digits(digits):
    remaining_digits = [str(digit) for digit in digits[1:]]
    remaining_digits = ''.join(remaining_digits)
    remaining_digits = int(remaining_digits)
    return remaining_digits

def convert(num):
    digits = extract_digits(num)
    digit_index = len(digits)
    if digit_index == 4:
        first_digit = repeat_numeral('', letters[digit_index][1], digits[0])
    else:
        if digits[0] < 4:
            first_digit = repeat_numeral('', letters[digit_index][1], digits[0])
        elif digits[0] == 4:
            first_digit = repeat_numeral(letters[digit_index][1], letters[digit_index][5], 1)
        elif 5 <= digits[0] < 9:
            first_digit = repeat_numeral(letters[digit_index][5], letters[digit_index][1], digits[0] - 5)
        elif digits[0] == 9:
            first_digit = repeat_numeral(letters[digit_index][1], letters[digit_index+1][1], 1)

    if digit_index == 1:
        return first_digit
    else:
        remaining_digits = extract_remaining_digits(digits)
        return first_digit + convert(remaining_digits)

class TestRomanNumberGenerator(unittest.TestCase):

    def test_given_1_return_I(self):
        self.assertEqual(convert(1), 'I')

    def test_given_2_return_II(self):
        self.assertEqual(convert(2), 'II')

    def test_given_4_return_IV(self):
        self.assertEqual(convert(4), 'IV')

    def test_given_5_return_V(self):
        self.assertEqual(convert(5), 'V')

    def test_given_9_return_IX(self):
        self.assertEqual(convert(9), 'IX')

    def test_given_10_return_X(self):
        self.assertEqual(convert(10), 'X')

    def test_given_11_return_XI(self):
        self.assertEqual(convert(11), 'XI')

    def test_given_14_return_XIV(self):
        self.assertEqual(convert(14), 'XIV')

    def test_given_45_return_XLV(self):
        self.assertEqual(convert(45), 'XLV')

    def test_given_50_return_L(self):
        self.assertEqual(convert(50), 'L')

    def test_given_69_return_LXIX(self):
        self.assertEqual(convert(69), 'LXIX')

    def test_given_90_return_XC(self):
        self.assertEqual(convert(90), 'XC')

    def test_given_93_return_XCIII(self):
        self.assertEqual(convert(93), 'XCIII')
    
    def test_given_100_return_C(self):
        self.assertEqual(convert(100), 'C')

    def test_given_101_return_CI(self):
        self.assertEqual(convert(101), 'CI')

    def test_given_200_returns_CC(self):
        self.assertEqual(convert(200), 'CC')

    def test_given_400_returns_CD(self):
        self.assertEqual(convert(400), 'CD')

    def test_given_500_return_D(self):
        self.assertEqual(convert(500), 'D')

    def test_given_1000_return_M(self):
        self.assertEqual(convert(1000), 'M')

    def test_given_2021_return_MMXXI(self):
        self.assertEqual(convert(2021), 'MMXXI')

if __name__ == '__main__':
    unittest.main()
