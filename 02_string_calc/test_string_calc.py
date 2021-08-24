import unittest

def add(inp_str):
    return 0

class StringCalculatorTest(unittest.TestCase):

    def test_given_empty_string_returns_zero(self):
        self.assertEqual(add(''), 0)

if __name__ == '__main__':
    unittest.main()

