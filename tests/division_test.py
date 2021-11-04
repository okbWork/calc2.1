"""Testing Division"""

import unittest
from calc.calculations.division import Division


class MyTestCase(unittest.TestCase):
    """Class to test division without having a runtime error"""
    def setUp(self) -> None:
        """setting up the values of mynumbers"""
        self.mynumbers = None

    def test_calculation_division(self):
        """testing that our calculator has a static method for division"""
        # Arrange
        self.mynumbers = (1.0, 2.0)
        division = Division(self.mynumbers)
        # Act
        # Assert
        assert division.get_result() == 0.5

    def test_calculator_division_by_zero(self):
        """ testing dividing by 0"""
        self.mynumbers = (1.0, 0.0)
        with self.assertRaises(ZeroDivisionError):
            division = Division(self.mynumbers)
            assert division.get_result() == 0.0

if __name__ == '__main__':
    unittest.main()
