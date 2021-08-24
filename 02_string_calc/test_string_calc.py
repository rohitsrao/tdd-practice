import unittest

def add(inp_str):
    if not inp_str:
        return 0
    return int(inp_str)

class StringCalculatorTest(unittest.TestCase):

    def test_given_empty_string_returns_zero(self):
        self.assertEqual(add(''), 0)

    def test_given_one_as_input_returns_one(self):
        self.assertEqual(add('1'), 1)

    def test_given_two_as_input_returns_two(self):
        self.assertEqual(add('2'), 2)

if __name__ == '__main__':
    unittest.main()

