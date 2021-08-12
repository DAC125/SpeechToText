filepath = "/home/estudiante/Documentos/TEC/SETI/speech/SpeechToText/src/Resourses/Audios" #Input audio file path
output_filepath = "/home/estudiante/Documentos/TEC/SETI/SpeechToText/src/Resourses/Transcriptions" #Final transcript path
bucketname = "audio_mp3" #Name of the bucket created in the step before
# Import libraries
from pydub import AudioSegment
import io
import os
from google.cloud import speech
import wave
from google.cloud import storage

import librosa
import soundfile as sf

def mp3_to_wav(audio_file_name):
    if audio_file_name.split('.')[1] == 'mp3':
        sound = AudioSegment.from_mp3(audio_file_name)
        audio_file_name = audio_file_name.split('.')[0] + '.wav'
        sound.export(audio_file_name, format="wav")


def frame_rate_channel(audio_file_name):
    x, _ = librosa.load(audio_file_name, sr=16000)
    sf.write('tmp.wav', x, 16000)
    with wave.open('tmp.wav', "r") as wave_file:
        frame_rate = wave_file.getframerate()
        channels = wave_file.getnchannels()
        return frame_rate, channels


def stereo_to_mono(audio_file_name):
    sound = AudioSegment.from_wav(audio_file_name)
    sound = sound.set_channels(1)
    sound.export(audio_file_name, format="wav")




def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)




def delete_blob(bucket_name, blob_name):
    """Deletes a blob from the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(blob_name)

    blob.delete()



def google_transcribe(audio_file_name):

    file_name = filepath + audio_file_name

    mp3_to_wav(file_name)
    # The name of the audio file to transcribe

    frame_rate, channels = frame_rate_channel(file_name)

    if channels > 1:
        stereo_to_mono(file_name)

    bucket_name = 'audio_mp3'
    source_file_name = filepath + audio_file_name
    destination_blob_name = audio_file_name

    upload_blob(bucket_name, source_file_name, destination_blob_name)

    gcs_uri = 'gs://audio_mp3/' + audio_file_name
    transcript = ''

    client = speech.SpeechClient()
    audio = speech.RecognitionAudio(uri=gcs_uri)

    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.FLAC,
        sample_rate_hertz=16000,
        language_code="en-US",
    )

    # Detects speech in the audio file

    operation = client.long_running_recognize(config=config, audio=audio)
    print("Waiting for operation to complete...")
    response = operation.result(timeout=90)

    # Each result is for a consecutive portion of the audio. Iterate through
    # them to get the transcripts for the entire audio file.
    for result in response.results:
        # The first alternative is the most likely one for this portion.
        print(u"Transcript: {}".format(result.alternatives[0].transcript))
        print("Confidence: {}".format(result.alternatives[0].confidence))


def write_transcripts(transcript_filename, transcript):
    f = open(output_filepath + transcript_filename, "w+")
    f.write(transcript)
    f.close()



def main():

    for audio_file_name in os.listdir(filepath):
        exists = os.path.isfile(output_filepath + audio_file_name.split('.')[0] + '.txt')
        if exists:
            pass
        else:
            google_transcribe("undefined.mp3")
            #transcript_filename = "undefined.mp3".split('.')[0] + '.txt'
            #write_transcripts(transcript_filename, transcript)


main()