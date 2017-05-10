import unittest

from eternal.main import calculate, main

"""
Run with PYTHONPATH=. python tests/test_dummy.py
"""


class TestDummy(unittest.TestCase):

    def test_fun(self):
        weekday = calculate(2017, 5, 8)
        self.assertEqual(weekday, 0)

        weekday = calculate(1648, 5, 8)
        self.assertEqual(weekday, 0)

        weekday = calculate(1790, 5, 8)
        self.assertEqual(weekday, 6)

        weekday = calculate(1000, 15, 1)
        self.assertEqual(weekday, -1)

        weekday = calculate(1000, 15, 0)
        self.assertEqual(weekday, -1)

        weekday = calculate(1000, 7, -13)
        self.assertEqual(weekday, -1)

        weekday = calculate(1000, 7, 40)
        self.assertEqual(weekday, -1)

        weekday = calculate(2000, 2, 30)
        self.assertEqual(weekday, -1)
        
        weekday = calculate(2000, -2, 30)
        self.assertEqual(weekday, -1)


        retcode = main(("--year", "2001", "--month", "1", "--day", "3"))
        self.assertEqual(retcode, 0)
        retcode = main(("--year", "2001", "--month", "1"))
        self.assertEqual(retcode, 1)


if __name__ == '__main__':
    unittest.main()
