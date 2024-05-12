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
        max_length=100, unique=True, verbose_name="Название лекции"
    )
    profile_id = models.ForeignKey(
        Specialization, on_delete=models.CASCADE, verbose_name="Профиль", default=None
    )
    slug = models.SlugField(max_length=50, unique=True, verbose_name="URL")
    in_production = models.BooleanField(default=False, verbose_name='Готовность лекции')

    class Meta:
        verbose_name = "лекция"
        verbose_name_plural = "лекции"

    def __str__(self) -> str:
        return f'{self.lection_name}'


class Paragraph(models.Model):
    lection_id = models.ForeignKey(
        Lection, on_delete=models.CASCADE, verbose_name="Лекция"
    )
    paragraph = models.TextField(max_length=10000, verbose_name="Абзац")
    paragraph_number = models.IntegerField(verbose_name="Номер абзаца", default=None)

    class Meta:
        verbose_name = "Контент лекции"
        verbose_name_plural = "Контент лекций"
        

    def __str__(self) -> str:
        return f'{self.lection_id} - {self.paragraph_number}'


class LectionImage(models.Model):
    paragraph_id = models.ForeignKey(Paragraph, on_delete=models.CASCADE, verbose_name="Параграф")  
    image = models.ImageField(upload_to='media/lection_images', verbose_name='Изображение')
    image_name = models.CharField(max_length=200, verbose_name='Название')

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"

    def __str__(self) -> str:
        return f'{self.paragraph_id} - {self.image_name}'
    

class LectionAudio(models.Model):
    paragraph_id = models.ForeignKey(Paragraph, on_delete=models.CASCADE, verbose_name="Параграф")  
    audio = models.FileField(upload_to='media/lection_audio', verbose_name='Аудиозапись')
    audio_name = models.CharField(max_length=200, verbose_name='Название')

    class Meta:
        verbose_name = "Аудиозапись"
        verbose_name_plural = "Аудиозаписи"

    def __str__(self) -> str:
        return f'{self.paragraph_id} - {self.audio_name}'