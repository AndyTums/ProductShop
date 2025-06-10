from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

from config import settings
from .apps import CartsConfig
from .views import CartViewSet, CartItemViewSet

app_name = CartsConfig.name

router = DefaultRouter()
router.register('items', CartItemViewSet)
router.register('', CartViewSet)

urlpatterns = []

urlpatterns += router.urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
