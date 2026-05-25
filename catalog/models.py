from django.db import models
from django.conf import settings


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
    name = models.CharField(max_length=100, verbose_name="Наименование продукта")
    description = models.TextField(verbose_name="Описание продукта", blank=True, null=True)
    picture = models.ImageField(upload_to="products/", blank=True, null=True, verbose_name="Изображение")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name="products", verbose_name="категория",
                                 blank=True, null=True)
    price = models.IntegerField(blank=True, null=True, verbose_name="цена за покупку")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="дата последнего изменения")
    published_status = models.BooleanField(default=False, verbose_name="Публикация")
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Владелец")

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        ordering = ["name", "description"]
        permissions = [
            ("can_unpublish_product", "Can unpublish product"),
        ]

    def __str__(self):
        return self.name
