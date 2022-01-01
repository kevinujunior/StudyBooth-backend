
from rest_framework import serializers
from .models import  User

class UserChatSerializer(serializers.Serializer):
    id = serializers.SerializerMethodField()
    username = serializers.SerializerMethodField()
    fullName = serializers.SerializerMethodField()
    userPic = serializers.SerializerMethodField()
    email = serializers.SerializerMethodField()
    userBio = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ['id', 'username', 'fullName', 'userPic','email','userBio']    
    
    
    def get_id(self,obj):
        return obj.id
    def get_username(self,obj):
        return obj.username
    
    def get_fullName(self,obj):
        return obj.fullName
    
    def get_userPic(self, obj):
            request = self.context.get('request')
            if self.context.get('request'):
                if obj.userPic and hasattr(obj.userPic, 'url'):
                    photo_url = obj.userPic.url
                    return request.build_absolute_uri(photo_url)
            else:
                    return None
    
    def get_email(self,obj):
        return obj.email
    
    def get_userBio(self,obj):
        return obj.userBio
    


class UserGroupChatSerializer(serializers.Serializer):
    id = serializers.SerializerMethodField()
    username = serializers.SerializerMethodField()
    fullName = serializers.SerializerMethodField()
    userPic = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ['id', 'username', 'fullName', 'userPic',]    
    
    
    def get_id(self,obj):
        return obj.id
    def get_username(self,obj):
        return obj.username
    
    def get_fullName(self,obj):
        return obj.fullName
    
    def get_userPic(self, obj):
            request = self.context.get('request')
            if self.context.get('request'):
                if obj.userPic and hasattr(obj.userPic, 'url'):
                    photo_url = obj.userPic.url
                    return request.build_absolute_uri(photo_url)
            else:
                    return None
    

    


