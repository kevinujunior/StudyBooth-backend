from django.shortcuts import render
from users.serializers import ProfileSerializer
from users.serializers import UserFollowingSerializer
from users.serializers import UserSerializer, UserNotFollowingSerializer, UserFollowsSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import  User, UserFollowing
from django.db.models import Q
from rest_framework.response import Response
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    # http_method_names = ['get']
    # queryset = User.objects.all()
    serializer_class = UserSerializer
    def get_queryset(self):
        queryset = User.objects.all() 
        if self.request.query_params.get("user", None):
            user = self.request.query_params.get("user", None)
            if(len(user)>=2):
                queryset = queryset.filter( Q(username__istartswith= user )| Q(fullName__istartswith = user))
            else:
                return None
        return queryset
    
    
    

class UserFollowingViewSet(viewsets.ModelViewSet):

    serializer_class = UserFollowingSerializer
    queryset = UserFollowing.objects.all()
    
    def get_queryset(self):
        queryset = UserFollowing.objects.all() 
        user = self.request.user
        if self.request.query_params.get("followingUser", None):
            followingUser = self.request.query_params.get("followingUser", None)
            queryset = queryset.filter(currUser=user, followingUser = followingUser)
        return queryset
        
    


class ProfileViewSet(viewsets.ModelViewSet):
    # http_method_names = ['get']
    serializer_class = ProfileSerializer
    queryset = UserFollowing.objects.all()
    
    
    def list(self, request, *args, **kwargs):
        
        user = self.request.user
        if user.id==None:
            return Response({"error":"user must login"})
        follow_users = UserFollowing.objects.filter(currUser = user)
        
        
        
        if self.request.query_params.get("viewUser", None):
            viewUser = self.request.query_params.get("viewUser", None)
            follow_viewUser = UserFollowing.objects.filter(currUser = user,followingUser = viewUser)
            
            if(follow_viewUser):
                follow_users = follow_users.filter(followingUser = viewUser)
                serializer = ProfileSerializer(follow_users,many=True)
                return Response(serializer.data)
           
            else:
                x = int(viewUser)
                y = int(user.id)
                if(x!=y):
                    print(type(user.id),"hello", type(viewUser))
                    user_details = User.objects.filter(id = viewUser)
                    serializer = UserNotFollowingSerializer(user_details,many=True)
                    return Response(serializer.data)
                else:
                    print("yo yo")
                    user_details = User.objects.filter(id = viewUser)
                    serializer = UserFollowsSerializer(user_details,many=True)
                    return Response(serializer.data)

        serializer = ProfileSerializer(follow_users,many=True)
        return Response(serializer.data)