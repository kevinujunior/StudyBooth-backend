from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import permissions
from rest_framework import viewsets
from chat.models import PrivateChat,Message
from .serializers import ChatSerializer, MessageSerializer, CreateChatSerializer
User = get_user_model()
from .pagination import StandardResultsSetPagination
def get_user_contact(username):
    user = get_object_or_404(User, username=username)
    contact = get_object_or_404(User, user=user)
    return contact


class PrivateChatViewSet(viewsets.ModelViewSet):
    serializer_class = CreateChatSerializer
    queryset = PrivateChat.objects.all()
    

# class CreateChatViewSet(viewsets.ModelViewSet):
#     serializer_class = CreateChatSerializer
#     queryset = PrivateChat.objects.all()
    

class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    # pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        queryset = Message.objects.all()
        queryset = queryset.order_by("-timestamp")
        return queryset
    





    
    