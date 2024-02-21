from channels.consumer import SyncConsumer,AsyncConsumer
from channels.exceptions import StopConsumer
from time import sleep
import asyncio
import json

class TaskSyncConsumer(SyncConsumer):
    # this handler is called when client initially opens a connection
    # is about to finish the WebSocket handshake
    def  websocket_connect(self,event):
        print("Event in Connect: ",event)
        print("Websocket Connected")
         # event
        self.send({
            'type':'websocket.accept',
            # message sending in connect not work
            # 'text': 'Connection Accepted'
        })

    # this handler is called when data received from client
    # def  websocket_receive(self,event):
    #     print("Event in Receive: ",event)
    #     print(event['text'])
    #     for i in range(10):
    #         self.send({
    #             'type':'websocket.send',
    #             'text': str(i)
    #         })
    #         sleep(1)
        
     # now sending json string   
    def  websocket_receive(self,event):
        print("Event in Receive: ",event)
        print(event['text'])
        for i in range(10):
            self.send({
                'type':'websocket.send',
                'text': json.dumps({'count':i})
            })
            sleep(1)

    # this handler is called when either connection to the client is lost,
    # either from the client closing the connection, the server closing the
    # connection, or loss of the socket
    def  websocket_disconnect(self,event):
        print("Event in Disconnect: ",event)
        print("Websocket Diconnected")
        raise StopConsumer()

class TaskAsyncSyncConsumer(AsyncConsumer):
    # this handler is called when client initially opens a connection
    # is about to finish the WebSocket handshake
    async def  websocket_connect(self,event):
        print("Event in Connect: ",event)
        print("Websocket Connected")
        # event
        await self.send({
            'type':'websocket.accept'
        })

    # this handler is called when data received from client
    async def  websocket_receive(self,event):
        print("Event in Receive: ",event)
        print(event['text'])
        for i in range(10):
            await self.send({
                'type':'websocket.send',
                'text': str(i)
            })
            await asyncio.sleep(1)

    # this handler is called when either connection to the client is lost,
    # either from the client closing the connection, the server closing the
    # connection, or loss of the socket
    async def  websocket_disconnect(self,event):
        print("Event in Disconnect: ",event)
        print("Websocket Diconnected")
        raise StopConsumer()