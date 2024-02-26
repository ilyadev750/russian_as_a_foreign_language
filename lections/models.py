from django.db import models


class Specialization(models.Model):
    specialization_name = models.CharField(
        max_length=100, unique=True, verbose_name="Специальность"
    )

    class Meta:
        verbose_name = "специальность"
        verbose_name_plural = "специальности"


class Lection(models.Model):
    lection_name = models.CharField(
        max_length=50, unique=True, verbose_name="Название лекции"
    )
    category_id = models.ForeignKey(
        Specialization, on_delete=models.CASCADE, verbose_name="Специальность"
    )
    slug = models.SlugField(max_length=50, unique=True, verbose_name="URL")

    class Meta:
        verbose_name = "лекция"
        verbose_name_plural = "лекции"


class Content(models.Model):
    lection_id = models.ForeignKey(
        Lection, on_delete=models.CASCADE, verbose_name="Лекция"
    )
    string_content = models.CharField(max_length=400, verbose_name="Абзац")
    italic_words = models.CharField(max_length=100, verbose_name="Курсивные слова")
    uppercase_words = models.CharField(max_length=100, verbose_name="Слова с заглавными буквами")
    
    class Meta:
        verbose_name = "Контент лекции"
        verbose_name_plural = "Контент лекций"
