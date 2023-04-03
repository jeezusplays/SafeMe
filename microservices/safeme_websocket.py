from flask import Flask
from flask_sock import Sock
from amqp_helper import Rabbitmq

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
    rabbitmq = Rabbitmq()
    rabbitmq.subscribe('user_1')
    # app.run(debug=True)

