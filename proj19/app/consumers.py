from channels.generic.websocket import WebsocketConsumer,AsyncWebsocketConsumer
from time import sleep
import asyncio
import json
from asgiref.sync import async_to_sync
from channels.db import database_sync_to_async
from .models import Chat,Group

class SyncWebsocketConsumer(WebsocketConsumer):
    def connect(self):
        print("Websocket Connected....")
        print("Channel Layer....",self.channel_layer)
        print("Channel Name...",self.channel_name)
        self.group_name = self.scope['url_route']['kwargs']['groupname']
        print("Group name...",self.group_name)
        async_to_sync(self.channel_layer.group_add)(
            self.group_name,
            self.channel_name
        )
        self.accept()        
    def receive(self, text_data=None, bytes_data=None):
        print('Message Received from Client...',text_data)# client message we will recive in text_data
        data = json.loads(text_data)
        print("Data...",data)
        message = data['msg']
        group = Group.objects.get(name=self.group_name)
        chat = Chat(
            content=message,
            group=group
        )
        chat.save()
        async_to_sync(self.channel_layer.group_send)(
            self.group_name,
            {
                'type':'chat.message',
                'message':message
            }
        )
        # we will send message to client
        # type is one event and for that we will write handler as follows
    def chat_message(self,event):
        # our message will come in event
        print("Event...",event)# Event... {'type': 'chat.message', 'message': 'hi'}
        self.send(text_data=json.dumps({
            'msg':event['message']
        }))
     
    def disconnect(self,close_code):
        print("Websocket disconnected...",close_code)
        print("Channel Layer...",self.channel_layer) 
        print("Channel Name: ",self.channel_name) 
        async_to_sync(self.channel_layer.group_discard)(
            self.group_name,
            self.channel_name
        )

class AsyncWebsocketConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print("Websocket Connected....")      
        print("Channel Layer....",self.channel_layer)
        print("Channel Name...",self.channel_name)
        self.group_name = self.scope['url_route']['kwargs']['groupname']
        print("Group name...",self.group_name)
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        await self.accept() 
    async def receive(self, text_data=None, bytes_data=None):
        print('Message Received from Client...',text_data)# client message we will recive in text_data
        data = json.loads(text_data)
        print("Data...",data)
        message = data['msg']
        group = await database_sync_to_async(Group.objects.get)(name=self.group_name)
        chat = Chat(
            content=message,
            group=group
        )
        await database_sync_to_async(chat.save)()
        await self.channel_layer.group_send(
            self.group_name,
            {
                'type':'chat.message',
                'message':message
            }
        )
        # we will send message to client
        # type is one event and for that we will write handler as follows
    async def chat_message(self,event):
        # our message will come in event
        print("Event...",event)# Event... {'type': 'chat.message', 'message': 'hi'}
        await self.send(text_data=json.dumps({
            'msg':event['message']
        }))
    async def disconnect(self,close_code):
        print("Websocket disconnected...",close_code)
        print("Channel Layer...",self.channel_layer) 
        print("Channel Name: ",self.channel_name) 
        self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )