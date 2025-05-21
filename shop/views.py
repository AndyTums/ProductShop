from rest_framework import viewsets
from .models import Category, Subcategory, Product
from .serializer import CategorySerializer, SubcategorySerializer, ProductSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """ VIEWSET для модели CATEGORY """

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'


class SubcategoryViewSet(viewsets.ModelViewSet):
    """ VIEWSET для модели SUBCATEGORY """

    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer
    lookup_field = 'slug'


class ProductViewSet(viewsets.ModelViewSet):
    """ VIEWSET для модели PRODUCT """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'slug'
