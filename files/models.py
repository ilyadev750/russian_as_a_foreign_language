from django.db import models
from lections.models import Paragraph


class Image(models.Model):
    image = models.ImageField(upload_to='lection_images', verbose_name='Картинка')
    paragraph_id = models.ForeignKey(
        Paragraph, on_delete=models.CASCADE, verbose_name="ID абзаца лекции"
        )
    
    class Meta:
        verbose_name = "Картинка"
        verbose_name_plural = "Картинки"

    def __str__(self) -> str:
        return f'{self.image.name}'


class Audio(models.Model):
    audio = models.FileField(upload_to='lection_audio', verbose_name='Аудиозапись')
    paragraph_id = models.ForeignKey(
        Paragraph, on_delete=models.CASCADE, verbose_name="ID абзаца лекции"
        )
    
    class Meta:
        verbose_name = "Аудиозапись"
        verbose_name_plural = "Аудиозаписи"

    def __str__(self) -> str:
        return f'{self.audio.name}'