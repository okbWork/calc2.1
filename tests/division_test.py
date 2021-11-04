"""Testing Division"""
from calc.calculations.division import Division


"""Testing the Calculator"""
import unittest

from calc.calculations.division import Division


class MyTestCase(unittest.TestCase):
    def test_calculation_division(self):
        """testing that our calculator has a static method for addition"""
        # Arrange
        mynumbers = (1.0, 2.0)
        division = Division(mynumbers)
        # Act
        # Assert
        assert division.get_result() == 0.5

    def test_calculator_division_by_zero(self):
        """ testing dividing by 0"""
        mynumbers = (1.0, 0.0)
        with self.assertRaises(ZeroDivisionError):
            self.calculator.divide_numbers(mynumbers)


if __name__ == '__main__':
    unittest.main()