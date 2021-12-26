from django.db.models import base
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static

from feed.views import (
   SectionViewSet,
   PostViewSet,
   PostListViewSet,
   CommentViewSet,
   CommentListViewSet,
   LikeViewSet,
   LikeListViewSet,
)

router = DefaultRouter()
router.register("section", SectionViewSet, basename="section-view")
router.register("create_post", PostViewSet, basename="create-post-view")
router.register("get_post", PostListViewSet, basename="get-post-view")
router.register("create_comment", CommentViewSet, basename="create-comment-view")
router.register("get_comment", CommentListViewSet, basename="get-comment-view")
router.register("create_like", LikeViewSet, basename="create-like-view")
router.register("get_like", LikeListViewSet, basename="get-like-view")


urlpatterns = [
    path("", include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
