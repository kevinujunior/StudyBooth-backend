from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey

# Create your models here.


class Post(models.Model):
    user = models.ForeignKey("users.User", on_delete=CASCADE)
    postCaption = models.TextField(null=False)
    postFile = models.FileField(upload_to="postFile/", null=True,blank=True)
    # postText = models.TextField(null=True)
    # likeCount = models.IntegerField(default=0)
    # commentCount = models.IntegerField(default=0)
    postSection = models.ForeignKey("feed.Section", on_delete=CASCADE, null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.postCaption

    


class Comment(models.Model):
    post = models.ForeignKey("feed.Post", on_delete=CASCADE)
    commentatorUser = models.ForeignKey("users.User", on_delete=CASCADE)
    commentText = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')
    
    
    def children(self):
        return Comment.objects.filter(parent=self)

    @property
    def is_parent(self):
        if self.parent is not None:
            return False
        return True
    
    def __str__(self) -> str:
        return self.commentText
        
    
    
    
    
class Like(models.Model):
    post = models.ForeignKey("feed.Post", on_delete=CASCADE)
    likeUser = models.ForeignKey("users.User", on_delete=CASCADE)
    # like = models.BooleanField(default=False)
    likedAt = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return str(self.likeUser.username)
    

class Section(models.Model):
    sectionName = models.CharField(max_length=50, unique=True,)
    sectionPic = models.ImageField(upload_to="sectionPic/",)
    
    
    def __str__(self) -> str:
        return str(self.sectionName)