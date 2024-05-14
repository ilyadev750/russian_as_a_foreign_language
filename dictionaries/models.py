from django.db import models
from lections.models import Lection


class Dictionary(models.Model):
    termin_in_rus = models.CharField(max_length=100, verbose_name="Термин на русском")
    termin_in_eng = models.CharField(max_length=100, verbose_name="Термин на английском")
    lection_id = models.ForeignKey(Lection, on_delete=models.CASCADE, verbose_name="Лекция")

    class Meta:
        verbose_name = "словарь"
        verbose_name_plural = "словари"
        unique_together = ('termin_in_rus', 'termin_in_eng', 'lection_id')

    def __str__(self) -> str:
        return f'{self.termin_in_rus} - {self.termin_in_eng} - {self.lection_id}'


class AdminDictionaryAction(models.Model):
    action_name = models.CharField(
        max_length=100, unique=True, verbose_name="Действие"
    )
    number = models.IntegerField(
        verbose_name="Номер действия", default=0
    )
    url = models.CharField(
        max_length=50, verbose_name="Ссылка", default='#'
    )

    class Meta:
        verbose_name = "Действие со словарем"
        verbose_name_plural = "Действия со словарями"

    def __str__(self) -> str:
        return f'{self.action_name}'