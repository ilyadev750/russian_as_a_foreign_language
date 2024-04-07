from django.shortcuts import render
from django.utils.safestring import mark_safe
from .models import Dictionary
from lections.models import Lection
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseNotFound
import re


def get_lection_dictionary(request, lection_slug):

    try:
        lection = Lection.objects.get(slug=lection_slug)
    except ObjectDoesNotExist:
        return HttpResponseNotFound("<h1>Page not found</h1>")
    
    values = Dictionary.objects.filter(lection_id=lection)

    # red = '(1)STYLESTYleSTYLE(1)(1)STYLESTYleSTYLE(1)(1)STYLESTYleSTYLE(1)'
    # pattern_1 = "\D1\D\w+\D1\D"
    # red = re.sub(pattern_1, '<span class="red">JURASSIC PARK</span>', red)
    # red = mark_safe(red)

    context = {
        'values': values,
        'lection': lection,
        # 'red': red,
    }
    
    return render(request, 'dictionaries/dictionary.html', context)