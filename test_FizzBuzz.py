import unittest
import FizzBuzz

class TestFizz(unittest.TestCase):
    def test1(self):   #testing for Fizz and Buzz
        self.assertIs(FizzBuzz.fizz(), "1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 15 16 17 Fizz 19 Buzz Fizz 22 23 Fizz Buzz 26 Fizz 28 29 30 31 32 Fizz 34 Buzz Fizz 37 38 Fizz Buzz 41 Fizz 43 44 45 46 47 Fizz 49 Buzz Fizz 52 53 Fizz Buzz 56 Fizz 58 59 60 61 62 Fizz 64 Buzz Fizz 67 68 Fizz Buzz 71 Fizz 73 74 75 76 77 Fizz 79 Buzz Fizz 82 83 Fizz Buzz 86 Fizz 88 89 90 91 92 Fizz 94 Buzz Fizz 97 98 Fizz Buzz")


if __name__ == '__main__':
   unittest.main(verbosity = 2)