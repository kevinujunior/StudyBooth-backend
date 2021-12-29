# from django.urls import path

# from . import views

# urlpatterns = [
#     path('', views.index, name='index'),
#     path('<str:room_name>/', views.room, name='room'),
# ]

# from django.urls import path, re_path

# from .views import (
#     ChatListView,
#     ChatDetailView,
#     ChatCreateView,
#     ChatUpdateView,
#     ChatDeleteView
# )

# app_name = 'chat'

# urlpatterns = [
#     path('', ChatListView.as_view()),
#     path('create/', ChatCreateView.as_view()),
#     path('<pk>', ChatDetailView.as_view()),
#     path('<pk>/update/', ChatUpdateView.as_view()),
#     path('<pk>/delete/', ChatDeleteView.as_view())
# ]


from django.db.models import base
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static

from chat.views import (
   PrivateChatViewSet,
   MessageViewSet,
)

router = DefaultRouter()
router.register("privatechat", PrivateChatViewSet, basename="private-chat-view")
router.register("message", MessageViewSet, basename="message-view")
# router.register("createchat", CreateChatViewSet, basename="create-chat-view")





urlpatterns = [
    path("", include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
