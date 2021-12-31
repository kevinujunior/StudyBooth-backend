
from users.models import UserFollowing
from feed.serializers import (
    CommentSerializer, 
    LikeSerializer, 
    PostSerializer, 
    SectionSerializer, 
    PostListSerializer, 
    CommentListSerializer, 
    LikeListSerializer)

from users.serializers import UserSerializer
from rest_framework import serializers, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from .models import Post, Comment, Like, Section
from users.models import User
from django.db.models import Q
from rest_framework.response import Response
from .pagination import CommentResultsSetPagination, StandardResultsSetPagination

class SectionViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    # http_method_names = ['post','get']
    serializer_class = SectionSerializer
    queryset = Section.objects.all()
    
    # def get_queryset(self):
    #     sections = Section.objects.all()
    

class PostViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    # authentication_classes = (TokenAuthentication,)
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    


class PostListViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    pagination_class = StandardResultsSetPagination
    def get_queryset(self):
    
        queryset = Post.objects.all()
        curruser = self.request.user
        following = UserFollowing.objects.filter(currUser = curruser)
        queryset = Post.objects.filter(
            Q(user__in= following.values_list('followingUser',flat = True)) | Q(user = curruser))
        
        if self.request.query_params.get("section", None):
            section = self.request.query_params.get("section", None)
            queryset = Post.objects.filter(postSection__id = section)
        queryset = queryset.order_by("-createdAt")
        
        if self.request.query_params.get("viewUserPost", None):
            viewUserPost = self.request.query_params.get("viewUserPost", None)
            queryset = Post.objects.filter(user = viewUserPost)
        queryset = queryset.order_by("-createdAt")
        return queryset
    
 
 
class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
   
   

class CommentListViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    # http_method_names = ['get']
    serializer_class = CommentListSerializer
    pagination_class = CommentResultsSetPagination
    
    def get_queryset(self):
        queryset = Comment.objects.filter(parent = None)
        if self.request.query_params.get("post", None):
            id = self.request.query_params.get("post", None)
            queryset = queryset.filter(post__id = id)
        queryset = queryset.order_by("-createdAt" )
        # queryset = queryset.order_by("commentText")
        return queryset
    
    
    
    @action(detail=False, methods=['GET'], name='replies')
    def replies(self, request, pk=None):
        queryset = Comment.objects.all()
        if self.request.query_params.get("parent", None):
            id = self.request.query_params.get("parent", None)
            queryset = queryset.filter(parent__id = id )
        queryset = queryset.order_by("createdAt" )
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
   
    
    


class LikeViewSet(viewsets.ModelViewSet):
    # http_method_names = ['post','get']
    serializer_class = LikeSerializer
    queryset = Like.objects.all()
    

class LikeListViewSet(viewsets.ModelViewSet):
    serializer_class = LikeListSerializer
    def get_queryset(self):
        queryset = Like.objects.all()
       
        
        if self.request.query_params.get("user", None):
            user = self.request.query_params.get("user", None)
            queryset = Like.objects.filter(likeUser__id = user)
        queryset = queryset.order_by("-likedAt")
        return queryset
    
    

