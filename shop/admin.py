from django.contrib import admin

from shop.models import Category, Product, Subcategory


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """ Функциональность админ панели для модели Category """

    list_display = ('id', 'name', 'slug', 'image')
    list_filter = ('name', 'slug')
    search_fields = ('id', 'name', 'slug')


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    """ Функциональность админ панели для модели Subcategory """

    list_display = ('id', 'name', 'category', 'slug', 'image')
    list_filter = ('name', 'slug', 'category')
    search_fields = ('id', 'name', 'slug', 'category')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """ Функциональность админ панели для модели Product """

    list_display = ('id', 'name', 'price', 'subcategory', 'slug', 'image_small', 'image_medium', 'image_large')
    list_filter = ('name', 'slug', 'price', 'subcategory')
    search_fields = ('id', 'name', 'price', 'slug', 'subcategory')
