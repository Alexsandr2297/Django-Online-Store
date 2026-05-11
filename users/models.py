from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="Email")

    phone_number = models.CharField(max_length=15, blank=True, null=True, help_text="Введите номер телефона")
    avatar = models.ImageField(upload_to='avatars/', verbose_name="Аватар", blank=True, null=True, help_text="Загрузите аватар")
    country = models.CharField(max_length=30, blank=True, null=True, help_text="Введите страну")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email