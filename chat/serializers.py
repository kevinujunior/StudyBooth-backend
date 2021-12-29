from django.core.checks import messages
from rest_framework import serializers
from chat.models import PrivateChat, Message
from users.serializers2 import UserChatSerializer
# from users.models import User
        
class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('__all__')
        

class ChatSerializer(serializers.ModelSerializer):
    author = UserChatSerializer()
    friend = UserChatSerializer()
    class Meta:
        model = PrivateChat
        fields = ('id','author','friend')
        

        

class CreateChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrivateChat
        fields = ('__all__')
          
        
