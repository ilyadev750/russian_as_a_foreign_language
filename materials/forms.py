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


class LectionImageForm(forms.ModelForm):
    class Meta:
        model = LectionImage
        fields = ["image_id"]
        labels = {
            "image_id": "Изображение"
        }


AddImageFormsetDb = modelformset_factory(
    model=Image,
    fields=["image", "image_name"],
    extra=3
    )

AddAudioFormsetDb = modelformset_factory(
    model=Audio,
    fields=["audio", "audio_name"],
    extra=3
    )