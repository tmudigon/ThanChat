from django.shortcuts import render
from rest_framework import viewsets
from .models import User, ChatRoom, User_ChatRoom, Message
from .serializers import UserSerializer, ChatRoomSerializer, User_ChatRoomSerializer, MessageSerializer
from rest_framework.permissions import IsAuthenticated

class ChatRoomViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = ChatRoom.objects.all()
    serializer_class = ChatRoomSerializer

