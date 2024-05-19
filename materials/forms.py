from .models import Image, LectionImage
from django import forms


class AddImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ["image", "image_name"]
        labels = {
            "image": 'Изображение',
            "image_name": 'Название',
        }


class ChooseImageForm(forms.ModelForm):
    class Meta:
        model = LectionImage
        fields = ["image_id"]
        labels = {
            "image": 'Изображение'
        }
