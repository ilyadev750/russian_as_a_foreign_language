from django import forms
from .models import Dictionary
from django.forms import modelformset_factory


DictionaryFormset = modelformset_factory(Dictionary,
                                         fields=["termin_in_rus", "termin_in_eng"],
                                         extra=5)
