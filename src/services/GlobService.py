from src.entities.mapping import Mapping
from src.config.pathConfig import PathConfig


# Variable qui sera a prompt par l'utilisateur dans le main
folderName="MAD\\"

# On charge les path de notre application
pathVideo=PathConfig.pathVideo+folderName
pathAudio=PathConfig.pathAudio+folderName
pathMD=PathConfig.pathMD+folderName


# On scan les fichiers puis on y rajoute les paths
globMapping=Mapping()
globMapping.addVideoAudio(pathVideo,pathAudio)
globMapping.pVideoAudio.pathToFile()

# On convertit les videos en audios, si ce n'est pas deja fait
globMapping.videoToAudio()

# On Transcrit les audios en texte sous forme de MD
globMapping.addAudioMD(pathAudio,pathMD)
globMapping.pAudioMD.pathToFile()

globMapping.audioToTxt()



# On synthetise les texte toujours en MD
