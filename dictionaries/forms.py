from django import forms
from .models import Dictionary
from django.forms import modelformset_factory
from django.forms.widgets import TextInput


DictionaryFormset = modelformset_factory(
    Dictionary,
    fields=["termin_in_rus", "termin_in_eng"],
    extra=5,
    widgets= {
            'termin_in_rus': TextInput(attrs={'class': 'dictionary-termin'}),
            'termin_in_eng': TextInput(attrs={'class': 'dictionary-termin'})
        }
    )
