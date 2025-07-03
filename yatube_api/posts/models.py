from django.contrib.auth import get_user_model
from django.db import models

from posts.constants import STR_LENGTH

User = get_user_model()


class Group(models.Model):
    title = models.CharField(
        'Название группы',
        max_length=200
    )
    slug = models.SlugField(
        'Идентификатор',
        unique=True
    )
    description = models.TextField(
        'Описание'
    )

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField(
        'Текст поста'
    )
    pub_date = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True
    )
    author = models.ForeignKey(
        User,
        verbose_name='Автор',
        on_delete=models.CASCADE,
        related_name='posts'
    )
    image = models.ImageField(
        'Изображение',
        upload_to='posts/',
        null=True,
        blank=True
    )
    group = models.ForeignKey(
        Group,
        verbose_name='Группа',
        on_delete=models.SET_NULL,
        related_name='group_posts',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.text[:STR_LENGTH]


class Comment(models.Model):
    author = models.ForeignKey(
        User,
        verbose_name='Автор',
        on_delete=models.CASCADE,
        related_name='comments'
    )
    post = models.ForeignKey(
        Post,
        verbose_name='Пост',
        on_delete=models.CASCADE,
        related_name='post_comments'
    )
    text = models.TextField(
        'Текст комментария'
    )
    created = models.DateTimeField(
        'Дата добавления',
        auto_now_add=True,
        db_index=True
    )

    def __str__(self):
        return (
            f'Комментарий от {self.author} '
            f'к посту: "{self.post.text[:STR_LENGTH]}" — '
            f'{self.text[:STR_LENGTH]}'
        )
