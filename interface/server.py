from flask import Flask, send_from_directory
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# serve the index.html file located in the 'static' folder
@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

# serve any other file located in the 'static' folder
@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory('static', path)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=6969)