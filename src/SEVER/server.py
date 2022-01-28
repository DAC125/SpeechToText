import time
from flask import Flask,jsonify,request,json
from flask.wrappers import Response
import base64
import os
#from speech_to_text_cloud_v import main

app = Flask(__name__)


@app.route("/transcriptFile", methods=["POST"])
def members():
    if request.method == 'POST':
        print(request)
        req = json.loads(request.data)
        
        audio_file = base64.b64decode(req['fileBase64'])
        with open(os.path.join('/home/dac125/Documents/SpeechToText/src/SEVER/Resources', req['name']), 'wb') as file_to_write:
            file_to_write.write(audio_file)
            file_to_write.close()
        
        with open("/home/dac125/Documents/SpeechToText/src/Resourses/Transcription/messi.txt", "rb") as file:
            encoded_string = base64.b64encode(file.read())
        res = {"file": encoded_string.decode('UTF-8')}
        time.sleep(5)
        return jsonify(res)


if __name__ == "__main__":
    app.run(debug=True)