import os
import torch
import whisper
from moviepy.video.io.VideoFileClip import VideoFileClip

from src.utilities.pathConfig import PathConfig
from src.entities.pathConverter import PathConverter
class ConverterService():

    folderName:str
    pathVideo:str
    pathAudio:str
    pathMD:str

    def __init__(self,_folderName):
        self.folderName=_folderName
        self.pathVideo = PathConfig.pathVideo + _folderName
        self.pathAudio = PathConfig.pathAudio + _folderName
        self.pathMD = PathConfig.pathMD + _folderName

    def addVideoAudio(self):
        pVideoAudio=PathConverter(self.pathVideo, self.pathAudio, "mp3")
        pVideoAudio.genListFiles()
        pVideoAudio.pathToFile()
        return pVideoAudio

    def addAudioMD(self):
       pAudioMD=PathConverter(self.pathAudio, self.pathMD, "txt")
       pAudioMD.genListFiles()
       pAudioMD.pathToFile()
       return pAudioMD


    def videoToAudio(self):
        pVideoAudio=self.addVideoAudio()
        for i in range(len(pVideoAudio.listPathFluxEnter)):
            print(f"[{i + 1}]/[{len(pVideoAudio.listPathFluxEnter) + 1}]")
            print(f"Converting {pVideoAudio.listFileFlux[i]}")
            video : VideoFileClip = VideoFileClip(pVideoAudio.listPathFluxEnter[i])
            if not os.path.exists(os.path.dirname(pVideoAudio.listPathFluxExit[i])):
                os.makedirs(os.path.dirname(pVideoAudio.listPathFluxExit[i]))
            video.audio.write_audiofile(pVideoAudio.listPathFluxExit[i])

    def audioToTxt(self):
        pAudioMD = self.addAudioMD()
        device = "cuda" if torch.cuda.is_available() else "cpu"
        whisper_model  = whisper.load_model("medium", device=device)
        for i in range(len(pAudioMD.listPathFluxEnter)):
            print(f"[{i+1}]/[{len(pAudioMD.listPathFluxEnter)+1}]")
            print(f"Converting {pAudioMD.listFileFlux[i]}")
            pmp3= pAudioMD.listPathFluxEnter[i]
            pmd = pAudioMD.listPathFluxExit[i]
            if not os.path.exists(os.path.dirname(pAudioMD.listPathFluxExit[i])):
                os.makedirs(os.path.dirname(pAudioMD.listPathFluxExit[i]))
            result  = whisper_model.transcribe(pmp3,verbose=True)
            with open(pmd, "w+") as f:
                f.write(result["text"])