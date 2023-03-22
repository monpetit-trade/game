from src.utilities.shareFunctions import ShareFunctions

class PathRead():
    pathEnter: str = ""
    listPathEnter: list[str] = []
    listFileEnter: list[str] = []

    def __init__(self, _pathEnter: str):
        self.pathEnter = _pathEnter
        self.listFileEnter=ShareFunctions.scan_files(_pathEnter)
        self.listPathEnter=[_pathEnter+self.listFileEnter[i] for i in range (len(self.listFileEnter))]


