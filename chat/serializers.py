from django.core.checks import messages
from rest_framework import serializers
from chat.models import PrivateChat, Message
from users.serializers2 import UserChatSerializer
# from users.models import User
from django.db.models import Q
from rest_framework.response import Response
        
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
        fields = ('id','author','friend')
        

   
        
    # def save(self):
    #     author = self.validated_data['author']
    #     friend = self.validated_data['friend']
    #     user = PrivateChat.objects.filter(Q(author= author, friend = friend) | Q(author=friend, friend = author))
    #     if not user and (author!=friend):
    #         return PrivateChat.objects.create(**self.validated_data)
    #     else:
    #         return Response({
    #             'id': 'none',
    #         'author' : 'none',
    #         'friend' : 'none',
    
    #         })
       
          
        
