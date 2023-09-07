from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

from .views import RoleViewSet, TaskViewSet


router = DefaultRouter()
router.register(r"role", RoleViewSet)
router.register(r"", TaskViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)