filepath = "/home/maria/Escritorio/2021/Seti/SpeechToText/src/Resourses/Audios/"     #Input audio file path
output_filepath = "/home/maria/Escritorio/2021/Seti/SpeechToText/src/Resourses/Transcription/" #Final transcript path
bucket_name = "audio_mp3" #Name of the bucket created in the step before

# Import libraries
import os
from google.cloud import speech
from google.cloud import storage
from pydub import AudioSegment


def mp3_to_flac(audio_name, output_audio_name):
    audio_mp3 = AudioSegment.from_file(filepath + audio_name, format="mp3")
    audio_mp3 = audio_mp3.set_frame_rate(16000)
    audio_mp3 = audio_mp3.set_channels(1)
    audio_mp3 = audio_mp3.set_sample_width(2)
    audio_mp3.export(filepath + output_audio_name, format="flac")


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
    mp3_to_flac(audio_file_name + ".mp3", audio_file_name + extension_flac)

    source_file_name = filepath + audio_file_name + extension_flac
    destination_blob_name = audio_file_name + extension_flac

    upload_blob(bucket_name, source_file_name, destination_blob_name)

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
    print("Waiting for operation to complete...")
    response = operation.result(timeout=10000)

    # Each result is for a consecutive portion of the audio. Iterate through
    # them to get the transcripts for the entire audio file.
    for result in response.results:
        # The first alternative is the most likely one for this portion.
        #print("Transcript: {}".format(result.alternatives[0].transcript))
        #print("Confidence: {}".format(result.alternatives[0].confidence))
        transcript += "Transcript: {}".format(result.alternatives[0].transcript) + '\n'  # Changed

    #delete_blob(bucket_name, destination_blob_name)
    return transcript


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
            transcript = google_transcribe("audio_1")
            transcript_filename = "ClaseMunguia".split('.')[0] + '.txt'
            write_transcripts(transcript_filename, transcript)

main()


