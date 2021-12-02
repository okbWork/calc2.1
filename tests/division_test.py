"""Testing Division"""

import unittest
from calc.calculations.division import Division
from calc.FileHandle.FileReader import FileReader
from calc.FileHandle.FileWriter import FileWriter
import time

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
            division.get_result()

    def test_calculation_multiplication_file():
        """testing that our calculator has a static method for division with addition file"""
        # Arrange
        filename = "./calc/FileHandle/testFiles/unreadFiles/DivisionTest.csv"
        filenameW = "./calc/FileHandle/testFiles/readFiles/DivisionTest.csv"
        filenameE = "./calc/FileHandle/testFiles/readFiles/Errors.csv"
        operation = "division,"
        fileR = FileReader(filename)
        fileW = FileWriter(filenameW)
        fileE = FileWriter(filenameE)
        line = fileR.get_next_row()
        res = True
        while line != []:
            # Act
            mynumbers = tuple(line[:len(line) - 1])
            division = Division(mynumbers)
            # Assert
            try:
                assert division.get_result() == line[-1]
            except:
                fileE.write_next_line(operation +" Dividing by Zero Error")
            # Arrange pt. 2
            fileW.write_next_line(operation + str(line[-1]))
            line = fileR.get_next_row()

    def test_calculation_multiplication_file_S():
        """testing that our calculator has a static method for division with simple addition file"""
        # Arrange
        filename = "./calc/FileHandle/testFiles/unreadFiles/DivisionTestSimple.csv"
        filenameW = "./calc/FileHandle/testFiles/readFiles/DivisionTestSimple.csv"
        operation = "division,"
        fileR = FileReader(filename)
        fileW = FileWriter(filenameW)
        line = fileR.get_next_row()
        res = True
        while line:
            # Act
            mynumbers = tuple(line[:len(line) - 1])
            division = Division(mynumbers)
            # Assert
            assert division.get_result() == line[-1]
            # Arrange pt. 2
            fileW.write_next_line(operation + str(line[-1]))
            line = fileR.get_next_row()
if __name__ == '__main__':
    unittest.main()
