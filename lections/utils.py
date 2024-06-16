from .models import Lection, Paragraph
from materials.models import LectionImage
from django.utils.safestring import mark_safe
import re


def get_lection_content(lection_slug):

    content = {}
    content_images = {}

    lection = Lection.objects.get(slug=lection_slug)
    paragraphs = (
        Paragraph.objects.filter(lection_id=lection)
                  .order_by('paragraph_number')
        )
    images = (LectionImage.objects.filter(lection_id=lection)
              .select_related('image_id'))
    pattern_1 = "(\D1\D\w+\D1\D)"
    pattern_2 = "\D1\D"

    for paragraph in paragraphs:
        paragraph.paragraph = re.sub(pattern_1, '<span id="red">\\1</span>', paragraph.paragraph)
        paragraph.paragraph = re.sub(pattern_2, r'', paragraph.paragraph)
        paragraph.paragraph = mark_safe(paragraph.paragraph)
        content[paragraph.paragraph_number] = paragraph.paragraph

    for image in images:
        content_images[image.position] = image

    return content, content_images