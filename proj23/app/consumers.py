from channels.generic.websocket import JsonWebsocketConsumer,AsyncJsonWebsocketConsumer
from time import sleep
import asyncio
from asgiref.sync import async_to_sync

class ChatJsonWebsocketConsumer(JsonWebsocketConsumer):
    # this handler is called when client initially opens a
    # connection and is about to finish the websocket handshake
    def connect(self):
        print("Websocket Connected....")
        print("Channel Layer: ",self.channel_layer)
        print("Channel Name: ",self.channel_name)
        self.group_name = self.scope['url_route']['kwargs']['groupname']
        print("Group name: ",self.group_name)
        async_to_sync(self.channel_layer.group_add)(
            self.group_name,
            self.channel_name # in one group there can be multiple channels
        )
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
        # message is sent in group, to send to client, we need to write event handler chat_message
        async_to_sync(self.channel_layer.group_send)(
            self.group_name,
            {
                'type':'chat.message',
                'message':content['msg']
            }
        )
    
    def chat_message(self,event):
        print("Event...",event)
        # it will encode to json
        self.send_json({
            'message':event['message']
        })
    

    # this handler is called when either connection to the client is lost,
    # either from the client closing the connection, the server closing 
    # the connection ,or loss of the socket
    def disconnect(self,close_code):
        print("Websocket disonnected....",close_code)
        print("Channel Layer: ",self.channel_layer)
        print("Channel Name: ",self.channel_name)
        async_to_sync(self.channel_layer.group_discard)(
            self.group_name,
            self.channel_name # in one group there can be multiple channels
        )



class ChatAsyncJsonWebsocketConsumer(AsyncJsonWebsocketConsumer):
    # this handler is called when client initially opens a
    # connection and is about to finish the websocket handshake
    async def connect(self):
        print("Websocket Connected....")
        print("Channel Layer: ",self.channel_layer)
        print("Channel Name: ",self.channel_name)
        self.group_name = self.scope['url_route']['kwargs']['groupname']
        print("Group name: ",self.group_name)
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name # in one group there can be multiple channels
        )
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
        # message is sent in group, to send to client, we need to write event handler chat_message
        await self.channel_layer.group_send(
            self.group_name,
            {
                'type':'chat.message',
                'message':content['msg']
            }
        )
    
    async def chat_message(self,event):
        print("Event...",event)
        # it will encode to json
        await self.send_json({
            'message':event['message']
        })
    
  
    # this handler is called when either connection to the client is lost,
    # either from the client closing the connection, the server closing 
    # the connection ,or loss of the socket
    async def disconnect(self,close_code):
        print("Websocket disonnected....",close_code)
        print("Channel Layer: ",self.channel_layer)
        print("Channel Name: ",self.channel_name)
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name # in one group there can be multiple channels
        )