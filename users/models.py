from django.contrib.auth.models import AbstractUser
from django.db import models

from materials.models import Course, Lesson

NULLABLE = {"null": True, "blank": True}


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name="Почта")
    phone = models.CharField(max_length=30, verbose_name="Телефон", **NULLABLE)
    avatar = models.ImageField(
        upload_to="users/avatars", verbose_name="Аватар", **NULLABLE
    )
    city = models.CharField(max_length=50, verbose_name="Город", **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Payments(models.Model):
    CASH_PAY = "наличные"
    CASHLESS_PAY = "безналичный"
    PAYMENT_CHOICES = (
        (CASH_PAY, "наличные"),
        (CASHLESS_PAY, "безналичный"),
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="payments",
        verbose_name="Пользователь",
    )
    date_payment = models.DateTimeField(verbose_name="дата оплаты", **NULLABLE)
    amount = models.PositiveIntegerField(verbose_name="Сумма оплаты")
    payment_type = models.CharField(
        max_length=11, default=CASHLESS_PAY, choices=PAYMENT_CHOICES, **NULLABLE
    )
    payment_course = models.ForeignKey(
        Course,
        related_name="course",
        on_delete=models.CASCADE,
        verbose_name="оплаченный курс",
        **NULLABLE
    )
    payment_lesson = models.ForeignKey(
        Lesson,
        related_name="lessons",
        on_delete=models.CASCADE,
        verbose_name="оплаченный урок",
        **NULLABLE
    )


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="user_follow",
        verbose_name="Пользователь",
        **NULLABLE
    )
    courses = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="follow_courses",
        verbose_name="курс",
        **NULLABLE
    )

    class Meta:
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"


class Donation(models.Model):
    amount = models.PositiveIntegerField(
        verbose_name="Сумма пожертвования", help_text="Сумма пожертвования"
    )
    session_id = models.CharField(max_length=255, verbose_name="Id сессии", **NULLABLE)
    link = models.URLField(max_length=400, verbose_name="Ccылка на оплату", **NULLABLE)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Пользователь", **NULLABLE
    )

    class Meta:
        verbose_name = "Пожертвования"
        verbose_name_plural = "Пожертвования"

    def __str__(self):
        return self.amount
