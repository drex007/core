import json
from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
from asgiref.sync import async_to_sync 

class NotificationConsumer(WebsocketConsumer):

        def connect(self):
            self.room_name = 'test_consumer'
            self.room_group_name = "test_consumer_group"
            async_to_sync(self.channel_layer.group_add)(
                self.room_name,self.room_group_name)
            
            self.accept()

            self.send(text_data=json.dumps({'status': 'connected from django channels'}))
        
        def receive(self, text_data):
            print(text_data)
            self.send(text_data=json.dumps({'status': 'We got you'}))
        
        def disconnect(self,*args ,**kwargs):
            print('Disconnected')
            
        
        def send_notification(self, event):
            print('notification')
            print(event)
            print('notification')
            