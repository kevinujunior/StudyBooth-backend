from users.models import User
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json
from .models import GroupChat, Message, GroupMessage
from .models import PrivateChat


class ChatConsumer(WebsocketConsumer):

    def fetch_messages(self, data):
        messages = Message.objects.filter(chat=data['chatId']).order_by('-timestamp')[:30]
        content = {
            'command': 'messages',
            'messages': self.messages_to_json(messages)
        }
        self.send_message(content)

    def new_message(self, data):
        user = data['from']
        user = User.objects.filter(username=user)[0]
        message = Message.objects.create(
            user=user, 
            chat=PrivateChat.objects.get(id=data['chatId']),
            content=data['message'])
        chat=data['chatId']
        messages = Message.objects.filter(chat=chat).order_by('-timestamp')
        room = PrivateChat.objects.get(id = chat )
        timestamp = room.timestamp
        
        if messages:
            timestamp = messages[0].timestamp
        PrivateChat.objects.filter(id = chat).update(timestamp= timestamp)
    
        content = {
            'command': 'new_message',
            'message': self.message_to_json(message)
        }
        return self.send_chat_message(content)
    
    def fetch_group_messages(self, data):
        messages = GroupMessage.objects.filter(chat=data['chatId']).order_by('-timestamp')[:30]
        content = {
            'command': 'group_messages',
            'messages': self.messages_to_json(messages)
        }
        self.send_message(content)

    def new_group_message(self, data):
        user = data['from']
        user = User.objects.filter(username=user)[0]
        message = GroupMessage.objects.create(
            user=user, 
            chat=GroupChat.objects.get(id=data['chatId']),
            content=data['message'])
        chat=data['chatId']
        messages = GroupMessage.objects.filter(chat=chat).order_by('-timestamp')
        room = GroupChat.objects.get(id = chat )
        timestamp = room.timestamp
        
        if messages:
            timestamp = messages[0].timestamp
        GroupChat.objects.filter(id = chat).update(timestamp= timestamp)
        content = {
            'command': 'new_group_message',
            'message': self.message_to_json(message)
        }
        return self.send_chat_message(content)

    def messages_to_json(self, messages):
        result = []
        for message in messages:
            result.append(self.message_to_json(message))
        return result

    def message_to_json(self, message):
        return {
            'id' : message.id,
            'user': message.user.username,
            'content': message.content,
            'timestamp': str(message.timestamp)
        }

    commands = {
        'fetch_messages': fetch_messages,
        'new_message': new_message,
        'fetch_group_messages' : fetch_group_messages,
        'new_group_message' : new_group_message,
    }

    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    def receive(self, text_data):
        data = json.loads(text_data)
        self.commands[data['command']](self, data)
        

    def send_chat_message(self, message):    
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    def send_message(self, message):
        self.send(text_data=json.dumps(message))

    def chat_message(self, event):
        message = event['message']
        self.send(text_data=json.dumps(message))