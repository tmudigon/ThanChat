
from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers
from .views import ChatRoomViewSet

router = routers.DefaultRouter()
router.register(r'chatRooms', ChatRoomViewSet, basename='chatRooms')

urlpatterns = [
    url(r'^', include(router.urls)),
]
