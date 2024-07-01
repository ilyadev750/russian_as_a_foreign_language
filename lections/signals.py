from django.dispatch import receiver
from .models import Lection, Paragraph
from django.db.models.signals import post_delete, pre_save
from django.db.models import Q


@receiver(post_delete, sender=Paragraph)
def delete_paragraph_update_numbers(sender, instance, *args, **kwargs):
    number = 1
    lection = instance.lection_id
    paragraphs = Paragraph.objects.filter(lection_id=lection).order_by('paragraph_number')
    for paragraph in paragraphs:
        paragraph.paragraph_number = number
        paragraph.save()
        number += 1


@receiver(pre_save, sender=Paragraph)
def add_paragraph_update_numbers(sender, instance, *args, **kwargs):
    number = instance.paragraph_number
    lection = instance.lection_id

    paragraphs = Paragraph.objects.filter(
                Q(lection_id=lection) &
                Q(paragraph_number__gte=number))
    
    for paragraph in paragraphs:
        paragraph.paragraph_number += 1
        paragraph.save()

