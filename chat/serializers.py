from django.core.checks import messages
from django.db.models.expressions import OrderBy
from django.http import request
from rest_framework import serializers
from chat.models import GroupChat, GroupMember, GroupMessage, PrivateChat, Message
from users.serializers2 import UserChatSerializer, UserGroupChatSerializer
# from users.models import User
from django.db.models import Q
from rest_framework.response import Response
        
class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('id','content','timestamp','user','chat')
    
    
    def create(self,validated_data): 
        print("yo created")
        instance = Message.objects.create(**validated_data)
        chat=validated_data['chat'].id
        messages = Message.objects.filter(chat=chat).order_by('-timestamp')
        room = PrivateChat.objects.get(id = chat)
        timestamp = room.timestamp
        
        if messages:
            timestamp = messages[0].timestamp
        PrivateChat.objects.filter(id = chat).update(timestamp= timestamp)
        return instance
       
    
    
    
        

class ChatSerializer(serializers.ModelSerializer):
    author = UserChatSerializer()
    friend = UserChatSerializer()
    timestamp = serializers.SerializerMethodField()
    class Meta:
        model = PrivateChat
        fields = ('id','author','friend', 'timestamp')
    
    def get_timestamp(self,obj):
        timestamp = obj.timestamp
        return timestamp

        

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


class GroupMemberSerializer2(serializers.ModelSerializer):
    member = UserGroupChatSerializer()
    class Meta:
        model = GroupMember
        fields = ('id','member','group','role')
        

   
class GroupMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupMessage
        fields = ('id','user','content', 'chat', 'timestamp' )
    
    def create(self,validated_data): 
        instance = GroupMessage.objects.create(**validated_data)
        chat=validated_data['chat'].id
        messages = GroupMessage.objects.filter(chat=chat).order_by('-timestamp')
        room = GroupChat.objects.get(id = chat)
        timestamp = room.timestamp
        if messages:
            timestamp = messages[0].timestamp
        GroupChat.objects.filter(id = chat).update(timestamp= timestamp)
        return instance
       
    
    
        


class GroupChatSerializer(serializers.Serializer):   
    id = serializers.SerializerMethodField()
    name = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    groupPic = serializers.SerializerMethodField()
    member = serializers.SerializerMethodField() 
    # messages =  serializers.SerializerMethodField() 
    timestamp = serializers.SerializerMethodField()
    class Meta:
        model = GroupChat
        fields = ('id','name','description','groupPic','member', 'timestamp')
    
    def get_id(self,obj):
        return obj.id

    def get_name(self,obj):
        return obj.name
    
    def get_description(self,obj):
        return obj.description
    
    def get_groupPic(self, obj):
            request = self.context.get('request')
            if self.context.get('request'):
                if obj.groupPic and hasattr(obj.groupPic, 'url'):
                    photo_url = obj.userPic.url
                    return request.build_absolute_uri(photo_url)
            else:
                    return None
        
    def get_member(self,obj):
        
        groupmember = GroupMember.objects.filter(group=obj).order_by('role')
        return GroupMemberSerializer2(groupmember,many=True).data
        
    
    
    def get_timestamp(self,obj):
        timestamp = obj.timestamp
        return timestamp
    
