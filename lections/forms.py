from django import forms
from .models import Lection


class CreateLection(forms.ModelForm):
    class Meta:
        model = Lection
        fields = ["lection_name", "profile_id", "slug"]
        labels = {
            "lection_name": 'Название лекции',
            "profile_id": 'Профиль',
            "slug": 'URL',
        }


class AddParagraph(forms.Form):
    paragraph = forms.TextInput()
    paragraph_number = forms.IntegerField()