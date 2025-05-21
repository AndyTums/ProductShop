from django.db import models
from autoslug import AutoSlugField
from transliterate import translit
from django.utils.text import slugify


def transliterate_name(instance):
    """Транслитерируем русский текст в латиницу и создаём slug"""

    name = instance.name  # Получаем название категории
    transliterated = translit(name, 'ru', reversed=True)
    return slugify(transliterated)


class Category(models.Model):
    """Модель: Категории"""

    name = models.CharField(
        max_length=150, verbose_name="Название категории"
    )
    slug = AutoSlugField(
        populate_from=transliterate_name, unique=True, verbose_name="Slug"
    )
    image = models.ImageField(
        upload_to='categories/images/', verbose_name="Изображение"
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    """Модель: Подкатегории"""

    name = models.CharField(
        max_length=150, verbose_name="Название подкатегории"
    )
    slug = AutoSlugField(
        populate_from=transliterate_name, unique=True, verbose_name="Slug"
    )
    image = models.ImageField(
        upload_to='subcategories/images/', verbose_name="Изображение"
    )
    category = models.ForeignKey(
        Category, related_name='subcategories', on_delete=models.CASCADE, verbose_name="Родительская категория"
    )

    class Meta:
        verbose_name = "Подкатегория"
        verbose_name_plural = "Подкатегории"

    def __str__(self):
        return self.name


class Product(models.Model):
    """Модель: Продукта"""

    name = models.CharField(
        max_length=255, verbose_name="Наименование продукта"
    )
    slug = AutoSlugField(
        populate_from=transliterate_name, unique=True, verbose_name="Slug"
    )
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Цена"
    )
    subcategory = models.ForeignKey(
        Subcategory, related_name='products', on_delete=models.CASCADE, verbose_name="Категория"
    )

    # Изображений в 3-х размерах
    image_small = models.ImageField(
        upload_to='products/images/small/', verbose_name="Изображение малого размера"
    )
    image_medium = models.ImageField(
        upload_to='products/images/medium/', verbose_name="Изображение среднего размера"
    )
    image_large = models.ImageField(
        upload_to='products/images/large/', verbose_name="Изображение большого размера"
    )

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return self.name
