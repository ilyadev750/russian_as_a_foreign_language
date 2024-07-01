import re
from django.urls import reverse, NoReverseMatch
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from django.http import HttpResponseNotFound
from .utils import get_lection_content as get_content
from .forms import CreateLectionForm, AddParagraphForm, AddParagraphFormset, ChangeParagraphForm
from .models import Specialization, Lection, Paragraph, AdminLectionAction
from materials.models import LectionAudio, LectionImage
from django.shortcuts import render, redirect
from django.utils.safestring import mark_safe
from django.db.models import Q


def create_new_lection(request):

    if request.method == 'POST':
        form = CreateLectionForm(request.POST)

        if form.is_valid():
            lection = Lection()
            lection.lection_name = form.cleaned_data["lection_name"]
            lection.profile_id = form.cleaned_data["profile_id"]
            lection.slug = form.cleaned_data["slug"]
            lection.save()
            request.session['slug'] = lection.slug
            return redirect('create_new_dictionary', lection_slug=lection.slug)

    form = CreateLectionForm()
    context = {
        'form': form
    }
    return render(request, 'lections/create_new_lection.html', context)


def get_all_exist_lections(request):
    all_lections = {}
    specializations = list(Specialization.objects.all())
    for profile in specializations:
        profile_lections = Lection.objects.filter(profile_id=profile)
        all_lections[profile.specialization_name] = []
        for lection in profile_lections:
            lection_info = {}
            lection_info['obj'] = lection
            lection_info['edit_url'] = reverse('open_lection_editor', args=[lection.slug])
            all_lections[profile.specialization_name].append(lection_info)
    context = {
        'specializations': specializations,
        'all_lections': all_lections,
    }

    return render(request, 'lections/get_all_lections.html', context)


def lection_editor_menu(request, lection_slug):
    actions = AdminLectionAction.objects.all().order_by('number')
    action_urls = {}
    for action in actions:

        try:
            action_urls[action.action_name] = reverse(action.url, args=[lection_slug])
        except NoReverseMatch:
            print('Try to reverse without args!')

    context = {
        'actions': action_urls
    }
    return render(request, 'lections/lection_editor_menu.html', context=context)


def add_lection_content(request, lection_slug):

    lection = Lection.objects.get(slug=lection_slug)
    exist_lection_content = Paragraph.objects.filter(lection_id=lection).order_by('-paragraph_number')
    if list(exist_lection_content):
        number_of_last_paragraph = exist_lection_content[0].paragraph_number
    else:
        number_of_last_paragraph = 0

    if request.method == 'POST':
        formset = AddParagraphFormset(request.POST)
        if formset.is_valid():
            lection = Lection.objects.get(slug=lection_slug)

            if 'return' in request.POST:
                return redirect('open_lection_editor', lection_slug=lection.slug)

            for form in formset:
                try:
                    paragraph = Paragraph()
                    paragraph.lection_id = lection
                    paragraph.paragraph = form.cleaned_data['paragraph']
                    number_of_last_paragraph += 1
                    paragraph.paragraph_number = number_of_last_paragraph
                    paragraph.save()
                except KeyError:
                    break
            return redirect('add_lection_content', lection_slug=lection.slug)
        
    
    formset = AddParagraphFormset(queryset=Paragraph.objects.none())
    context = {
        'formset': formset,
        'lection_slug': lection_slug,
    }
    return render(request, 'lections/add_paragraph.html', context)


def insert_paragraph_in_the_middle(request, lection_slug):
    if request.method == 'POST':
        if 'return' in request.POST:
            return redirect('open_lection_editor', lection_slug)
        form = AddParagraphForm(request.POST)
        if form.is_valid():

            lection = Lection.objects.get(slug=lection_slug)
            paragraph_number = int(request.GET.get('paragraph_number'))

            new_paragraph = Paragraph()
            new_paragraph.lection_id = lection
            new_paragraph.paragraph_number = paragraph_number
            new_paragraph.paragraph = form.cleaned_data["paragraph"]
            new_paragraph.save()
            return redirect('get_lection_content_insert_paragraph', lection_slug)
    
        if 'return' in request.POST:
            return redirect('open_lection_editor', lection_slug)

    form = AddParagraphForm()
    context = {
        'form': form,
        'lection_slug': lection_slug,
    }
    return render(request, 'lections/add_paragraph_in_middle.html', context)


def get_profile_lections(request, profile_slug):
    # add pagination
    try:
        profile = Specialization.objects.get(slug=profile_slug)
    except ObjectDoesNotExist:
        return HttpResponseNotFound("<h1>Page not found</h1>")

    lections = Lection.objects.filter(profile_id=profile)
    context = {
        'profile': profile.specialization_name,
        'lections': lections
    }

    return render(request, 'lections/lections_list.html', context)


def get_lection_content(request, lection_slug):

    result = get_content(lection_slug=lection_slug)
    context = {
        'content': result[0],
        'lection_name': result[1],
        'lection_slug': lection_slug,
    }

    return render(request, 'lections/lection_content.html', context)


def get_lection_content_for_changing(request, lection_slug):

    result = get_content(lection_slug=lection_slug)
    replace_url = reverse('replace_content', args=[lection_slug])
    image_url = reverse('add_image_to_paragraph', args=[lection_slug])
    audio_url = reverse('add_audio_to_paragraph', args=[lection_slug])

    context = {
        'replace_url': replace_url,
        'content': result[0],
        'lection_name': result[1],
        'image_url': image_url,
        'audio_url': audio_url,
        'lection_slug': lection_slug,
    }

    return render(request, 'lections/lection_content_change.html', context)

def get_lection_content_insert_paragraph(request, lection_slug):

    result = get_content(lection_slug=lection_slug)
    insert_url = reverse('insert_paragraph_in_the_middle', args=[lection_slug])

    context = {
        'content': result[0],
        'insert_url': insert_url,
        'lection_slug': lection_slug,
        'lection_name': result[1],
    }


    return render(request, 'lections/lection_content_insert_paragraph.html', context)


def get_lection_content_for_deleting(request, lection_slug):

    result = get_content(lection_slug=lection_slug)
    delete_image_url = reverse('delete_image_from_paragraph', args=[lection_slug])
    delete_audio_url = reverse('delete_audio_from_paragraph', args=[lection_slug])
    delete_paragraph_url = reverse('delete_paragraph_from_lection', args=[lection_slug])

    context = {
        'content': result[0],
        'delete_image_url': delete_image_url,
        'delete_audio_url': delete_audio_url,
        'delete_paragraph_url': delete_paragraph_url,
        'lection_slug': lection_slug,
    }

    return render(request, 'lections/lection_content_delete.html', context)


def replace_content(request, lection_slug):
    paragraph_number = int(request.GET.get('paragraph_number'))
    lection = Lection.objects.get(slug=lection_slug)
    if request.method == 'POST':
        form = ChangeParagraphForm(request.POST)
        
        if form.is_valid():
            changed_paragraph = Paragraph.objects.get(lection_id=lection, paragraph_number=paragraph_number)
            changed_paragraph.lection_id = lection
            changed_paragraph.paragraph = form.cleaned_data['paragraph']
            changed_paragraph.save()
            return redirect('get_lection_content_for_changing', lection_slug=lection.slug)

    form = ChangeParagraphForm(instance=Paragraph.objects.get(lection_id=lection, paragraph_number=paragraph_number))
    context = {
        'form': form,
        'lection_slug': lection_slug,
    }
    return render(request, 'lections/replace_paragraph.html', context)


def delete_paragraph_from_lection(request, lection_slug):
    paragraph_number = int(request.GET.get('paragraph_number'))
    lection = Lection.objects.get(slug=lection_slug)
    paragraph = Paragraph.objects.get(lection_id=lection, paragraph_number=paragraph_number)
    paragraph.delete()

    return redirect('get_lection_content_for_deleting', lection_slug=lection.slug)


def delete_lection(request):
    pass


# добавить абзац с картинками и аудиозаписями
# добавить картинки к абзацу
# добавить аудиозаписи к абзацу
# добавить новый абзац
