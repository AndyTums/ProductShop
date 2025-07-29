from rest_framework import serializers

from carts.serializer import CartSerializer
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """ Сериализатор для модели USER """

    cart = CartSerializer(required=False)
    password = serializers.CharField(write_only=True, required=True)
    password2 = serializers.CharField(write_only=True, required=True)

    # Удобный формат времени
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'password2', 'first_name', 'last_name', 'phone', 'country', 'photo', 'created_at',
                  'updated_at', 'cart']

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError('Пароли не совпадают')
        else:
            return attrs

    def create(self, validated_data):
        """ Шифруем пароль """

        password = validated_data.pop('password')
        validated_data.pop('password2')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
