from django.contrib.auth.models import AbstractUser
from django.db import models

from materials.models import Course, Lesson

NULLABLE = {'null': True, 'blank': True}


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='Почта')
    phone = models.CharField(max_length=30, verbose_name='Телефон', **NULLABLE)
    avatar = models.ImageField(upload_to='users/avatars', verbose_name='Аватар', **NULLABLE)
    city = models.CharField(max_length=50, verbose_name='Город', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Payments(models.Model):
    CASH_PAY = 'наличные'
    CASHLESS_PAY = 'безналичный'
    PAYMENT_CHOICES = (
        (CASH_PAY, 'наличные'),
        (CASHLESS_PAY, 'безналичный'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='payments', verbose_name='Пользователь')
    date_payment = models.DateTimeField(verbose_name='дата оплаты', **NULLABLE)
    amount = models.PositiveIntegerField(verbose_name='Сумма оплаты')
    payment_type = models.CharField(max_length=11, default=CASHLESS_PAY, choices=PAYMENT_CHOICES)
    payment_course = models.ForeignKey(Course, related_name='course', on_delete=models.CASCADE,
                                       verbose_name='оплаченный курс')
    payment_lesson = models.ForeignKey(Lesson, related_name='lessons', on_delete=models.CASCADE,
                                       verbose_name='оплаченный урок')
