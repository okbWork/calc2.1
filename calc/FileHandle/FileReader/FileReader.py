import pandas as pd
from pathlib import Path

def absolutepath(filepath):
    relative = Path(filepath)
    return relative.absolute()

class FileReader:
    def __init__(self, filename):
        self.reader = pd.read_csv(absolutepath(filepath))
        self.arr = self.reader.values.tolist()
        self.row = 0
        self.fname = filename
    def get_next_row(self):
        if self.row < len(self.arr) - 1:
            self.row += 1
            return self.arr[self.row]
        else:
            return []
