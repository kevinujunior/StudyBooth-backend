from django.core.checks import messages
from rest_framework import serializers
from chat.models import PrivateChat, Message

        
class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('__all__')
        

class ChatSerializer(serializers.ModelSerializer):
    # user1 = UserSerializer()
    # user2 = UserSerializer()
    class Meta:
        model = PrivateChat
        fields = ('id','user1','user2')
        
        
