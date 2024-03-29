# Generated by Django 3.2.8 on 2021-12-28 16:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0002_privatechat_unique chat'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='privatechat',
            name='unique chat',
        ),
        migrations.RemoveField(
            model_name='privatechat',
            name='user1',
        ),
        migrations.RemoveField(
            model_name='privatechat',
            name='user2',
        ),
        migrations.AddField(
            model_name='privatechat',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='author', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='privatechat',
            name='friend',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='friend', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddConstraint(
            model_name='privatechat',
            constraint=models.UniqueConstraint(fields=('author', 'friend'), name='unique chat'),
        ),
    ]
