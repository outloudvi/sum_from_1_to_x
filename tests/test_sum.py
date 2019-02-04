"""
 Unittest part.
"""

import unittest
from sumfrom import sum_from_one_to_x


class SumTest(unittest.TestCase):
    """
    Testcases.
    """
    def test_numbers(self):
        """
        Basic tests.
        """
        self.assertEqual(sum_from_one_to_x(3), 6)
        self.assertEqual(sum_from_one_to_x(1), 1)
        self.assertEqual(sum_from_one_to_x(9), 45)

    def test_error(self):
        """
        Edge case tests.
        """
        with self.assertRaises(NotImplementedError):
            sum_from_one_to_x(-1)
        with self.assertRaises(TypeError):
            sum_from_one_to_x(1.3)


if __name__ == "__main__":
    unittest.main()
