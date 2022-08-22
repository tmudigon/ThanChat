# Generated by Django 3.2.15 on 2022-08-21 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatroom',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='message',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='user_chatroom',
            name='user_join_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]