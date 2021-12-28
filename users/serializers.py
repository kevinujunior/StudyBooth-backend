
from chat.models import PrivateChat
from rest_framework import serializers
from django.db import transaction
from dj_rest_auth.registration.serializers import RegisterSerializer
from .models import  User, UserFollowing
from feed.models import Post
import chat.serializers as chat
from django.db.models import Q


#custom serializer for rest_auth 
# full_name is added field
class CustomRegisterSerializer(RegisterSerializer):
    
    fullName = serializers.CharField(max_length=30)
    # Define transaction.atomic to rollback the save operation in case of error
    @transaction.atomic
    def save(self, request):
        user = super().save(request)
        user.fullName = self.data.get('fullName')
        user.save()
        return user
    
  

class UserFollowingSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserFollowing
        fields = ["id", "currUser","followingUser",]  
        
class FollowingSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserFollowing
        fields = ["id", "followingUser",]




class FollowerSerializer(serializers.ModelSerializer): 
    followerUser = serializers.SerializerMethodField()
    class Meta:
        model = UserFollowing
        fields = ["id", "followerUser",]
    
    def get_followerUser(self,obj):
        return obj.currUser.id


class UserSerializer(serializers.ModelSerializer):
    # following = serializers.SerializerMethodField()
    # followers = serializers.SerializerMethodField()
    followingCount = serializers.SerializerMethodField()
    followerCount= serializers.SerializerMethodField()
    postCount= serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ['id', 'username', 'fullName', 'userPic','email','userBio','postCount','followingCount','followerCount']
        
    def get_following(self, obj):
        return FollowingSerializer(obj.following.all(), many=True).data

    def get_followers(self, obj):
        return FollowerSerializer(obj.followers.all(), many=True).data
    
    def get_followingCount(self,obj):
        following = UserFollowing.objects.filter(currUser = obj)
        return len(following)

    def get_followerCount(self,obj):
        follower = UserFollowing.objects.filter(followingUser = obj)
        return len(follower)
    
    def get_postCount(self,obj):
        posts = Post.objects.filter(user = obj)
        return len(posts)
    
        
class UserFollowsSerializer(serializers.ModelSerializer):
    followingCount = serializers.SerializerMethodField()
    followerCount= serializers.SerializerMethodField()
    postCount= serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ['id', 'username', 'fullName', 'userPic','email','userBio','postCount','followingCount','followerCount',]
        
    def get_following(self, obj):
        return FollowingSerializer(obj.following.all(), many=True).data

    def get_followers(self, obj):
        return FollowerSerializer(obj.followers.all(), many=True).data
    
    def get_followingCount(self,obj):
        following = UserFollowing.objects.filter(currUser = obj)
        return len(following)

    def get_followerCount(self,obj):
        follower = UserFollowing.objects.filter(followingUser = obj)
        return len(follower)
    
    def get_postCount(self,obj):
        posts = Post.objects.filter(user = obj)
        return len(posts)
    
    # def get_viewUserPosts(self,obj):
    #     posts = Post.objects.filter(user= obj)
    #     return fs.PostListSerializer(posts,many=True).data
  


class UserNotFollowingSerializer(serializers.ModelSerializer):
    followingCount = serializers.SerializerMethodField()
    followerCount= serializers.SerializerMethodField()
    postCount= serializers.SerializerMethodField()
    isFollowedByCurrUser = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ['id', 'username', 'fullName', 'userPic','email','userBio','postCount','followingCount','followerCount','isFollowedByCurrUser']
        
    def get_following(self, obj):
        return FollowingSerializer(obj.following.all(), many=True).data

    def get_followers(self, obj):
        return FollowerSerializer(obj.followers.all(), many=True).data
    
    def get_followingCount(self,obj):
        following = UserFollowing.objects.filter(currUser = obj)
        return len(following)

    def get_followerCount(self,obj):
        follower = UserFollowing.objects.filter(followingUser = obj)
        return len(follower)
    
    def get_postCount(self,obj):
        posts = Post.objects.filter(user = obj)
        return len(posts)

    def get_isFollowedByCurrUser(self,obj):
        return False

class CommentUserSerializer(serializers.ModelSerializer):
    # userPic = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ['id', 'username', 'userPic']
        
    # def get_userPic(self,obj):
    #     request = self.context.get("request")
    #     return request.build_absolute_uri(obj.userPic.url)
    
    # def get_userPic(self, obj):
    #         request = self.context.get('request')
    #         if self.context.get('request'):
    #             if obj.userPic and hasattr(obj.userPic, 'url'):
    #                 photo_url = obj.userPic.url
    #             return request.build_absolute_uri(photo_url)
    #         else:
    #                 return None
        
    

class ProfileSerializer(serializers.Serializer):
    viewUser = serializers.SerializerMethodField()
    isFollowedByCurrUser = serializers.SerializerMethodField()
    class Meta:
        model = UserFollowing
        fields = ['viewUser','isFollowedByCurrUSer']
        
    def get_viewUser(self,obj):
        return UserFollowsSerializer(obj.followingUser).data
    
    def get_isFollowedByCurrUser(self,obj):
        return True
    
    
