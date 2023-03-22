from src.services.converterService import ConverterService

# Variable qui sera a prompt par l'utilisateur dans le main
folderName="LINDBERG\\"


# On scan les fichiers puis on y rajoute les paths
converterService=ConverterService(folderName)
# On convertit les videos en audios, si ce n'est pas deja fait
converterService.videoToAudio()
# On Transcrit les audios en texte sous forme de MD
converterService.audioToTxt()

