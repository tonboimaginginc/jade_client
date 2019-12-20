import websocket
import threading
from time import sleep

class DataWebSocket:
    def on_message(self, message):
        print('[*] Message received')
        print(message)
        # TODO: use the JSON object

    def on_error(self, error):
        print(error)

    def on_close(self):
        self.ws.close()
        self.connected = False
        print('[*] data socket connection closed')

    def on_open(self):
        self.connected = True
        print('[*] Connection opened')

    def send(self, data):
        print('[*] Dont send anything')

    def start(self):
        self.ws = websocket.WebSocketApp(self.server,
                                         on_message=self.on_message,
                                         on_error=self.on_error,
                                         on_close=self.on_close)
        self.ws.on_open = self.on_open

        self.wst = threading.Thread(target=self.ws.run_forever)
        self.wst.daemon = True
        self.wst.start()

    def __init__(self, server="ws://127.0.0.1:4042"):
        self.server = server
        self.connected = False
        self.start()

    def __del__(self):
        self.ws.close()


if __name__ == '__main__':
    datasocket = DataWebSocket('ws://192.168.42.1:4042')
    sleep(60)