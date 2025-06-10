from rest_framework import serializers

from shop.models import Product
from .models import Cart, CartItem


class CartItemSerializer(serializers.ModelSerializer):
    """ Сериализатор для модели CARTITEM """

    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = CartItem
        fields = ['id', 'product', 'quantity', 'price', 'subtotal', 'created_at', 'updated_at']
        read_only_fields = ['price', 'subtotal', 'created_at', 'updated_at']


class CartSerializer(serializers.ModelSerializer):
    """ Сериализатор для модели CART """

    items = CartItemSerializer(many=True, read_only=True)
    total = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = Cart
        fields = ['id', 'user', 'items', 'total', 'created_at', 'updated_at']
        read_only_fields = ['user', 'created_at', 'updated_at']
