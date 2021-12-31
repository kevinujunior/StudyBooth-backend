from django.core.checks import messages
from django.db.models.expressions import OrderBy
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
    timestamp = serializers.SerializerMethodField()
    class Meta:
        model = PrivateChat
        fields = ('id','author','friend', 'timestamp')
    
    def get_timestamp(self,obj):
        messages = Message.objects.filter(chat=obj).order_by('-timestamp')
        chat = PrivateChat.objects.get(id = obj.id)
        timestamp = chat.timestamp
        if messages:
            timestamp = messages[0].timestamp
            # print(timestamp)
        PrivateChat.objects.filter(id = obj.id).update(timestamp= timestamp)
        print(chat, " : " , chat.timestamp)
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
    # member = UserChatSerializer()
    class Meta:
        model = GroupMember
        fields = ('id','member','group','role')
        

   
class GroupMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupMessage
        fields = ('id','user','content', 'chat', 'timestamp' )
    
    
        


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
        return GroupMemberSerializer(groupmember,many=True).data
        

    
    def get_timestamp(self,obj):
        groupmessages = GroupMessage.objects.filter(chat=obj).order_by('-timestamp')
        group = GroupChat.objects.get(id = obj.id)
        timestamp = group.timestamp
        if groupmessages:
            timestamp = groupmessages[0].timestamp
            # print(timestamp)
        GroupChat.objects.filter(id = obj.id).update(timestamp= timestamp)
        print(group, " : " , group.timestamp)
        return timestamp
    
