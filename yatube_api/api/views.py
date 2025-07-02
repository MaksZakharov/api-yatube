from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated

from posts.models import Comment, Group, Post

from api.permissions import IsAuthorOrReadOnly
from api.serializers import CommentSerializer, GroupSerializer, PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    """
    Вьюсет для модели Post с CRUD операциями.

    Ограничения:
    - Только аутентифицированные пользователи могут создавать посты.
    - Только автор поста может изменять или удалять его.
    """

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        """При создании поста автоматически назначает автора."""
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    """
    Вьюсет для комментариев, связанных с постами.

    Ограничения:
    - Только аутентифицированные пользователи могут создавать комментарии.
    - Только автор комментария может его изменять или удалять.
    """

    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def get_queryset(self):
        """Возвращает комментарии к конкретному посту."""
        post_id = self.kwargs.get('post_id')
        return Comment.objects.filter(post__id=post_id)

    def perform_create(self, serializer):
        """При создании комментария автоматически назначает автора и пост."""
        post_id = self.kwargs.get('post_id')
        serializer.save(
            author=self.request.user,
            post=Post.objects.get(id=post_id)
        )


class GroupViewSet(mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   viewsets.GenericViewSet):
    """
    Вьюсет для модели Group.

    Разрешён только просмотр списка и деталей групп.
    """

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]
