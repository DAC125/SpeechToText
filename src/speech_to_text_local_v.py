filepath = "/home/estudiante/Documentos/TEC/SETI/speech/SpeechToText/src/Resourses/Audios/"     #Input audio file path
output_filepath = "/home/estudiante/Documentos/TEC/SETI/speech/SpeechToText/src/Resourses/Transcription/" #Final transcript path
bucket_name = "audios_mp3" #Name of the bucket created in the step before
blobs_names=[]
# Import libraries
import os, math
from google.cloud import speech
from pydub import AudioSegment
from google.cloud import speech_v1p1beta1 as speech


def single_split(audio, from_min, to_min, split_filename):
    t1 = from_min * 60 * 1000
    t2 = to_min * 60 * 1000
    split_audio = audio[t1:t2]
    split_audio.export(filepath + split_filename + '.flac', format="flac")

def multiple_split(audio, min_per_split,output_audio_name):
    print(min_per_split)
    total_mins = math.ceil(audio.duration_seconds/ 60)
    for i in range(0, total_mins, min_per_split):
        split_fn = str(i) + '_' + output_audio_name
        blobs_names.append(split_fn)
        #print(blobs_names)
        single_split(audio,i, i + min_per_split, split_fn)
        print(str(i) + ' Done')
        if i == total_mins - min_per_split:
            print('All splited successfully')

def mp3_to_flac(audio_name, output_audio_name):
    audio_mp3 = AudioSegment.from_file(filepath + audio_name, format="mp3")
    audio_mp3 = audio_mp3.set_frame_rate(16000)
    audio_mp3 = audio_mp3.set_channels(1)
    audio_mp3 = audio_mp3.set_sample_width(2)
    multiple_split(audio_mp3, math.ceil(audio_mp3.duration_seconds/1920),output_audio_name) #divide audio in 32 parts








def google_transcribe(audio_file_name):
    extension_flac = ".flac"

    mp3_to_flac(audio_file_name + ".mp3", audio_file_name)




    transcript_filename = audio_file_name + '.txt'
    print("Waiting for operation to complete...")
    for blobs in blobs_names:
        transcript= transcrip(blobs,extension_flac)
        write_transcripts(transcript_filename, transcript)


def transcrip(audio_file_name,extension_flac):
    client = speech.SpeechClient()

    speech_file = filepath + audio_file_name + extension_flac

    with open(speech_file, "rb") as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)

    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.FLAC,
        sample_rate_hertz=16000,
        language_code="es-CR",
        enable_speaker_diarization=True,
    )


    response = client.recognize(config=config, audio=audio)

    # The transcript within each result is separate and sequential per result.
    # However, the words list within an alternative includes all the words
    # from all the results thus far. Thus, to get all the words with speaker
    # tags, you only have to take the words list from the last result:

    result = response.results[-1]

    words_info = result.alternatives[0].words

    text = ''
    # Printing out the output:
    speaker = ''
    for word_info in words_info:
        text += word_info.word + ' '
        speaker = word_info.speaker_tag
    return "speaker {}: {}".format(speaker,text)

def write_transcripts(transcript_filename, transcript):
    f = open(output_filepath + transcript_filename, "a")
    f.write(transcript+'\n')
    f.close()





def main():
    file_name = 'messi'
    google_transcribe(file_name)
    for audio in blobs_names:
        os.remove(filepath + audio + '.flac')



main()


