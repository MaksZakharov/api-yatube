from django.contrib import admin

from posts.models import Comment, Group, Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Настройки отображения модели Post в админке."""
    list_display = ('pk', 'text', 'pub_date', 'author')
    search_fields = ('text',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    """Настройки отображения модели Group в админке."""


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """Настройки отображения модели Comment в админке."""
