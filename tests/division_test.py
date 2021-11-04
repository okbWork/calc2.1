"""Testing Division"""

import unittest
from calc.calculations.division import Division


class MyTestCase(unittest.TestCase):
    """Class to test division without having a runtime error"""
    def test_calculation_division(self):
        """testing that our calculator has a static method for division"""
        # Arrange
        mynumbers = (1.0, 2.0)
        self.division = Division(mynumbers)
        # Act
        # Assert
        assert self.division.get_result() == 0.5

    def test_calculator_division_by_zero(self):
        """ testing dividing by 0"""
        mynumbers = (1.0, 0.0)
        with self.assertRaises(ZeroDivisionError):
            self.Division(mynumbers)


if __name__ == '__main__':
    unittest.main()
