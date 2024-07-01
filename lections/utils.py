from .models import Lection, Paragraph
from materials.models import LectionImage, LectionAudio
from django.utils.safestring import mark_safe
import re


def get_lection_content(lection_slug):

    content = {}
    result = []

    lection = Lection.objects.get(slug=lection_slug)
    paragraphs = (
        Paragraph.objects.filter(lection_id=lection)
                  .order_by('paragraph_number')
        )
    
    images = LectionImage.objects.filter(paragraph_id__in=paragraphs)
    images = images.select_related('paragraph_id').select_related('image_id')

            
    audio = LectionAudio.objects.filter(paragraph_id__in=paragraphs)
    audio = audio.select_related('paragraph_id').select_related('audio_id')


    pattern_1 = "(\D1\D\w+\D1\D)"
    pattern_2 = "\D1\D"

    for paragraph in paragraphs:
        paragraph.paragraph = re.sub(pattern_1, '<span id="red">\\1</span>', paragraph.paragraph)
        paragraph.paragraph = re.sub(pattern_2, r'', paragraph.paragraph)
        paragraph.paragraph = mark_safe(paragraph.paragraph)
        content[paragraph.paragraph_number] = {}
        content[paragraph.paragraph_number]['images'] = []
        content[paragraph.paragraph_number]['audio'] = []
        content[paragraph.paragraph_number]['paragraph'] = paragraph

    
    for image in images:
        content[image.paragraph_id.paragraph_number]['images'].append(image)

    for track in audio:
        content[track.paragraph_id.paragraph_number]['audio'].append(track)

    result.append(content)
    result.append(lection.lection_name)

    return result