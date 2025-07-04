from django.contrib.auth import get_user_model
from rest_framework import serializers

from posts.models import Comment, Group, Post

User = get_user_model()


class PostSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Post.

    Поле author отображается через username.
    """

    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
    )

    class Meta:
        model = Post
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Comment.

    Поле author отображается через username.
    Поле post доступно только для чтения.
    """

    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
    )

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('post',)


class GroupSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Group.
    """

    class Meta:
        model = Group
        fields = '__all__'
