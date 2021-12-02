"""Testing Subtraction"""
from calc.calculations.subtraction import Subtraction
from calc.FileHandle.FileReader import FileReader
from calc.FileHandle.FileWriter import FileWriter

def test_calculation_subtraction():
    """testing that our calculator has a static method for subtraction"""
    #Arrange
    mynumbers = (1.0,2.0)
    subtraction = Subtraction(mynumbers)
    #Act
    #Assert
    assert subtraction.get_result() == -3

def test_calculation_multiplication_file():
    """testing that our calculator has a static method for subtraction with addition file"""
    #Arrange
    filename = "./calc/FileHandle/testFiles/unreadFiles/SubtractionTest.csv"
    filenameW = "./calc/FileHandle/testFiles/readFiles/SubtractionTest.csv"
    operation = "subtraction,"
    fileR = FileReader(filename)
    fileW = FileWriter(filenameW)
    line = fileR.get_next_row()
    res = True
    while line:
        #Act
        mynumbers = tuple(line[:len(line)-1])
        subtraction = Subtraction(mynumbers)
        #Assert
        assert subtraction.get_result() == line[-1]
        #Arrange pt. 2
        fileW.write_next_line(operation + str(line[-1]))
        line = fileR.get_next_row()

def test_calculation_multiplication_file_S():
    """testing that our calculator has a static method for subtraction with simple addition file"""
    #Arrange
    filename = "./calc/FileHandle/testFiles/unreadFiles/SubtractionTestSimple.csv"
    filenameW = "./calc/FileHandle/testFiles/readFiles/SubtractionTestSimple.csv"
    operation = "subtraction,"
    fileR = FileReader(filename)
    fileW = FileWriter(filenameW)
    line = fileR.get_next_row()
    res = True
    while line != []:
        #Act
        mynumbers = tuple(line[:len(line)-1])
        subtraction = Subtraction(mynumbers)
        #Assert
        assert subtraction.get_result() == line[-1]
        #Arrange pt. 2
        fileW.write_next_line(operation + str(line[-1]))
        line = fileR.get_next_row()