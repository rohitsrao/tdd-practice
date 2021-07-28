import unittest

from fizz_buzz import FizzBuzz

class FizzBuzzTest(unittest.TestCase):

    def test_fizz_buzz_of_1_returns_1(self):
        self.assertEqual(FizzBuzz(1), 1)

    def test_fizz_buzz_of_2_returns_2(self):
        self.assertEqual(FizzBuzz(2), 2)

    def test_fizz_bizz_of_3_returns_fizz(self):
        self.assertEqual(FizzBuzz(3), 'Fizz')

    def test_fizz_bizz_of_4_returns_4(self):
        self.assertEqual(FizzBuzz(4), 4)
    
    def test_fizz_bizz_of_5_returns_buzz(self):
        self.assertEqual(FizzBuzz(5), 'Buzz')

    def test_fizz_bizz_of_6_returns_fizz(self):
        self.assertEqual(FizzBuzz(6), 'Fizz')

    def test_fizz_bizz_of_10_returns_buzz(self):
        self.assertEqual(FizzBuzz(10), 'Buzz')

    def test_fizz_bizz_of_15_returns_fizzbuzz(self):
        self.assertEqual(FizzBuzz(15), 'FizzBuzz')

if __name__ == '__main__':
    unittest.main()
