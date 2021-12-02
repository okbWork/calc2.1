"""Testing Multiplication"""
from calc.calculations.multiplication import Multiplication
from calc.FileHandle.FileReader import FileReader
from calc.FileHandle.FileWriter import FileWriter

def test_calculation_multiplication():
    """testing that our calculator has a static method for multiplication"""
    #Arrange
    mynumbers = (1.0,2.0)
    multiplication = Multiplication(mynumbers)
    #Act
    #Assert
    assert multiplication.get_result() == 2

def test_calculation_multiplication_file():
    """testing that our calculator has a static method for multiplication with addition file"""
    #Arrange
    filename = "./calc/FileHandle/testFiles/unreadFiles/MultTest.csv"
    filenameW = "./calc/FileHandle/testFiles/readFiles/MultTest.csv"
    operation = "multiplication,"
    fileR = FileReader(filename)
    fileW = FileWriter(filenameW)
    line = fileR.get_next_row()
    res = True
    while line:
        #Act
        mynumbers = tuple(line[:len(line)-1])
        multiplication = Multiplication(mynumbers)
        #Assert
        assert multiplication.get_result() == line[-1]
        #Arrange pt. 2
        fileW.write_next_line(operation + str(line[-1]))
        line = fileR.get_next_row()

def test_calculation_multiplication_file_S():
    """testing that our calculator has a static method for multiplication with simple addition file"""
    #Arrange
    filename = "./calc/FileHandle/testFiles/unreadFiles/MultTestSimple.csv"
    filenameW = "./calc/FileHandle/testFiles/readFiles/MultTestSimple.csv"
    operation = "multiplication,"
    fileR = FileReader(filename)
    fileW = FileWriter(filenameW)
    line = fileR.get_next_row()
    res = True
    while line != []:
        #Act
        mynumbers = tuple(line[:len(line)-1])
        multiplication = Multiplication(mynumbers)
        #Assert
        assert multiplication.get_result() == line[-1]
        #Arrange pt. 2
        fileW.write_next_line(operation + str(line[-1]))
        line = fileR.get_next_row()