from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

from config import settings
from .apps import ShopConfig
from .views import CategoryViewSet, SubcategoryViewSet, ProductViewSet

app_name = ShopConfig.name

router = DefaultRouter()
router.register('categories', CategoryViewSet)
router.register('subcategories', SubcategoryViewSet)
router.register('products', ProductViewSet)

urlpatterns = []

urlpatterns += router.urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
