# Generated by Django 3.2.8 on 2021-12-31 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0012_privatechat_timstamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='privatechat',
            name='timstamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]