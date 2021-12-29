from django.core.checks import messages
from django.http import request
from rest_framework import serializers
from chat.models import GroupChat, GroupMember, GroupMessage, PrivateChat, Message
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
        

     

class CreateGroupChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupChat
        fields = ('id','name','description','groupPic')
   

   
class GroupMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupMember
        fields = ('id','member','group','role')
        

   
class GroupMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupMessage
        fields = ('id','user','content', 'chat', 'timestamp' )
        

