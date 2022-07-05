from api.serializers import (
    CommentSerializer,
    FollowSerializer,
    GroupSerializer,
    PostSerializer,
)
from django.shortcuts import get_object_or_404
from rest_framework import filters, permissions, viewsets
from rest_framework.pagination import LimitOffsetPagination

from .mixins import ListCreateViewSet, ListRetrieveViewSet
from .permissions import IsOwnerOrReadOnly
from posts.models import Group, Post


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (
        IsOwnerOrReadOnly,
        permissions.IsAuthenticatedOrReadOnly,
    )
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(ListRetrieveViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (
        IsOwnerOrReadOnly,
        permissions.IsAuthenticatedOrReadOnly,
    )

    def get_post(self):
        """
        Retrieves post id from url and gets post from db.
        If post with id doesn't exist, returns 404.
        """
        post_id = self.kwargs.get("post_id")
        return get_object_or_404(Post, pk=post_id)

    def get_queryset(self):
        post = self.get_post()
        new_queryset = post.comments
        return new_queryset

    def perform_create(self, serializer):
        post = self.get_post()
        serializer.save(author=self.request.user, post=post)


class FollowViewSet(ListCreateViewSet):
    serializer_class = FollowSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username', 'following__posts__text')

    def get_queryset(self):
        user = self.request.user
        following = user.follower.all()
        return following

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
