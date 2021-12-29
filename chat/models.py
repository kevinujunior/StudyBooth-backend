
from django.core.checks import messages
from django.db import models
from users.models import User
from django.db.models import Q


 
class PrivateChat(models.Model):
    author = models.ForeignKey(User,related_name='author',on_delete=models.CASCADE,)
    friend = models.ForeignKey(User,related_name='friend', on_delete=models.CASCADE)
    def __str__(self):
        return "Chat "+"{}".format(self.pk)
    

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['author', 'friend'],  name='unique chat')
        ]
    


class Message(models.Model):
    user = models.ForeignKey(User, related_name='message_user', on_delete=models.CASCADE,)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    chat = models.ForeignKey(PrivateChat, related_name='chat', on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username + " : " + self.content
   