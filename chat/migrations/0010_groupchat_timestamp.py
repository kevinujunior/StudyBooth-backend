# Generated by Django 3.2.8 on 2021-12-31 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0009_remove_groupchat_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='groupchat',
            name='timestamp',
            field=models.DateTimeField(default=None),
        ),
    ]
