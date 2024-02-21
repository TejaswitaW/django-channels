from channels.generic.websocket import WebsocketConsumer,AsyncWebsocketConsumer

class SyncWebsocketConsumer(WebsocketConsumer):
    def connect(self):
        print("Websocket Connected....")
        self.accept() #accept the connection
        self.close() #to reject the accepted connection
        #self.close(code=4123) #to add a custom websocket error code
    def receive(self, text_data=None, bytes_data=None):
        print('Message Received from Client...',text_data)
        # you can send binary data
        #self.send(bytes_data=data)
        self.send(text_data="Will Come Soon")
    def disconnect(self,close_code):
        print("Websocket disconnected...",close_code)

class AsyncWebsocketConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print("Websocket Connected....")
        await self.accept() #accept the connection
        #await self.close() #to reject the accepted connection
        #self.close(code=4123) #to add a custom websocket error code
    async def receive(self, text_data=None, bytes_data=None):
        print('Message Received from Client...',text_data)
        # you can send binary data
        #self.send(bytes_data=data)
        await self.send(text_data="Will Come Soon")
    async def disconnect(self,close_code):
        print("Websocket disconnected...",close_code)