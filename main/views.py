from django.shortcuts import render
from lections.models import Specialization

def index(request):
    profiles = Specialization.objects.all()
    context = {
        "profiles": profiles
    }
    return render(request, "main/index.html")