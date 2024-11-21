from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название курса")
    image = models.ImageField(upload_to='materials/images', verbose_name='Превью', blank=True, null=True)
    description = models.TextField(verbose_name="Описание курса")

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Lesson(models.Model):
    title = models.CharField(max_length=50, verbose_name='Урок')
    description = models.TextField(verbose_name='Описание урока')
    image = models.ImageField(upload_to='materials/images', verbose_name='Превью', blank=True, null=True)
    slug = models.SlugField(verbose_name='url')
    lesson = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons')

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
