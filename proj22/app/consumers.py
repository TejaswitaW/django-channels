from channels.generic.websocket import JsonWebsocketConsumer,AsyncJsonWebsocketConsumer
from time import sleep
import asyncio

class ChatJsonWebsocketConsumer(JsonWebsocketConsumer):
    # this handler is called when client initially opens a
    # connection and is about to finish the websocket handshake
    def connect(self):
        print("Websocket Connected....")
        self.accept()
        # self.close()# t reject the connection
    
    # This handler is called when data received from client
    # with decoded JSON content
    def receive_json(self, content, **kwargs):
        # automatically content decoded to dict 
        # Message received from client... {'msg': 'When will you come back'}
        print("Message received from client...",content)
        # Type Message received from client... <class 'dict'>
        print("Type Message received from client...",type(content))
        # now will give data in dict automatically converted to JSON
        for i in range(20):
            # automatically convert into json string and send
            self.send_json({
                'message':str(i)
            })
            sleep(1)

    # this handler is called when either connection to the client is lost,
    # either from the client closing the connection, the server closing 
    # the connection ,or loss of the socket
    def disconnect(self,close_code):
        print("Websocket disonnected....",close_code)


class ChatAsyncJsonWebsocketConsumer(AsyncJsonWebsocketConsumer):
    # this handler is called when client initially opens a
    # connection and is about to finish the websocket handshake
    async def connect(self):
        print("Websocket Connected....")
        await self.accept()
        # self.close()# t reject the connection
    
    # This handler is called when data received from client
    # with decoded JSON content
    async def receive_json(self, content, **kwargs):
        # automatically content decoded to dict 
        # Message received from client... {'msg': 'When will you come back'}
        print("Message received from client...",content)
        # Type Message received from client... <class 'dict'>
        print("Type Message received from client...",type(content))
        # now will give data in dict automatically converted to JSON
        for i in range(20):
            # automatically convert into json string and send
               await self.send_json({'message':str(i)})
               await asyncio.sleep(1)
  
    # this handler is called when either connection to the client is lost,
    # either from the client closing the connection, the server closing 
    # the connection ,or loss of the socket
    async def disconnect(self,close_code):
        print("Websocket disonnected....",close_code)