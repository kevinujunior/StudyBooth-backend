
from django.db.models.fields import NullBooleanField
from users.serializers import CommentUserSerializer
from rest_framework import serializers
from .models import Post, Section
from .models import Comment
from .models import Like
from django.db.models import Q

class SectionSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = Section
        fields = ['id', 'sectionName', 'sectionPic']
    



class PostSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Post
        fields = ['id','postCaption', "postFile",  'user','postSection','createdAt']
        
        
    
class PostListSerializer(serializers.ModelSerializer):
    commentCount = serializers.SerializerMethodField(read_only=True)
    likeCount = serializers.SerializerMethodField(read_only= True)
    # comments  = serializers.SerializerMethodField()
    userName =  serializers.SerializerMethodField()
    userPic = serializers.SerializerMethodField()
    sectionName = serializers.SerializerMethodField()
    isLiked = serializers.SerializerMethodField()
    likeId = serializers.SerializerMethodField()
    

  
    class Meta:
        model = Post
        fields = ['id','postCaption', "postFile",  'likeCount', 'commentCount', 'user','userName','userPic','sectionName','createdAt','isLiked','likeId']
        
        
    def get_commentCount(self,obj):
        commentcount = Comment.objects.filter(post = obj)
        return len(commentcount)
    
    def get_likeCount(self,obj):
        likecount = Like.objects.filter(post = obj)
        return len(likecount)
    
    def get_postSection(self,obj):
        if(obj.postSection!=None):
            return SectionSerializer(obj.postSection).data
        else:
            return 
    
    def get_userName(self,obj):
        user_username= obj.user.username
        return user_username
    
    def get_userPic(self,obj):
        
        request = self.context.get('request')
        if(obj.user.userPic):
            photo_url = obj.user.userPic.url
            if(request ):
                return request.build_absolute_uri(photo_url)
            else:
                return None
        return None
    
    def get_sectionName(self,obj):
        if(obj.postSection!=None):
            return obj.postSection.sectionName
        else:
            return 
        
        
    def get_isLiked(self,obj):
        request = self.context.get('request', None)
        user = None
        if request:
            user = request.user
        like = Like.objects.filter(likeUser=user,post = obj)
        if(like):
            return True
        else:
            return False
        
    def get_likeId(self,obj):
        request = self.context.get('request', None)
        user = None
        if request:
            user = request.user
        like = Like.objects.filter(likeUser=user,post = obj)
        if(like):
            likeId = LikeSerializer(like,many=True).data
            return likeId[0]['id']
        else:
            return None

class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = ['id','post', 'commentatorUser','commentText', 'createdAt', 'parent']
    

class CommentChildSerializer(serializers.ModelSerializer):
    parent_id = serializers.PrimaryKeyRelatedField(queryset=Comment.objects.all(),source='parent.id')
    commentatorUser = CommentUserSerializer()
    class Meta:
        model = Comment
        fields = ('id','parent_id', 'commentatorUser', 'commentText','createdAt')

    def get_author(self, obj):
        return obj.author.username

    def create(self, validated_data):
        subject = parent.objects.create(parent=validated_data['parent']['id'], commentText=validated_data['commentText'])

    


class CommentListSerializer(serializers.ModelSerializer):
    # userName =  serializers.SerializerMethodField(read_only = True)
    # userPic = serializers.SerializerMethodField(read_only = True)
    commentatorUser = CommentUserSerializer()
    replies = serializers.SerializerMethodField()
    
    class Meta:
        model = Comment
        fields = ['id','post', 'commentatorUser','commentText', 'createdAt','replies']
    
    def get_replies(self, obj):
        replies = obj.children().order_by('-createdAt')
        if obj.is_parent:
            return CommentChildSerializer(replies, many=True).data
        return None
  
    

class LikeSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = Like
        fields = ['id', 'post','likeUser','likedAt']
    
    



class LikeListSerializer(serializers.ModelSerializer):
    
  
    
    userName =  serializers.SerializerMethodField()
    userPic = serializers.SerializerMethodField()
    class Meta:
        model = Like
        fields = ['id', 'post','likeUser','likedAt','userName','userPic']
    
    
    def get_userName(self,obj):
        user_username= obj.likeUser.username
        return user_username
    
    def get_userPic(self,obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.likeUser.userPic)
