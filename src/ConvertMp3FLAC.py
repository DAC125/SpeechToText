
from pydub import AudioSegment
audio_mp3 = AudioSegment.from_file('/home/maria/Escritorio/2021/Seti/SpeechToText/src/Resourses/Audios/undefined.mp3',format="mp3")
audio_mp3 = audio_mp3.set_frame_rate(16000)
audio_mp3 = audio_mp3.set_channels(1)
audio_mp3 = audio_mp3.set_sample_width(2)
audio_mp3.export('/home/maria/Escritorio/2021/Seti/SpeechToText/src/Resourses/Audios/undefined2.flac',format="flac")




"""
from subprocess import call

import soundfile

call(["ffmpeg","-i","/home/maria/Escritorio/2021/Seti/SpeechToText/src/Resourses/Audios/undefined.mp3","-acodec", "pcm_s16le", "-ac" ,"1", "-ar", "16000","/home/maria/Escritorio/2021/Seti/SpeechToText/src/Resourses/Audios/undefined2.flac"])
"""
