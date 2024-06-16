from django.db import models
from lections.models import Lection, Paragraph


class Image(models.Model):
    image = models.ImageField(upload_to='lection_images', verbose_name='Изображение')
    image_name = models.CharField(max_length=200, verbose_name='Название')

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения в базе данных"

    def __str__(self) -> str:
        return f'{self.image_name}'


class Audio(models.Model):
    audio = models.FileField(upload_to='lection_audio', verbose_name='Аудиозапись')
    audio_name = models.CharField(max_length=200, verbose_name='Название')

    class Meta:
        verbose_name = "Аудиозапись"
        verbose_name_plural = "Аудиозаписи в базе данных"

    def __str__(self) -> str:
        return f'{self.audio_name}'


class LectionImage(models.Model):
    lection_id = models.ForeignKey(Lection, on_delete=models.CASCADE, verbose_name="Лекция", blank=True, null=True)  
    image_id = models.ForeignKey(Image, on_delete=models.CASCADE, verbose_name="Изображение")
    position = models.IntegerField(verbose_name="Номер абзаца", default=None)

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения в лекциях"

    def __str__(self) -> str:
        return f'{self.lection_id} - {self.image_id} - {self.position}'


class LectionAudio(models.Model):
    lection_id = models.ForeignKey(Lection, on_delete=models.CASCADE, verbose_name="Лекция", blank=True, null=True)   
    audio_id = models.ForeignKey(Audio, on_delete=models.CASCADE, verbose_name="Аудиозапись")
    position = models.IntegerField(verbose_name="Номер абзаца", default=None)
    
    class Meta:
        verbose_name = "Аудиозапись"
        verbose_name_plural = "Аудиозаписи в лекциях"

    def __str__(self) -> str:
        return f'{self.lection_id} - {self.audio_id} - {self.position}'
