from websocket import *
from time import sleep
import json

if __name__ == "__main__":
    enableTrace(True)
    ws = WebSocket()
    ws.connect("ws://localhost:9000/ws")
    test1 ={
        "message":"getUserAlert",
        "userID":1
    }
    test2 ={
        "message":"getFamilyAlert",
        "familyID":1
    }
    count = 10
    while count>0:
        print("=== sending test 1 - user alert ===")
        ws.send(json.dumps(test1))
        print(ws.recv())
        print("=== sending test 2 - family alert ===")
        ws.send(json.dumps(test2))
        print(ws.recv())
        sleep(2)
        count -= 1
    ws.close()
