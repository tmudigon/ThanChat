from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.http import JsonResponse


class ChatRoomViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = ChatRoom.objects.all()
    serializer_class = ChatRoomSerializer


class MessageViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def create(self, request, pk=None):
        user = self.request.user
        
        data_mod = {
            'message_text': request.data['message_text'],
            'sender': user.id,
            'user_receiver': request.data['user_receiver'],
            'chat_room_receiver': request.data['chat_room_receiver'],
        }

        serializer = MessageSerializer(data=data_mod)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED, safe=False)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST, safe=False)

    def get_queryset(self):
        chat_room_id = self.request.query_params.get('chat_room_id')
        if chat_room_id:
            try:
                return Message.objects.filter(chat_room_receiver=chat_room_id)
            except Exception:
                pass
            return queryset

        else:
            user = self.request.user
            try:
                return Message.objects.filter(user_receiver=user.id)
            except Exception:
                pass
            return queryset

            
