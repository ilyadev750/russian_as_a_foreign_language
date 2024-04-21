from django import forms
from .models import Dictionary
from django.forms import modelformset_factory


# class CreateDictionaryForm(forms.ModelForm):
#     class Meta:
#         model = Dictionary
#         fields = ["termin_in_rus", "termin_in_eng"]
#         labels = {
#             "paragraph": 'Абзац',
#             "paragraph_number": 'Номер абзаца',
#         }

DictionaryFormset = modelformset_factory(Dictionary,
                                         fields=["termin_in_rus", "termin_in_eng", "lection_id"],
                                         extra=5)
