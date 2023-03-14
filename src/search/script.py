import os
import torch
import whisper
from moviepy.editor import *

# Convert MP4 to MP3

# pathMP4 = chemin_fichier = os.path.join(os.path.dirname(__file__), "sample.mp4")
# pathMP3 = os.path.join(os.path.dirname(__file__), "sample.mp3")
#
# video = VideoFileClip(pathMP4)
# video.audio.write_audiofile(pathMP3)

#Load Model Whisper

device = "cuda" if torch.cuda.is_available() else "cpu"
# Load the model
whisper_model = whisper.load_model("small", device=device)

pathMP3 = "C:/holding/game/code/niceconverter/src/search/sample.mp3"


#Convert MP3 to TXT
print(pathMP3)
result_ADO = whisper_model.transcribe(pathMP3,verbose=True)
print(result_ADO)