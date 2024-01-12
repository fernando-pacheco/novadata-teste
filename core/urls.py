from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from apps.api.views import PostViewSet, CommentViewSet

router = routers.DefaultRouter()
router.register('posts', PostViewSet, basename='Post')
router.register('comments', CommentViewSet, basename='Comment')

urlpatterns = [
    path('area-restrita/', admin.site.urls),
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('app/', include('apps.app.urls')),
    path('users/', include('apps.users.urls')),
    path('api/', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
