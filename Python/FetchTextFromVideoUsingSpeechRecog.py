from moviepy.editor import *
import pysrt
import speech_recognition as sr
video = VideoFileClip(r"Avengers.mp4")
video.subclip().audio.write_audiofile(filename = r"Avengers.wav") 
r = sr.Recognizer()

audio_wav=sr.AudioFile(r"Avengers.wav")
with audio_wav as source:
    audio = r.record(source)
    s = r.recognize_google(audio)

    with open("Avengers.srt", "w") as text_file:
        text_file.write(s)
    print("Srt file generated")
#print(extensions_dict)