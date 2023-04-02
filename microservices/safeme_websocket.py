from flask import Flask
from flask_sock import Sock

app = Flask(__name__)
sock = Sock(app)

@sock.route('/ws')
def ws(ws):
    while True:
        txt = ws.receive()
        ws.send(txt[::-1])
    # print(ws)
    # print('WebSocket client connected')
    # return 'WebSocket connection established'

if __name__ == '__main__':
    app.run(debug=True)

