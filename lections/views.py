import re
from django.shortcuts import render
from .models import Specialization, Lection
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseNotFound
from .forms import CreateLection, AddParagraph
from .models import Specialization, Lection, Paragraph
from django.shortcuts import render, redirect
from django.utils.safestring import mark_safe


def create_new_lection(request):

    if request.method == 'POST':
        form = CreateLection(request.POST)

        if form.is_valid():
            lection = Lection()
            lection.lection_name = form.cleaned_data["lection_name"]
            lection.profile_id = form.cleaned_data["profile_id"]
            lection.slug = form.cleaned_data["slug"]
            lection.save()
            return redirect('add_lection_content', lection_slug=lection.slug)
        
    form = CreateLection()
    context = {
        'form': form
    }
    return render(request, 'lections/create_new_lection.html', context)


def add_lection_content(request, lection_slug):
    
    if request.method == 'POST':
        form = AddParagraph(request.POST)

        if form.is_valid():
            lection = Lection.objects.get(slug=lection_slug)
            paragraph = Paragraph()
            paragraph.lection_id = lection
            paragraph.paragraph = form.cleaned_data['paragraph']
            paragraph.paragraph_number = form.cleaned_data['paragraph_number']
            paragraph.save()
            return redirect('add_lection_content', lection_slug=lection.slug)
    
    form = AddParagraph()
    context = {
        'form': form,
        'lection_slug': lection_slug,
    }
    return render(request, 'lections/add_paragraph.html', context)


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


def get_lection_content(request, lection_slug):

    lection = Lection.objects.get(slug=lection_slug)
    paragraphs = Paragraph.objects.filter(lection_id=lection).order_by('paragraph_number')
    pattern_1 = "(\D1\D\w+\D1\D)"
    pattern_2 = "\D1\D"
    
    for paragraph in paragraphs:
        paragraph.paragraph = re.sub(pattern_1, '<span id="red">\\1</span>', paragraph.paragraph)
        paragraph.paragraph = re.sub(pattern_2, r'', paragraph.paragraph)
        paragraph.paragraph = mark_safe(paragraph.paragraph)
    
    context = {
        'paragraphs': paragraphs
    }

    return render(request, 'lections/lection_content.html', context)


# добавить картинки к абзацу
# добавить аудиозаписи к абзацу