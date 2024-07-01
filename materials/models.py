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
    image_id = models.ForeignKey(Image, on_delete=models.CASCADE, verbose_name="Изображение")
    paragraph_id = models.ForeignKey(Paragraph, on_delete=models.CASCADE, verbose_name="Параграф лекции", blank=True, null=True)

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения в лекциях"
        # unique_together = ('lection_id', 'image_id', 'position')

    def __str__(self) -> str:
        return f'{self.image_id} - {self.paragraph_id}'


class LectionAudio(models.Model):
    audio_id = models.ForeignKey(Audio, on_delete=models.CASCADE, verbose_name="Аудиозапись")
    paragraph_id = models.ForeignKey(Paragraph, on_delete=models.CASCADE, verbose_name="Параграф лекции", blank=True, null=True)
    
    class Meta:
        verbose_name = "Аудиозапись"
        verbose_name_plural = "Аудиозаписи в лекциях"
        # unique_together = ('lection_id', 'audio_id', 'position')
        

    def __str__(self) -> str:
        return f'{self.audio_id} - {self.paragraph_id}'
