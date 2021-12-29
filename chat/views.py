from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import permissions
from rest_framework import viewsets
from chat.models import PrivateChat,Message
from .serializers import ChatSerializer, MessageSerializer, CreateChatSerializer
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
    





    
    