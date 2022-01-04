from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import BLANK_CHOICE_DASH


class User(AbstractUser):
    fullName = models.CharField(max_length=150)
    userPic =  models.FileField(upload_to='userPic/', default=None)
    userBio =  models.TextField(null=True,blank=True)
   
    
    
    
    
class UserFollowing(models.Model):
    currUser = models.ForeignKey('users.User', related_name="following", on_delete=models.CASCADE, default=None)
    followingUser = models.ForeignKey('users.User', related_name="followers", on_delete=models.CASCADE, default=None)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['currUser', 'followingUser'], name='unique followers')
        ]
    
    def __str__(self):
        return f"{self.currUser} follows {self.followingUser}"
    
  
    
