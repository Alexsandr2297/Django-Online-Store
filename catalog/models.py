from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=100, verbose_name="Наименование категории", help_text="Введите наименование категории"
    )
    description = models.TextField(
        verbose_name="Описание категории", blank=True, null=True, help_text="Введите описание категории"
    )

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(
        max_length=100, verbose_name="Наименование продукта", help_text="Введите наименование продукта"
    )
    description = models.TextField(
        verbose_name="Описание продукта", blank=True, null=True, help_text="Введите описание продукта"
    )
    picture = models.ImageField(
        upload_to="products/", blank=True, null=True, verbose_name="Изображение", help_text="загрузите изображения"
    )
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, related_name="products", verbose_name="категория",  blank=True, null=True
    )
    price = models.IntegerField(
        blank=True, null=True, verbose_name="цена за покупку", help_text="Введите цену за покупку"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="дата последнего изменения")

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        ordering = ["name", "description"]

    def __str__(self):
        return self.name
