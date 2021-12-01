from pathlib import Path
def absolutepath(filepath):
    relative = Path(filepath)
    return relative.absolute()

class FileWriter:
    def __init__(self, fname, apath):
        self.path = apath
        self.filename = fname
    def write_next_line(self):
