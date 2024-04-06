from django.shortcuts import render
from .models import Dictionary
from lections.models import Lection
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseNotFound


def get_lection_dictionary(request, lection_slug):

    try:
        lection = Lection.objects.get(slug=lection_slug)
    except ObjectDoesNotExist:
        return HttpResponseNotFound("<h1>Page not found</h1>")
    
    values = Dictionary.objects.filter(lection_id=lection)

    context = {
        'values': values,
        'lection': lection,
        'red': '<span id="red">Красный</span>'
    }
    
    return render(request, 'dictionaries/dictionary.html', context)