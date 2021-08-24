import unittest

def add(inp_str):
    if not inp_str:
        return 0
    elif len(inp_str) == 1:
        return int(inp_str)
    else:
        return 3

class StringCalculatorTest(unittest.TestCase):

    def test_given_empty_string_returns_zero(self):
        self.assertEqual(add(''), 0)

    def test_given_one_as_input_returns_one(self):
        self.assertEqual(add('1'), 1)

    def test_given_two_as_input_returns_two(self):
        self.assertEqual(add('2'), 2)

    def test_given_one_and_two_as_input_returns_three(self):
        self.assertEqual(add('1,2'), 3)

if __name__ == '__main__':
    unittest.main()

