import os

class Path():
    pathEnter: str = ""
    pathExit: str = ""
    extensionOutput:str=""
    listPathEnter: list[str] = []
    listPathExit: list[str] = []
    listPathFluxEnter: list[str] = []
    listPathFluxExit:list[str] = []
    listFileEnter: list[str] = []
    listFileExit: list[str] = []
    listFileFlux: list[str] = []

    def __init__(self, _pathEnter: str, _pathExit: str,_outsideExtension:str):
        self.pathEnter = _pathEnter
        self.pathExit = _pathExit
        self.extensionOutput = _outsideExtension

    @staticmethod
    def scan_files(path: str) -> list[str]:
        listFile: list[str] = []
        for root, dirs, files in os.walk(path):
            for file in files:
                file_path = os.path.join(root, file)
                listFile.append(file_path[len(path):])
        return listFile

    def genListFiles(self):
        # Scanning files in Video, and in Audio
        self.listFileEnter = self.scan_files(self.pathEnter)
        self.listFileExit = self.scan_files(self.pathExit)

        # Create a dictionary to store filenames and their extensions
        file_extensions = {}

        # Loop over all files in the input directory
        for file_path in self.listFileEnter:
            # Split the filename and extension using os.path.splitext
            filename, extension = os.path.splitext(file_path)

            # If the filename is not already in the dictionary, create a new entry
            if filename not in file_extensions:
                file_extensions[filename] = set()

            # Add the extension to the set of extensions for this filename
            file_extensions[filename].add(extension)

        # Create a set of unique filenames from the input directory
        set_enter_files = set(file_extensions.keys())

        # Loop over all files in the output directory
        set_exit_files = set([os.path.splitext(file_path)[0] for file_path in self.listFileExit])

        # Find the set difference to get the files that are in the input directory but not the output directory
        set_file_flux = set_enter_files - set_exit_files

        # Reconstruct the list of files to output, including their original extensions
        self.listFileFlux = []
        for filename in set_file_flux:
            extensions = file_extensions[filename]
            for extension in extensions:
                self.listFileFlux.append(filename + extension)

    def pathToFile(self):
        self.listPathEnter = [self.pathEnter + self.listFileEnter[i] for i in range(len(self.listFileEnter))]
        self.listPathExit = [self.pathExit + self.listFileExit[i] for i in range(len(self.listFileExit))]
        self.listPathFluxEnter = [self.pathEnter + self.listFileFlux[i] for i in range(len(self.listFileFlux))]
        self.listPathFluxExit = [self.pathExit + self.listFileFlux[i][:-3] + self.extensionOutput for i in range(len(self.listFileFlux))]

