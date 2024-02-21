from channels.consumer import SyncConsumer,AsyncConsumer
from channels.exceptions import StopConsumer
from channels.db import database_sync_to_async
from time import sleep
import asyncio
import json
from asgiref.sync import async_to_sync
from .models import Group,Chat

class TaskSyncConsumer(SyncConsumer):
    def  websocket_connect(self,event):
        print("Event in Connect: ",event)
        # print("Websocket Connected") 
        print("Channel Layer...",self.channel_layer) #Channel Layer... RedisChannelLayer(hosts=[{'address': ('localhost', 6379)}])
        print("Channel Name: ",self.channel_name) # Channel Name:  specific.16b8a1851cb7443b83e2991611e93570!1e26810b28ff432f864cb742803b250e
        self.group_name = self.scope['url_route']['kwargs']['groupname']
        print("Group Name: ",self.group_name)
        
        # add channel to new or exsiting group
        async_to_sync(self.channel_layer.group_add)(
            self.group_name,#group name
            self.channel_name
            )
        self.send({
            'type':'websocket.accept'
        })     
 
    def  websocket_receive(self,event):
        print("Event in Receive: ",event)
        print(event['text'])   
        print("Message type: ",type(event['text'])) #<class 'str'>
        data = json.loads(event['text'])
        print("Actual Message: ",data['msg'])
        # find group object
        group = Group.objects.get(name=self.group_name)
        # create new chat object
        chat = Chat(
            content=data['msg'],
            group=group,       
            )
        chat.save()
        async_to_sync(self.channel_layer.group_send)(self.group_name,{
            'type':'chat.message',
            'message':event['text']
        })
    def chat_message(self,event):
        print("Event....", event)
        print("Event data....", event['message'])
        print("Type Event data....", type(event['message']))
        self.send({
            'type': 'websocket.send',
            'text':event['message']
        })

   
    def  websocket_disconnect(self,event):
        print("Event in Disconnect: ",event)
        print("Websocket Diconnected")
        print("Channel Layer...",self.channel_layer) 
        print("Channel Name: ",self.channel_name) 
        async_to_sync(self.channel_layer.group_discard)(
            self.group_name,
            self.channel_name)
        raise StopConsumer()
    

class TaskAsyncSyncConsumer(AsyncConsumer):
    async def  websocket_connect(self,event):
        print("Event in Connect: ",event)
        # print("Websocket Connected") 
        print("Channel Layer...",self.channel_layer) #Channel Layer... RedisChannelLayer(hosts=[{'address': ('localhost', 6379)}])
        print("Channel Name: ",self.channel_name) # Channel Name:  specific.16b8a1851cb7443b83e2991611e93570!1e26810b28ff432f864cb742803b250e
        self.group_name = self.scope['url_route']['kwargs']['groupname']
        print("Group Name: ",self.group_name)
        # add channel to new or exsiting group
        await self.channel_layer.group_add(
            self.group_name,#group name
            self.channel_name
            )
        await self.send({
            'type':'websocket.accept'
        })     
 
    async def  websocket_receive(self,event):
        print("Event in Receive: ",event)
        print(event['text'])   
        print("Message type: ",type(event['text'])) #<class 'str'>
        data = json.loads(event['text'])
        print("Actual Message: ",data['msg'])
        # find group object
        group = await database_sync_to_async(Group.objects.get)(name=self.group_name)
        # create new chat object
        chat = Chat(
            content=data['msg'],
            group=group,       
            )
        await database_sync_to_async(chat.save)()
        await self.channel_layer.group_send('self.group_name',{
            'type':'chat.message',
            'message':event['text']
        })
    async def chat_message(self,event):
        print("Event....", event)
        print("Event data....", event['message'])
        print("Type Event data....", type(event['message']))
        await self.send({
            'type': 'websocket.send',
            'text':event['message']
        })

   
    async def  websocket_disconnect(self,event):
        print("Event in Disconnect: ",event)
        print("Websocket Diconnected")
        print("Channel Layer...",self.channel_layer) 
        print("Channel Name: ",self.channel_name) 
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name)
        raise StopConsumer()

