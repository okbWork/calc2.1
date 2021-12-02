from pathlib import Path
import pandas as pd
import time
"""Write csv Files to a Folder"""

def absolutepath(filepath):
    """get the absolute file path of a relative file"""
    relative = Path(filepath)
    return relative.absolute()

class FileWriter:
    def __init__(self, fname):
        """Constructor for FileWriter Object"""
        self.path = absolutepath(apath)
        self.filename = fname
        self.writeList = []
        self.row = 0

    def write_next_line(self, statement):
        """statement to add line to the FileWriter array"""
        s = statement.split(",")
        writeStat = [self.row, time.time()]+s
        self.writeList.append(writeStat)

    def writeFile(self):
        """turn the object into an array"""
        df = pd.DataFrame(self.writeList)
        df.to_csv(absolutepath(self.path))
