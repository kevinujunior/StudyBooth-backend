from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import permissions
from rest_framework import viewsets
from chat.models import PrivateChat,Message
from .serializers import ChatSerializer, MessageSerializer
User = get_user_model()
from .pagination import StandardResultsSetPagination
def get_user_contact(username):
    user = get_object_or_404(User, username=username)
    contact = get_object_or_404(User, user=user)
    return contact


class PrivateChatViewSet(viewsets.ModelViewSet):
    serializer_class = ChatSerializer
  
    # pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        queryset = PrivateChat.objects.all()
        username = self.request.query_params.get('username', None)
        if username is not None:
            contact = get_user_contact(username)
            queryset = contact.chats.all()
        return queryset
    

class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    # pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        queryset = Message.objects.all()
        queryset = queryset.order_by("-timestamp")
        return queryset
    

