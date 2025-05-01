from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

from config import settings
from users.apps import UsersConfig

from users.views import UserViewSet

app_name = UsersConfig.name

router = DefaultRouter()
router.register("", UserViewSet, basename="users")

urlpatterns = []

urlpatterns += router.urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
