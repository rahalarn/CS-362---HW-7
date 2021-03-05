import unittest
import leapYear

class TestLeap(unittest.TestCase):
    def test1(self):
        self.assertIs(leapYear.leap_year(2021), False)

    def test2(self):
        self.assertIs(leapYear.leap_year(400), True)


if __name__ == '__main__':
    unittest.main(verbosity = 2)
