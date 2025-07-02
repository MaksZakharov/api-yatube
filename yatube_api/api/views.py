from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from posts.models import Post
from api.serializers import PostSerializer
from api.permissions import IsAuthorOrReadOnly


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
