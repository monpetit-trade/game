import os
from moviepy.editor import *
video = VideoFileClip(os.path.join("path","to","movie.mp4"))
video.audio.write_audiofile(os.path.join("path","to","movie_sound.mp3"))