from django import forms
from .models import Dictionary


class CreateDictionary(forms.ModelForm):
    class Meta:
        model = Dictionary
        fields = ["termin_in_rus", "termin_in_eng"]
        labels = {
            "paragraph": 'Абзац',
            "paragraph_number": 'Номер абзаца',
        }