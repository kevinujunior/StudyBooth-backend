
from django.core.checks import messages
from django.db import models
from users.models import User


 
class PrivateChat(models.Model):
    user1 = models.ForeignKey(User,related_name='user1', on_delete=models.CASCADE)
    user2 = models.ForeignKey(User,related_name='user2', on_delete=models.CASCADE)
    def __str__(self):
        return "Chat "+"{}".format(self.pk)
    


class Message(models.Model):
    user = models.ForeignKey(User, related_name='message_user', on_delete=models.CASCADE, null=True, blank=True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    chat = models.ForeignKey(PrivateChat,null=True, blank=True,on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username + " : " + self.content
   