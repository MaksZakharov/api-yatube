from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from api.permissions import IsAuthorOrReadOnly
from api.serializers import CommentSerializer, GroupSerializer, PostSerializer
from posts.models import Group, Post


class PostViewSet(viewsets.ModelViewSet):
    """
    Вьюсет для модели Post с CRUD операциями.

    Ограничения:
    - Только авторизованные пользователи могут создавать посты.
    - Только автор поста может изменять или удалять его.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    """
    Вьюсет для комментариев, связанных с постами.

    Ограничения:
    - Только авторизованные пользователи могут создавать комментарии.
    - Только автор комментария может его изменять или удалять.
    """

    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def get_post(self):
        """Возвращает объект поста или 404."""
        return get_object_or_404(Post, id=self.kwargs.get('post_id'))

    def get_queryset(self):
        """Возвращает комментарии к конкретному посту."""
        post = self.get_post()
        return post.post_comments.all()

    def perform_create(self, serializer):
        """При создании комментария назначает автора и пост."""
        post = self.get_post()
        serializer.save(author=self.request.user, post=post)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Вьюсет для модели Group.

    Разрешён только просмотр списка и деталей групп.
    """

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]
