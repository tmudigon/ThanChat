
from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers
from .views import ChatRoomViewSet, MessageViewSet

router = routers.DefaultRouter()
router.register(r'chatRooms', ChatRoomViewSet, basename='chatRooms')
router.register(r'messages', MessageViewSet, basename='messages')

urlpatterns = [
    url(r'^', include(router.urls)),
]
