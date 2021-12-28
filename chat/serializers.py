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
    user1 = UserChatSerializer()
    # user1 = serializers.SerializerMethodField()
    user2 = UserChatSerializer()
    class Meta:
        model = PrivateChat
        fields = ('id','user1','user2')
        
    # def get_user1(self,obj):
    #     user1 = User.objects.filter(id = obj.user1.id)
    #     print(user1)
    #     user = UserChatSerializer(user1)
    #     return user.data
    
    # def get_user2(self,obj):
    #     user = us.UserChatSerializer(obj.user2)
    #     return user.data
        
    # def get_author(self,obj):
    #     author = User.objects.filter(id = obj.user1.id)
    #     print(author)
    #     user = us.UserChatSerializer(author)
    #     return user.data
        
        
