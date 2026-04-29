from django.db import models


class Blog(models.Model):
    heading = models.CharField(max_length=100, verbose_name="Заголовок:", help_text="Введите наименование заголовка")

    content = models.TextField(verbose_name="Содержимое", blank=True, null=True, help_text="Введите основной текст статьи")

    picture = models.ImageField(upload_to="blogs/", blank=True, null=True, verbose_name="Изображение", help_text="загрузите изображения")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="дата создания")

    publication_attribute = models.BooleanField(default=True, verbose_name="Публикация")

    quantity_views = models.IntegerField(default=0, verbose_name="Количество просмотров", help_text="Количество просмотров")

    class Meta:
        verbose_name = "блог"
        verbose_name_plural = "блоги"
        ordering = ["heading", "content"]

    def __str__(self):
        return self.heading



