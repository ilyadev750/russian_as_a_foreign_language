from .models import Image, LectionImage, Audio, LectionAudio
from django import forms
from django.forms import modelformset_factory
from django.forms.widgets import TextInput, FileInput, Select


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
        widgets = { 
            'image_id': Select(attrs={'class': 'create-lection-field'})
        }


class LectionAudioForm(forms.ModelForm):
    class Meta:
        model = LectionAudio
        fields = ["audio_id"]
        labels = {
            "audio_id": "Аудиозапись"
        }
        widgets = { 
            'audio_id': Select(attrs={'class': 'create-lection-field'})
        }


AddImageFormsetDb = modelformset_factory(
    model=Image,
    fields=["image", "image_name"],
    extra=3,
    widgets= {
                'image': FileInput(attrs={'id': 'image-audio-form'}),
                "image_name": TextInput(attrs={'id': 'image-audio-div', 'placeholder': 'Название изображения'})
            }
    )

AddAudioFormsetDb = modelformset_factory(
    model=Audio,
    fields=["audio", "audio_name"],
    extra=3,
    widgets= {
                'audio': FileInput(attrs={'id': 'image-audio-form'}),
                "audio_name": TextInput(attrs={'id': 'image-audio-div', 'placeholder': 'Название аудиозаписи'})
            }
    )