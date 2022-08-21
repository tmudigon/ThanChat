from tkinter import CASCADE
from django.db import models
from userauth.models import User

class ChatRoom(models.Model):
    name = models.CharField(max_length=20, blank=False, null=False)
    capacity = models.IntegerField(blank=False, null=False)
    link=models.CharField(max_length=50, blank=False, null=False)
    password=models.CharField(max_length=20, blank=True, null=True)

class User_ChatRoom(models.Model):
    user = models.ForeignKey(User, blank=False, null=False, on_delete=models.CASCADE)
    chat_room = models.ForeignKey(ChatRoom, blank=False, null=False, on_delete=models.CASCADE)
    user_join_time = models.DateTimeField(blank=False, null=False)
    user_exit_time = models.DateTimeField(blank=False, null=True)

class Message(models.Model):
    message_text = models.CharField(max_length=500, blank=True, null=False)
    sender = models.ForeignKey(User, blank=False, null=False, on_delete=models.CASCADE, related_name='messages_sent')
    user_receiver = models.ForeignKey(User, blank=False, null=True, on_delete=models.CASCADE, related_name='messages_received')
    chat_room_receiver = models.ForeignKey(ChatRoom, blank=False, null=True, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.CheckConstraint(
                name="%(app_label)s_%(class)s_user_receiver_or_chat_room_receiver",
                check=(
                    models.Q(user_receiver__isnull=True, chat_room_receiver__isnull=False)
                    | models.Q(user_receiver__isnull=False, chat_room_receiver__isnull=True)
                ),
            )
        ]
    
