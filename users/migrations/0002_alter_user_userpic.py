# Generated by Django 3.2.8 on 2022-01-04 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='userPic',
            field=models.FileField(default=None, upload_to='userPic/'),
        ),
    ]