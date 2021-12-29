from django.db import models
from users.models import User


user_role_choices = (
    ("A", "Admin"),
    ("M", "Member"),
)
  

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
    content = models.TextField(null=False,blank=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    chat = models.ForeignKey(PrivateChat, related_name='chat', on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username + " : " + self.content
   

class GroupChat(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200, null=True, blank=True)
    groupPic =  models.ImageField(upload_to='groupPic/', default=None, null=True, blank=True)
    def __str__(self):
        return self.name

    
class GroupMember(models.Model):
    member = models.ForeignKey(User,related_name='member',on_delete=models.CASCADE,)
    group = models.ForeignKey(GroupChat, related_name='group', on_delete=models.CASCADE,)
    role = models.CharField(max_length=2, choices=user_role_choices)
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['member', 'group'],  name='unique group member')
        ]
    

    def __str__(self):
        return self.member.username + " : " + self.group.name
    

class GroupMessage(models.Model):
    user = models.ForeignKey(User, related_name='group_message_user', on_delete=models.CASCADE,)
    content = models.TextField(null=False,blank=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    chat = models.ForeignKey(GroupChat, related_name='group_chat', on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username + " : " + self.content