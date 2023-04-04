from flask import Flask
from flask_sock import Sock
from amqp_helper import Rabbitmq
from time import sleep


import json

app = Flask(__name__)
sock = Sock(app)

class MessageCentre:
    def __init__(self) -> None:
        self.messages = {
            'user':{},
            'family':{}
        }
        pass
    def _add(self,msg,type,id):
        if type == 'user' or type == 'family':
            # If user message doesnt exist, add in a new list, else add to list
            self.messages[type][id] = self.messages[type].get(id,[])+[msg]
    def getUserAlert(self,userID):
        return self.messages['user'].get(userID,[])
    def getFamilyAlert(self,familyID):
        return self.messages['family'].get(familyID,[])

def callback(ch, method, properties, body):
    data = json.loads(body)

    print(data)

    type = data.get('type',None)
    id = data.get('id',None)
    msg = data.get('msg',None)
    messageCentre._add(msg=msg,type=type,id=id)


@sock.route('/ws')
def ws(ws):
    while True:
        txt = ws.receive()
        print(txt)
        try:
            data = json.loads(txt)
            message_type = data.get('message',"Error")
            if message_type == "getUserAlert":
                id = data.get('userID')
                if id is not None and messageCentre:
                    msg = messageCentre.getUserAlert(id)
                    ws.send(json.dumps({'code': 200, 'data': msg}))
            elif message_type == "getFamilyAlert":
                id = data.get('familyID')
                if id is not None and messageCentre:
                    msg = messageCentre.getUserAlert(id)
                    ws.send(json.dumps({'code': 200, 'data': msg}))

        except Exception as e:
            print(e)


if __name__ == '__main__':
    global messageCentre
    messageCentre = MessageCentre()
    rabbitmq = Rabbitmq()
    print("subscribing to user_1 and family_1")
    rabbitmq.subscribe('user_1')
    rabbitmq.subscribe('family_1')
    # rabbitmq.subscribe('family_1')
    app.run(debug=True)
    rabbitmq.unsubscribe()
    

