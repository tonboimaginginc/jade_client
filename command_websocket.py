import websocket
import threading
from time import sleep
import json


class CommandWebSocket:
    def on_message(self, message):
        print('[*] Message received')
        print(message)

    def on_error(self, error):
        print(error)

    def on_close(self):
        self.ws.close()
        self.connected = False
        print('[*] Connection closed')

    def on_open(self):
        self.connected = True
        print('[*] Connection opened')

    # Example data(request command) to send: { "commandId": 1001, "value": "" }
    def send(self, data):
        if not self.connected:
            print('[*] Not connected. Trying again')
            self.start()

        try:
            self.ws.send(data)
        except websocket._exceptions.WebSocketConnectionClosedException as ex:
            print('[*] Not connected')

    def start(self):
        self.ws = websocket.WebSocketApp(self.server,
                                         on_message=self.on_message,
                                         on_error=self.on_error,
                                         on_close=self.on_close)
        self.ws.on_open = self.on_open

        self.wst = threading.Thread(target=self.ws.run_forever)
        self.wst.daemon = True
        self.wst.start()

    def __init__(self, server="ws://127.0.0.1:4040"):
        self.server = server
        self.connected = False
        self.start()

    def __del__(self):
        self.ws.close()

if __name__ == '__main__':
    commandsocket = CommandWebSocket('ws://192.168.42.1:4040')
    sleep(2)
    commandsocket.send('{ "commandId": 1001, "value": "" }')
    sleep(2)
