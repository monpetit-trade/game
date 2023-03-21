import os
import torch
import whisper


from moviepy.video.io.VideoFileClip import VideoFileClip

from src.entities.path import Path

class Mapping():
    pVideoAudio:None|Path = None
    pAudioMD:None|Path = None
    pMDSynthesis:None|Path=None

    def __init__(self):
        pass
    def addVideoAudio(self,_pathVideo:str,_pathAudio:str):
        self.pVideoAudio=Path(_pathVideo,_pathAudio,"mp3")
        self.pVideoAudio.genListFiles()
        self.pVideoAudio.pathToFile()

    def addAudioMD(self,_pathAudioEnter:str,_pathAudioExit):
        self.pAudioMD=Path(_pathAudioEnter,_pathAudioExit,"txt")
        self.pAudioMD.genListFiles()
        self.pAudioMD.pathToFile()

    def addMDSynthesis(self,_pathMDEnter:str,_pathMDExit:str):
        self.pMDSynthesis=Path(_pathMDEnter,_pathMDExit)
        self.pMDSynthesis.genListFiles()
        self.pMDSynthesis.pathToFile()

    def videoToAudio(self):
        for i in range(len(self.pVideoAudio.listPathFluxEnter)):
            print(f"[{i + 1}]/[{len(self.pVideoAudio.listPathFluxEnter) + 1}]")
            print(f"Converting {self.pVideoAudio.listFileFlux[i]}")
            video : VideoFileClip = VideoFileClip(self.pVideoAudio.listPathFluxEnter[i])
            if not os.path.exists(os.path.dirname(self.pVideoAudio.listPathFluxExit[i])):
                os.makedirs(os.path.dirname(self.pVideoAudio.listPathFluxExit[i]))
            video.audio.write_audiofile(self.pVideoAudio.listPathFluxExit[i])

    def audioToTxt(self):
        device = "cuda" if torch.cuda.is_available() else "cpu"
        whisper_model  = whisper.load_model("medium", device=device)
        for i in range(len(self.pAudioMD.listPathFluxEnter)):
            print(f"[{i+1}]/[{len(self.pAudioMD.listPathFluxEnter)+1}]")
            print(f"Converting {self.pAudioMD.listFileFlux[i]}")
            pmp3= self.pAudioMD.listPathFluxEnter[i]
            pmd = self.pAudioMD.listPathFluxExit[i]
            if not os.path.exists(os.path.dirname(self.pAudioMD.listPathFluxExit[i])):
                os.makedirs(os.path.dirname(self.pAudioMD.listPathFluxExit[i]))
            result  = whisper_model.transcribe(pmp3,verbose=True)
            with open(pmd, "w+") as f:
                f.write(result["text"])