from flask import Flask,jsonify,request,json
from flask.wrappers import Response
import base64
import os
import time
#from speech_to_text_cloud_v import main

app = Flask(__name__)


@app.route("/members", methods=["POST"])
def members():
    if request.method == 'POST':
        print("waiting...")
        '''
        print(request)
        req = json.loads(request.data)
        #print(req)
        
        audio_file = base64.b64decode(req['fileBase64'])
        with open(os.path.join('/home/dac125/Documents/SpeechToText/src/Resourses/test', req['name']), 'wb') as file_to_write:
            file_to_write.write(audio_file)
            file_to_write.close()
        #print(req)
        
        #main(req['nombre'],req['direccion'])
        print("----------------------------------------------------")
        print("El nombre del archivo es: ", req['nombre'])
        print("----------------------------------------------------")
        '''
        time.sleep(10)
        res = {"members": ["Maria","dac","Alberto"]}
        return jsonify(res)


if __name__ == "__main__":
    app.run(debug=True)