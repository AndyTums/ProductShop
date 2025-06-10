from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from shop.models import Product
from .models import Cart, CartItem
from .serializer import CartSerializer, CartItemSerializer


class CartViewSet(viewsets.ModelViewSet):
    """ VIEWSET для модели CART """

    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        # Возвращаем корзину текущего пользователя
        return Cart.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Создаем корзину для текущего пользователя, если еще нет
        serializer.save(user=self.request.user)


class CartItemViewSet(viewsets.ModelViewSet):
    """ VIEWSET для модели CARTITEM """

    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        # Фильтруем по корзине текущего пользователя
        return super().get_queryset().filter(cart__user=self.request.user)

    def perform_create(self, serializer):
        # Получаем или создаем корзину пользователя
        cart, created = Cart.objects.get_or_create(user=self.request.user)

        # Исходя из полученного запроса получаем данные о продукте и кол-ве
        product_id = self.request.data.get('product')
        quantity = self.request.data.get('quantity', 1)

        # Получаем продукт
        product = Product.objects.get(id=product_id)

        # Проверяем есть ли уже такой товар в корзине, если нет то создаем
        cart_item, created = CartItem.objects.get_or_create(
            cart=cart,
            product=product,
            defaults={'quantity': quantity}
        )

        if not created:
            # Товар уже есть — увеличиваем количество
            cart_item.quantity += quantity
            cart_item.save()

        # Вернем сериалоизатор
        serializer.instance = cart_item

    @action(detail=False, methods=['delete'], permission_classes=[IsAuthenticated])
    def clear(self, request):
        """ Метод удаления товаров с корзины """

        # Получаем корзину текущего пользователя
        cart = Cart.objects.get(user=request.user)
        # Удаляем все элементы этой корзины
        deleted_count, _ = CartItem.objects.filter(cart=cart).delete()

        return Response(
            {"detail": f"Товары из корзины удалены. Удалено товаров: {deleted_count}."},
            status=status.HTTP_204_NO_CONTENT
        )
