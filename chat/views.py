from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import permissions
from rest_framework import viewsets
from chat.models import PrivateChat,Message,GroupChat,GroupMessage,GroupMember
from .serializers import ChatSerializer, GroupMessageSerializer, MessageSerializer, CreateChatSerializer,CreateGroupChatSerializer, GroupMemberSerializer, GroupMessage
User = get_user_model()
from .pagination import StandardResultsSetPagination
from rest_framework.response import Response
from django.db.models import Q
from rest_framework import  status

def get_user_contact(username):
    user = get_object_or_404(User, username=username)
    contact = get_object_or_404(User, user=user)
    return contact


class PrivateChatViewSet(viewsets.ModelViewSet):
    serializer_class = CreateChatSerializer
    queryset = PrivateChat.objects.all()
    

    def create(self,request):
        author = request.data['author']
        friend = request.data['friend']
        serializer = CreateChatSerializer(data=request.data)
        user = PrivateChat.objects.filter(Q(author= author, friend = friend) | Q(author=friend, friend = author))
        if not user and (author!=friend):
            if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({
                'error': 'Invalid Request',
            })
    

class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    # pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        queryset = Message.objects.all()
        queryset = queryset.order_by("-timestamp")
        return queryset
    


class GroupViewSet(viewsets.ModelViewSet):
    serializer_class = CreateGroupChatSerializer
    queryset = GroupChat.objects.all()
    def create(self, request, format=None): 
        serializer = CreateGroupChatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            group = GroupChat.objects.get(id=serializer.data['id'])
            GroupMember.objects.create(member=request.user, group = group, role="A")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      

class GroupMemberViewSet(viewsets.ModelViewSet):
    serializer_class = GroupMemberSerializer
    queryset = GroupMember.objects.all()
    
    
class GroupMessageViewSet(viewsets.ModelViewSet):
    serializer_class = GroupMessageSerializer
    queryset = GroupMessage.objects.all()
    
    def create(self, request, format=None): 
        serializer = GroupMessageSerializer(data=request.data)
        member = request.data['user']
        group = request.data['chat']
        group_member = GroupMember.objects.filter(member = member, group =  group)
        if group_member:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({
                'error': 'Invalid Request',
            })
      
    
   



    
    