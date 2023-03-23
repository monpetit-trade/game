import os

class ShareFunctions():

    @staticmethod
    def scan_files(path: str) -> list[str]:
        listFile: list[str] = []
        for root, dirs, files in os.walk(path):
            for file in files:
                file_path = os.path.join(root, file)
                listFile.append(file_path[len(path):])
        return listFile

    @staticmethod
    def parentPathIndex(parentIndex):
        currentPath = os.getcwd()
        for i in range(parentIndex):
            currentPath = os.path.dirname(currentPath)
        return currentPath+"\\"

    @staticmethod
    def readFile(path):
        with open(path,"r") as f:
            lignes=[]
            for ligne in f:
                lignes.append(ligne)
        return lignes

