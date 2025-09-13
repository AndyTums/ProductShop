from django.contrib import admin

from carts.models import Cart, CartItem


class CartItemInline(admin.TabularInline):
    """ Настройка модели CATRITEM и формируем для удобства в одну позицию CART """

    model = CartItem
    extra = 1
    fields = ('id', 'product', 'quantity', 'price')
    readonly_fields = ('id',)


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    """ Админка для модели Cart с отображением товаров внутри """

    list_display = ('id', 'user', 'quantity', 'total', 'created_at', 'updated_at')
    list_filter = ('user',)
    search_fields = ('id', 'user__username')
    inlines = [CartItemInline]

    def quantity(self, obj):
        """ Вывод кол-во товара  """

        total_quantity = sum(item.quantity for item in obj.items.all())
        return total_quantity

    quantity.short_description = 'Количество'
