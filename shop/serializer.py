from rest_framework import serializers
from .models import Category, Subcategory, Product


class ProductSerializer(serializers.ModelSerializer):
    """ Сериализатор для модели PRODUCT """

    subcategory = serializers.CharField(
        source='subcategory.name', read_only=True
    )
    category = serializers.CharField(
        source='subcategory.category.name', read_only=True
    )

    class Meta:
        model = Product
        fields = ('name', 'price', 'category', 'subcategory', 'slug', 'image_small', 'image_medium', 'image_large')


class SubcategorySerializer(serializers.ModelSerializer):
    """ Сериализатор для модели SUBCATEGORY """

    class Meta:
        model = Subcategory
        fields = ('name', 'slug', 'image')


class CategorySerializer(serializers.ModelSerializer):
    """ Сериализатор для модели CATEGORY """

    subcategories = SubcategorySerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ('name', 'slug', 'image', 'subcategories')
