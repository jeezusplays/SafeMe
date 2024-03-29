from flask import Flask
from flask_sock import Sock
from amqp_helper import Rabbitmq
from time import sleep
from os import environ
import json
import servicehelper

app = Flask(__name__)
sock = Sock(app)
SAFEME_WEBSOCKET_HOST_PORT = environ.get("SAFEME_WEBSOCKET_HOST_PORT")



class MessageCentre:
    def __init__(self) -> None:
        self.messages = {
            'user':{},
            'family':{}
        }
    def _add(self,msg,type,id):
        if type == 'user' or type == 'family':
            self.messages[type][id] = self.messages[type].get(id,[])+[msg]
            print(self.messages)

    def getUserAlert(self,userID):
        print(f"sending user alert now {userID}")
        return self.messages['user'].get(userID,[])
    
    def getFamilyAlert(self,familyID):
        print(f"sending family alert now {familyID}")
        return self.messages['family'].get(familyID,[])

def callback_alert(ch, method, properties, body):
    routing_key = method.routing_key
    data = json.loads(body)
    split = routing_key.split('.')
    id = split[1]
    type = split[0]

    print(id)
    print(type)

    message_centre._add(msg=data,type=type,id=id)
        
@sock.route('/ws')
def ws(ws):
    while True:
        txt = ws.receive()
        print(txt)
        try:
            with app.app_context():
                data = json.loads(txt)
                message_type = data.get('message', "Error")

                if message_type == "getUserAlert":
                    id = data.get('userID')
                    if id is not None and message_centre:
                        print(message_centre.messages)
                        msg = message_centre.getUserAlert(str(id))
                        ws.send(json.dumps({'code': 200, 'data': msg}))

                elif message_type == "getFamilyAlert":
                    id = data.get('familyID')
                    if id is not None and message_centre:
                        msg = message_centre.getFamilyAlert(str(id))
                        ws.send(json.dumps({'code': 200, 'data': msg}))

        except Exception as e:
            print(e)

if __name__ == "__main__":

    print("Websocket microservice has started")
    while not servicehelper.isServiceReady("createdisaster"):
        sleep(1)
    rabbitmq = Rabbitmq()
    rabbitmq._setup()
    message_centre = MessageCentre()

    print("subscribing to user_1 and family_1")

    rabbitmq.subscribe('user_1', callback_alert)
    rabbitmq.subscribe('family_1', callback_alert)
    try:
        servicehelper.serviceIsReady("websocket")
        app.run(host='0.0.0.0', port=SAFEME_WEBSOCKET_HOST_PORT)
    except:
        pass
    finally:
        rabbitmq.unsubscribe()
