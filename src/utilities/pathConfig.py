from src.utilities.shareFunctions import ShareFunctions
class PathConfig():
    pathMain = ShareFunctions.parentPathIndex(2)
    res="res\\"
    pathRes = pathMain + res
    audio="audio\\"
    video="video\\"
    md="md\\"
    synthesis="synthesis\\"
    pathAudio = pathRes + audio
    pathVideo = pathRes + video
    pathMD = pathRes + md
    pathSynthesis = pathRes + synthesis
    def __init__(self):
        pass

