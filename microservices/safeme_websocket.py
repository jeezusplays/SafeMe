from flask import Flask
from flask_sock import Sock
from amqp_helper import Rabbitmq
import json

app = Flask(__name__)
sock = Sock(app)

@sock.route('/ws')
def ws(ws):
    while True:
        txt = ws.receive()
        try:
            data = json.loads(txt)
            print(data)
            ws.send('Hello there')
        except Exception as e:
            print(e)
        
    # print(ws)
    # print('WebSocket client connected')
    # return 'WebSocket connection established'

if __name__ == '__main__':
    rabbitmq = Rabbitmq()
    rabbitmq.subscribe('user_1')
    # app.run(debug=True)

