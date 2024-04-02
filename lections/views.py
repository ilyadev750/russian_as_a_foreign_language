from django.shortcuts import render
from .models import Specialization, Lection
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseNotFound


def get_profile_lections(request, profile):

    try:
        profile = Specialization.objects.get(slug=profile)
    except ObjectDoesNotExist:
        return HttpResponseNotFound("<h1>Page not found</h1>")
    
    lections = Lection.objects.filter(profile_id=profile)
    context = {
        'lections': lections
    }

    return render(request, 'lections/lections_list.html', context)