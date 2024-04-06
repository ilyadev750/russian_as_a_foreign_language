from django.shortcuts import render
from .models import Specialization, Lection
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseNotFound


def get_profile_lections(request, profile_slug):

    try:
        profile_slug = Specialization.objects.get(slug=profile_slug)
    except ObjectDoesNotExist:
        return HttpResponseNotFound("<h1>Page not found</h1>")
    
    lections = Lection.objects.filter(profile_id=profile_slug)
    context = {
        'lections': lections
    }

    return render(request, 'lections/lections_list.html', context)


def get_lection_content(request, slug, page):
    pass