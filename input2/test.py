# test de fonctions de year.py

# imports
from year import validate_year
import unittest

# x = validate_year("96")
# print(x)


class ValidateYearTest(unittest.TestCase):
    """Tests for validate_year() from year.py"""

    def test(self):
        x = validate_year("50")
        self.assertEqual(x, 1950)


if __name__ == "__main__":
    unittest.main()
