import pandas as pd
from pathlib import Path

def absolutepath(filepath):
    """get the absolute path of a file"""
    relative = Path(filepath)
    return relative.absolute()

class FileReader:
    def __init__(self, filename):
        """Create a class to read a csv file"""
        self.reader = pd.read_csv(absolutepath(filename))
        self.arr = self.reader.values.tolist()
        self.row = -1
        self.fname = filename
    def get_next_row(self):
        """read the next row of a csv file"""
        if self.row < len(self.arr) - 1:
            self.row += 1
            return self.arr[self.row]
        else:
            return []
