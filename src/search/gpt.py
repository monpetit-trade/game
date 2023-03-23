from src.utilities.pathConfig import PathConfig
from src.utilities.shareFunctions import ShareFunctions

pkey=PathConfig.pathMain+"keys\\gpt.key"
key=ShareFunctions.readFile(pkey)[0]

