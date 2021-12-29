from django.contrib import admin

from .models import Message, PrivateChat, GroupChat, GroupMember, GroupMessage


admin.site.register(Message)
admin.site.register(PrivateChat)
admin.site.register(GroupMember)
admin.site.register(GroupChat)
admin.site.register(GroupMessage)

