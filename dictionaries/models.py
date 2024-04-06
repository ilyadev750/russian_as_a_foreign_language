from django.db import models
from lections.models import Lection


class Dictionary(models.Model):
    termin_in_rus = models.CharField(max_length=100, verbose_name="Термин на русском")
    termin_in_eng = models.CharField(max_length=100, verbose_name="Термин на английском")
    lection_id = models.ForeignKey(Lection, on_delete=models.CASCADE, verbose_name="Лекция")

    class Meta:
        verbose_name = "словарь"
        verbose_name_plural = "словари"

    def __str__(self) -> str:
        return f'{self.termin_in_rus} - {self.termin_in_eng} - {self.lection_id}'