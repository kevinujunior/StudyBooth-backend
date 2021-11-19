from datetime import datetime
from django.core.checks import messages
from django.db.models.fields.files import ImageFileDescriptor
from django.utils.timezone import make_aware
from faker import Faker
import random

fake = Faker()
Faker.seed(999)

from feed.models import(
    Section,
    Post,
    Comment,
    Like,
)

from users.models import User

image_url_list = ["/postFile/1.jpg", "/postFile/2.jpg","/postFile/3.PNG"]

def populate(total):
    populate_section(total)
    populate_post(100)
    populate_comment(300)
    populate_like(1000)
    

def populate_section(total):
    for _ in range(total):
        sectionName=fake.word(),
       
        Section.objects.create(
            sectionName = sectionName[0],
            sectionPic ="/sectionPic/" + str(random.randint(1,7)) +".jpg",
        )
        

def populate_post(total):
    for i in range(total):
        print("feed=",i)
        users = User.objects.all()
        sections = Section.objects.all()
        index =random.randint(0, users.count() - 1)
        Post.objects.create(
            user=users[index],
            postCaption = fake.text(max_nb_chars=20),
            # postFile = image_url_list[random.randint(0,len(image_url_list)-1)],
            postFile =  "/postFile/" + str(random.randint(1,7)) +".jpg",
          
            postSection = sections[random.randint(0, sections.count() - 1)],
            createdAt = make_aware(datetime.now()),
        )

def populate_comment(total):
    for i in range(total):
        print("comment=",i)
        posts = Post.objects.all()
        users = User.objects.all()
        index =random.randint(0, users.count() - 1)
        Comment.objects.create(
            post=posts[random.randint(0, posts.count() - 1)],
           commentatorUser = users[index],
        #    userFields = users[index],
           commentText =  fake.text(max_nb_chars =20),
           createdAt = make_aware(datetime.now()),
        )


def populate_like(total):
    for i in range(total):
        print("like=",i)
        posts = Post.objects.all()
        users = User.objects.all()
        index =random.randint(0, users.count() - 1)
        Like.objects.create(
            post=posts[random.randint(0, posts.count() - 1)],
            likeUser = users[index],
            # userFields = users[index],
           likedAt = make_aware(datetime.now()),
        )
