from rest_framework import serializers
from .models import User, ChatRoom, User_ChatRoom, Message

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']


class ChatRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatRoom
        fields = '__all__'


class User_ChatRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_ChatRoom
        fields = '__all__'


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'