from websocket import *
from time import sleep
import json

if __name__ == "__main__":
    enableTrace(True)
    ws = WebSocket()
    ws.connect("ws://localhost:5000/ws")
    test1 ={
        "message":"getUserAlert",
        "userID":1
    }
    count = 10
    while count>0:
        ws.send(json.dumps(test1))
        sleep(2)
        count -= 1
    ws.close()
