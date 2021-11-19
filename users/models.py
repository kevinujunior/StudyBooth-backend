from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import BLANK_CHOICE_DASH, NullBooleanField



class User(AbstractUser):
    fullName = models.CharField(max_length=150)
    userPic =  models.ImageField(upload_to='userPic/', null=True, blank=True, default=None)
    userBio =  models.TextField(null=True,blank=True)
    # userPostCount = models.IntegerField(null = True,default=0)
    # userQuestionCount = models.IntegerField(null = True,default=0)
    # userAnswerCount = models.IntegerField(null=True,default=0)
    
    
    
    
class UserFollowing(models.Model):
    currUser = models.ForeignKey('users.User', related_name="following", on_delete=models.CASCADE, default=None)
    followingUser = models.ForeignKey('users.User', related_name="followers", on_delete=models.CASCADE, default=None)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['currUser','followingUser'],  name="unique_followers")
        ]
    ordering = ["-created"]
    
    def __str__(self):
        return f"{self.user_id} follows {self.following_user_id}"
    
  
    
