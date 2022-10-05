filepath = "/home/estudiante/Documentos/TEC/SETI/speech/SpeechToText/src/Resourses/Audios/"     #Input audio file path
output_filepath = "/home/estudiante/Documentos/TEC/SETI/speech/SpeechToText/src/Resourses/Transcription/" #Final transcript path
bucket_name = "audios_mp3" #Name of the bucket created in the step before
blobs_names=[]
# Import libraries
import os, math
from google.cloud import speech
from google.cloud import storage
from pydub import AudioSegment
from google.cloud import speech_v1p1beta1 as speech


def single_split(audio, from_min, to_min, split_filename):
    t1 = from_min * 60 * 1000
    t2 = to_min * 60 * 1000
    split_audio = audio[t1:t2]
    split_audio.export(filepath + split_filename + '.flac', format="flac")

def multiple_split(audio, min_per_split,output_audio_name):
    total_mins = math.ceil(audio.duration_seconds/ 60)
    for i in range(0, total_mins, min_per_split):
        split_fn = output_audio_name + '_' + str(i)
        blobs_names.append(split_fn)
        #print(blobs_names)
        single_split(audio,i, i + min_per_split, split_fn)
        print(str(i) + ' Done')
        if i >= total_mins - min_per_split:
            print('All splited successfully')

def mp3_to_flac(audio_name, output_audio_name):

    audio_mp3 = AudioSegment.from_file(filepath + audio_name, format="m4a")
    audio_mp3 = audio_mp3.set_frame_rate(16000)
    audio_mp3 = audio_mp3.set_channels(1)
    audio_mp3 = audio_mp3.set_sample_width(2)
    multiple_split(audio_mp3, math.ceil((audio_mp3.duration_seconds)/1920),output_audio_name) #divide audio in 32 parts


def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(source_file_name)


def delete_blob(bucket_name, blob_name):
    """Deletes a blob from the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)

    blob = bucket.blob(blob_name)

    blob.delete()


def google_transcribe(audio_file_name):
    extension_flac = ".flac"

    mp3_to_flac(audio_file_name + ".m4a", audio_file_name)

    for i in blobs_names:
        source_file_name = filepath + i + extension_flac
        destination_blob_name = i + extension_flac
        upload_blob(bucket_name, source_file_name, destination_blob_name)
    print('All uploaded successfully...')

    #compose_file(bucket_name, audio_file_name + extension_flac)
    transcript_filename = audio_file_name + '.txt'
    print("Waiting for operation to complete...")
    for blobs in blobs_names:
        transcript= transcrip(blobs,extension_flac)
        write_transcripts(transcript_filename, transcript)

def transcrip(audio_file_name,extension_flac):


    gcs_uri = 'gs://' + bucket_name + '/' + audio_file_name + extension_flac
    transcript = ''

    client = speech.SpeechClient()
    audio = speech.RecognitionAudio(uri=gcs_uri)

    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.FLAC,
        sample_rate_hertz=16000,
        language_code="es-CR",

    )

    # Detects speech in the audio file
    operation = client.long_running_recognize(config=config, audio=audio)

    response = operation.result(timeout=10000)

    # Each result is for a consecutive portion of the audio. Iterate through
    # them to get the transcripts for the entire audio file.
    for result in response.results:
        # The first alternative is the most likely one for this portion.
        transcript += "speaker: {}".format(result.alternatives[0].transcript) + '\n'  # Changed


    return transcript


def write_transcripts(transcript_filename, transcript):
    f = open(output_filepath + transcript_filename, "a")
    f.write(transcript+'\n')
    f.close()


def main(name, direccion):
    print(name)
    print(direccion)

    '''
    file_name = 'audioss'
    google_transcribe(file_name)
    for audio in blobs_names:
        delete_blob(bucket_name, audio + '.flac')
        os.remove(filepath + audio + '.flac')'''

