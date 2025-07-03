from django.urls import include, path, re_path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from api.views import GroupViewSet, CommentViewSet, PostViewSet

v1_router = DefaultRouter()
v1_router.register('posts', PostViewSet, basename='post')
v1_router.register('groups', GroupViewSet, basename='group')

# группируем v1-эндпоинты
v1_patterns = [
    path('', include(v1_router.urls)),
    path('api-token-auth/', views.obtain_auth_token),
    re_path(
        r'^posts/(?P<post_id>\d+)/comments/$',
        CommentViewSet.as_view({'get': 'list', 'post': 'create'}),
        name='comment-list',
    ),
    re_path(
        r'^posts/(?P<post_id>\d+)/comments/(?P<pk>\d+)/$',
        CommentViewSet.as_view({
            'get': 'retrieve',
            'put': 'update',
            'patch': 'partial_update',
            'delete': 'destroy',
        }),
        name='comment-detail',
    ),
]

urlpatterns = [
    path('v1/', include(v1_patterns)),
]
