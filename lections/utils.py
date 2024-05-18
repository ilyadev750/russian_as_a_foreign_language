from .models import Lection, Paragraph
from django.utils.safestring import mark_safe
import re


def get_lection_content(lection_slug):

    lection = Lection.objects.get(slug=lection_slug)
    paragraphs = Paragraph.objects.filter(lection_id=lection).order_by('paragraph_number')
    pattern_1 = "(\D1\D\w+\D1\D)"
    pattern_2 = "\D1\D"

    for paragraph in paragraphs:
        paragraph.paragraph = re.sub(pattern_1, '<span id="red">\\1</span>', paragraph.paragraph)
        paragraph.paragraph = re.sub(pattern_2, r'', paragraph.paragraph)
        paragraph.paragraph = mark_safe(paragraph.paragraph)

    return paragraphs