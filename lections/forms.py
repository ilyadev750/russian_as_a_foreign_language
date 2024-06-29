from django import forms
from .models import Lection, Paragraph, Specialization
from django.forms import modelformset_factory
from django.forms.widgets import TextInput, Select, NumberInput, Textarea


class CreateLectionForm(forms.Form):
    lection_name = forms.CharField(
        max_length=200,
        widget=forms.TextInput(
            attrs={'placeholder': 'Название лекции',
                   'class': 'create-lection-field'}
            )
        )
    profile_id = forms.ModelChoiceField(
        queryset=Specialization.objects.all(),
        empty_label='Профиль',
        widget=forms.Select(
            attrs={'class': 'create-lection-field'}       
            )
        )   
    slug=forms.SlugField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Ссылка',
                   'class': 'create-lection-field'}
            )
        )
        

class AddParagraphForm(forms.ModelForm):
    class Meta:
        model = Paragraph
        fields = ["paragraph"]
        labels = {
            "paragraph": 'Абзац',
        }


class ChangeParagraphForm(forms.ModelForm):
    class Meta:
        model = Paragraph
        fields = ["paragraph"]
        labels = {
            "paragraph": 'Абзац',
        }


AddParagraphFormset = modelformset_factory(
    model=Paragraph,
    fields=["paragraph"],
    extra=3,
    widgets= {
        'paragraph': Textarea(attrs={'class': 'my-textarea', 'placeholder': 'Абзац'}),
    }
    )
