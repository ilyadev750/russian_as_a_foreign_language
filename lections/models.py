from django.db import models


class Specialization(models.Model):
    specialization_name = models.CharField(
        max_length=100, unique=True, verbose_name="Профиль"
    )
    slug = models.SlugField(max_length=50, verbose_name="URL", default='slug')
    
    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"

    def __str__(self) -> str:
        return f'{self.specialization_name}'


class Lection(models.Model):
    lection_name = models.CharField(
        max_length=50, unique=True, verbose_name="Название лекции"
    )
    profile_id = models.ForeignKey(
        Specialization, on_delete=models.CASCADE, verbose_name="Профиль", default=None
    )
    slug = models.SlugField(max_length=50, unique=True, verbose_name="URL")

    class Meta:
        verbose_name = "лекция"
        verbose_name_plural = "лекции"

    def __str__(self) -> str:
        return f'{self.lection_name}'


class Content(models.Model):
    lection_id = models.ForeignKey(
        Lection, on_delete=models.CASCADE, verbose_name="Лекция"
    )
    content = models.CharField(max_length=400, verbose_name="Абзац")
    content_number = models.IntegerField(verbose_name="Номер абзаца", default=None)
    
    class Meta:
        verbose_name = "Контент лекции"
        verbose_name_plural = "Контент лекций"

    def __str__(self) -> str:
        return f'{self.content_number}'

    
