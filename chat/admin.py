from django.contrib import admin

from .models import Message, PrivateChat

admin.site.register(Message)
admin.site.register(PrivateChat)
