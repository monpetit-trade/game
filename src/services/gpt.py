import os
from typing import List


class MyScanner:
    @staticmethod
    def scan_files(path: str) -> List[str]:
        listFile: List[str] = []
        for root, dirs, files in os.walk(path):
            for file in files:
                file_path = os.path.join(root, file)
                listFile.append(file_path)
        return listFile

        # Ajout du chemin parent dans la liste des répertoires
        dirs = [path] + dirs

        for dir in dirs:
            for file in os.listdir(dir):
                file_path = os.path.join(dir, file)
                if os.path.isfile(file_path):
                    listFile.append(file_path)

        return listFile



if __name__ == "__main__":
    path = r"C:\HOLDING\GAME\CODE\NICECONVERTER\RES\VIDEO"
    files = MyScanner.scan_files(path)
    print(files)