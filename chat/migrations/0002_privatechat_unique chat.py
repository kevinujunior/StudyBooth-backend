# Generated by Django 3.2.8 on 2021-12-28 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='privatechat',
            constraint=models.UniqueConstraint(fields=('user1', 'user2'), name='unique chat'),
        ),
    ]
