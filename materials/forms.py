from .models import Image, LectionImage, Audio, LectionAudio
from django import forms
from django.forms import modelformset_factory


class AddImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ["image", "image_name"]
        labels = {
            "image": 'Изображение',
            "image_name": 'Название',
        }


class ImageForm(forms.ModelForm):
    class Meta:
        model = LectionImage
        fields = ["paragraph_id", "image_id"]
        labels = {
            "paragraph_id": "Параграф",
            "image_id": 'Изображение'
        }


AddImageFormset = modelformset_factory(
    model=Image,
    fields=["image", "image_name"],
    extra=3
    )

AddAudioFormset = modelformset_factory(
    model=Audio,
    fields=["audio", "audio_name"],
    extra=3
    )