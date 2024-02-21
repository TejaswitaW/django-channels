from channels.generic.websocket import WebsocketConsumer,AsyncWebsocketConsumer
from time import sleep
import asyncio

class SyncWebsocketConsumer(WebsocketConsumer):
    def connect(self):
        print("Websocket Connected....")
        self.accept()        
    def receive(self, text_data=None, bytes_data=None):
        print('Message Received from Client...',text_data)
        self.send(text_data="Will Come Soon")
        for i in range(1,11):
            self.send(text_data=str(i)) # to send data to client
            sleep(1)
        
    def disconnect(self,close_code):
        print("Websocket disconnected...",close_code)

class AsyncWebsocketConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print("Websocket Connected....")
        await self.accept() 
    async def receive(self, text_data=None, bytes_data=None):
        print('Message Received from Client...',text_data)
        await self.send(text_data="Will Come Soon")
        for i in range(1,11):
            await self.send(text_data=str(i)) # to send data to client
            await asyncio.sleep(1)
    async def disconnect(self,close_code):
        print("Websocket disconnected...",close_code)