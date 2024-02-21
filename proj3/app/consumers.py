from channels.consumer import SyncConsumer,AsyncConsumer

class TaskSyncConsumer(SyncConsumer):
    # this handler is called when client initially opens a connection
    # is about to finish the WebSocket handshake
    def  websocket_connect(self,event):
        print("Event in Connect: ",event)
        print("Websocket Connected")
       

    # this handler is called when data received from client
    def  websocket_receive(self,event):
        print("Event in Receive: ",event)
        print("Websocket Received")

    # this handler is called when either connection to the client is lost,
    # either from the client closing the connection, the server closing the
    # connection, or loss of the socket
    def  websocket_disconnect(self,event):
        print("Event in Disconnect: ",event)
        print("Websocket Diconnected")

class TaskAsyncSyncConsumer(AsyncConsumer):
    # this handler is called when client initially opens a connection
    # is about to finish the WebSocket handshake
    async def  websocket_connect(self,event):
        print("Event in Connect: ",event)
        print("Websocket Connected")

    # this handler is called when data received from client
    async def  websocket_receive(self,event):
        print("Event in Receive: ",event)
        print("Websocket Received")

    # this handler is called when either connection to the client is lost,
    # either from the client closing the connection, the server closing the
    # connection, or loss of the socket
    async def  websocket_disconnect(self,event):
        print("Event in Disconnect: ",event)
        print("Websocket Diconnected")