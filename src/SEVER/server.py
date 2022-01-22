from flask import Flask,jsonify,request,json
from flask.wrappers import Response
import base64
import os
#from speech_to_text_cloud_v import main

app = Flask(__name__)


@app.route("/members", methods=["POST"])
def members():
    if request.method == 'POST':
        data = json.loads(request.data)
        audio_file = base64.b64decode(data['file'])
        with open(os.path.join(r'C:\Users\dcapr\OneDrive\Documents\SpeechToText\src\Resourses\test', 'aaaa.m4a'), 'wb') as file_to_write:
            file_to_write.write(audio_file)
            file_to_write.close()
        #print(data)
        '''
        #main(data['nombre'],data['direccion'])
        print("----------------------------------------------------")
        print("El nombre del archivo es: ", data['nombre'])
        print("----------------------------------------------------")'''
        data = {"members": ["Maria","dac","Alberto"]}
        return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)