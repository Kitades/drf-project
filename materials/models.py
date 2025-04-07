from django.db import models
from django.apps import apps

NULLABLE = {"blank": True, "null": True}


class Course(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название курса")
    image = models.ImageField(
        upload_to="materials/images", verbose_name="Превью", **NULLABLE
    )
    description = models.TextField(verbose_name="Описание курса", **NULLABLE)
    link = models.URLField(verbose_name="url", **NULLABLE)
    owner = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="owner_course",
        verbose_name="Пользователь",
        **NULLABLE
    )

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Lesson(models.Model):
    title = models.CharField(max_length=50, verbose_name="Урок")
    description = models.TextField(verbose_name="Описание урока", **NULLABLE)
    image = models.ImageField(
        upload_to="materials/images", verbose_name="Превью", **NULLABLE
    )
    link = models.URLField(verbose_name="url", **NULLABLE)
    courses = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name="lesson_set", **NULLABLE
    )
    owner = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="owner_lesson",
        verbose_name="Пользователь",
        **NULLABLE
    )

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
