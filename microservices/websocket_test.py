from websocket import *

def on_message(ws, message):
    print(message)

def on_error(ws, error):
    print(error)

def on_close(ws, namespace, sid):
    print("### closed ###")

def on_open(ws):
    print("### connected ###")
    ws.send("Hello, server!")

if __name__ == "__main__":
    enableTrace(True)
    ws = WebSocketApp("ws://localhost:5000/ws",
                                on_message = on_message,
                                on_error = on_error,
                                on_close = on_close)
    ws.on_open = on_open
    ws.run_forever()
