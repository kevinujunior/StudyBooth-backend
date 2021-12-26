import os, django
from users.models import UserFollowing
from faker import Faker
import random
from users.models import User

fake = Faker()
Faker.seed(999)


def populate(N):
    bio = fake.text()
    pic = "/userPic/" + str(random.randint(1,3)) +".jpg"
    user = User.objects.create_superuser(username='admin', password="admin", fullName="Dabsay",userPic=pic,userBio=bio)
    user = User.objects.create_superuser(username='kevin', password="admin",  fullName="Kevin")
    user = User.objects.create_superuser(username='uditdabsay', password="admin",  fullName="Udit Dabsay")
    # for _ in range(2):
    #     add_superuser()
    for i in range(N):
        print("user=",i)
        add_user()
    # for _ in range(2):
    #     add_user_following()


# def add_superuser():
#     username = fake.user_name()
#     fullName = fake.name()
#     email=fake.email()
#     password = fake.password(length=12)
#     user = User.objects.create_superuser(username=username, email = email, fullName=fullName,  password="admin")
 




def add_user():
    username = fake.user_name()
    fullName = fake.name()
    password = fake.password(length=12)
    bio = fake.text()
    user = User.objects.create_user(
        username = username,
        email=fake.email(),
        fullName = fullName,
        password=password,
        userBio = bio,
        userPic = "/userPic/" + str(random.randint(1,3)) +".jpg",

    )

# def add_user_following():
#     users = User.objects.all()
#     UserFollowing.objects.create(
#         currUser = users[random.randint(0, users.count() - 1)],
#         followingUser = users[random.randint(0, users.count() - 1)] ,
#     )