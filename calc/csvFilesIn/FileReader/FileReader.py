import pandas as pd
class FileReader:
    def __init__(self, filename):
        self.name = filename
        self.pandas = pd.read_csv(filename)
        self.size = pandas.size
        self.curr = 0
    def readNextRow(self):
        return pandas.lo
