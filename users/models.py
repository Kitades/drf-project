from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='Почта')
    phone = models.CharField(max_length=30, verbose_name='Телефон', null=True, blank=True)
    avatar = models.ImageField(upload_to='users/avatars', verbose_name='Аватар', null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True, verbose_name='Город')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
