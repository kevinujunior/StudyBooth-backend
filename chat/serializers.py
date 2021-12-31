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
    class Meta:
        model = GroupChat
        fields = ('id','name','description','groupPic','member')
    
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
        
        groupmember = GroupMember.objects.filter(group=obj)
        return GroupMemberSerializer(groupmember,many=True).data
        
    