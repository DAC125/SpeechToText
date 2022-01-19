from flask import Flask,jsonify,request,json
from flask.wrappers import Response
#from speech_to_text_cloud_v import main

app = Flask(__name__)


@app.route("/members", methods=["POST"])
def members():
    if request.method == 'POST':
        data = json.loads(request.data)
        #main(data['nombre'],data['direccion'])
        print("----------------------------------------------------")
        print("El nombre del archivo es: ", data['nombre'])
        print("----------------------------------------------------")
        data = {"members": ["Maria","dac","Alberto"]}
        return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)