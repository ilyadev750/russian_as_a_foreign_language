from django import forms
from .models import Lection, Paragraph


class CreateLection(forms.ModelForm):
    class Meta:
        model = Lection
        fields = ["lection_name", "profile_id", "slug"]
        labels = {
            "lection_name": 'Название лекции',
            "profile_id": 'Профиль',
            "slug": 'URL',
        }


class AddParagraph(forms.ModelForm):
    class Meta:
        model = Paragraph
        fields = ["paragraph", "paragraph_number"]
        labels = {
            "paragraph": 'Абзац',
            "paragraph_number": 'Номер абзаца',
        }