from flask import Flask, send_file
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/")
def teste():
    return "<h1>Hello World</h1>"

@app.route("/image")
def image():
    return send_file('image.jpg', mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

