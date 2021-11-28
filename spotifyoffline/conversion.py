from moviepy.editor import VideoFileClip

from os import getcwd, remove
from os.path import join

def convertMP3ToMP4(filename: str):
    source = join(getcwd(), "music", filename)
    target = join(getcwd(), "music", filename.replace(".mp4", ".mp3"))
    video = VideoFileClip(source)
    video.audio.write_audiofile(target, logger = None)
    remove(source)