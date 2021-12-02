"""Testing Addition"""
from calc.calculations.addition import Addition
from calc.FileHandle.FileReader import FileReader
from calc.FileHandle.FileWriter import FileWriter

def test_calculation_addition():
    """testing that our calculator has a static method for addition"""
    #Arrange
    mynumbers = (1.0,2.0)
    addition = Addition(mynumbers)
    #Act
    #Assert
    assert addition.get_result() == 3.0

def test_calculation_addition_file():
    """testing that our calculator has a static method for addition with addition file"""
    #Arrange
    filename = "./calc/FileHandle/testFiles/unreadFiles/AdditionTest.csv"
    filenameW = "./calc/FileHandle/testFiles/readFiles/AdditionTest.csv"
    operation = "addition,"
    fileR = FileReader(filename)
    fileW = FileWriter(filenameW)
    line = fileR.get_next_row()
    res = True
    while line:
        #Act
        mynumbers = tuple(line[:len(line)-1])
        addition = Addition(mynumbers)
        #Assert
        assert addition.get_result() == line[-1]
        #Arrange pt. 2
        fileW.write_next_line(operation + str(line[-1]))
        line = fileR.get_next_row()

def test_calculation_addition_file_S():
    """testing that our calculator has a static method for addition with simple addition file"""
    #Arrange
    filename = "./calc/FileHandle/testFiles/unreadFiles/AdditionTestSimple.csv"
    filenameW = "./calc/FileHandle/testFiles/readFiles/AdditionTestSimple.csv"
    operation = "addition,"
    fileR = FileReader(filename)
    fileW = FileWriter(filenameW)
    line = fileR.get_next_row()
    res = True
    while line != []:
        #Act
        mynumbers = tuple(line[:len(line)-1])
        addition = Addition(mynumbers)
        #Assert
        assert addition.get_result() == line[-1]
        #Arrange pt. 2
        fileW.write_next_line(operation + str(line[-1]))
        line = fileR.get_next_row()
