from django.db import models
from lections.models import Paragraph


class Image(models.Model):
    image = models.ImageField(upload_to='media/lection_images', verbose_name='Изображение')
    image_name = models.CharField(max_length=200, verbose_name='Название')

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"

    def __str__(self) -> str:
        return f'{self.image.name}'


class Audio(models.Model):
    audio = models.FileField(upload_to='media/lection_audio', verbose_name='Аудиозапись')
    audio_name = models.CharField(max_length=200, verbose_name='Название')

    class Meta:
        verbose_name = "Аудиозапись"
        verbose_name_plural = "Аудиозаписи"

    def __str__(self) -> str:
        return f'{self.audio.name}'


class LectionImage(models.Model):
    paragraph_id = models.ForeignKey(Paragraph, on_delete=models.CASCADE, verbose_name="Параграф")  
    image_id = models.ForeignKey(Image, on_delete=models.CASCADE, verbose_name="Изображение")

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"

    def __str__(self) -> str:
        return f'{self.paragraph_id} - {self.image_name}'
    

class LectionAudio(models.Model):
    paragraph_id = models.ForeignKey(Paragraph, on_delete=models.CASCADE, verbose_name="Параграф")  
    audio_id = models.ForeignKey(Audio, on_delete=models.CASCADE, verbose_name="Аудиозапись")

    class Meta:
        verbose_name = "Аудиозапись"
        verbose_name_plural = "Аудиозаписи"

    def __str__(self) -> str:
        return f'{self.paragraph_id} - {self.audio_name}'
