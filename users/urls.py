from django.db.models import base
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from users.views import (
   UnfollowViewSet,
   UserViewSet,
   UserFollowingViewSet,
    ProfileViewSet,
    UserChatsViewSet
)

router = DefaultRouter()
router.register("userview", UserViewSet, basename="user-view")
router.register("followingview", UserFollowingViewSet, basename="following-view")
router.register("unfollow", UnfollowViewSet, basename="unfollow-view")
router.register("profileview", ProfileViewSet, basename="profile-view")
router.register("userchats", UserChatsViewSet, basename="user-chat-view")



urlpatterns = [
    path("", include(router.urls)),
]
