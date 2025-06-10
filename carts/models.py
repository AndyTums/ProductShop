from django.db import models

from shop.models import Product
from users.models import User


class Cart(models.Model):
    """ Модель: Корзина пользователя """

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='cart', verbose_name="Пользователь"
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата создания"
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Дата последнего обновления"
    )

    class Meta:
        verbose_name = "Корзина"
        verbose_name_plural = "Корзины"

    @property
    def total(self):
        """ Вывода общей стоимости """

        return sum(item.subtotal for item in self.items.all())

    def __str__(self):
        return f"Корзина пользователя {self.user.email}"


class CartItem(models.Model):
    """ Модель: Товар в корзине """

    cart = models.ForeignKey(
        Cart, on_delete=models.CASCADE, related_name='items', verbose_name="Корзина"
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, verbose_name="Товар в корзине"
    )
    quantity = models.PositiveIntegerField(
        default=1, verbose_name="Количество"
    )
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Цена"
    )  # Фиксированная цена

    class Meta:
        verbose_name = "Товар в корзине"
        verbose_name_plural = "Товары в корзине"

    @property
    def subtotal(self):
        """ Подсчет общей суммы по продуктам """

        return self.price * self.quantity

    def save(self, *args, **kwargs):
        self.price = self.product.price
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.quantity} × {self.product.name}"
