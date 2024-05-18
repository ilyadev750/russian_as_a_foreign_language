import re
from django.urls import reverse
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseNotFound
from .utils import get_lection_content as get_content
from .forms import CreateLectionForm, AddParagraphForm, AddParagraphFormset, ChangeParagraphForm
from .models import Specialization, Lection, Paragraph, AdminLectionAction
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


def lection_editor_menu(request, lection_slug):
    actions = AdminLectionAction.objects.all().order_by('number')
    action_urls = {}
    for action in actions:
        action_urls[action.action_name] = reverse(action.url, args=[lection_slug])
    context = {
        'actions': action_urls
    }
    return render(request, 'lections/lection_editor_menu.html', context=context)


def add_lection_content(request, lection_slug):

    if request.method == 'POST':
        formset = AddParagraphFormset(request.POST)
        if formset.is_valid():
            lection = Lection.objects.get(slug=lection_slug)
            for form in formset:
                try:
                    paragraph = Paragraph()
                    paragraph.lection_id = lection
                    paragraph.paragraph = form.cleaned_data['paragraph']
                    paragraph.paragraph_number = form.cleaned_data['paragraph_number']
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
        form = AddParagraphForm(request.POST)
        if form.is_valid():
            lection = Lection.objects.get(slug=lection_slug)
            paragraph_number = form.cleaned_data['paragraph_number']
            lection_paragraphs = Paragraph.objects.filter(
                Q(lection_id=lection) &
                Q(paragraph_number__gte=paragraph_number))
            for paragraph in lection_paragraphs:
                paragraph.paragraph_number += 1
                paragraph.save()

            new_paragraph = Paragraph()
            new_paragraph.lection_id = lection
            new_paragraph.paragraph = form.cleaned_data['paragraph']
            new_paragraph.paragraph_number = form.cleaned_data['paragraph_number']
            new_paragraph.save()
            return redirect('open_lection_editor', lection_slug=lection.slug)

    form = AddParagraphForm()
    context = {
        'form': form,
        'lection_slug': lection_slug,
    }
    return render(request, 'lections/add_paragraph_in_middle.html', context)


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

    paragraphs = get_content(lection_slug=lection_slug)
    context = {
        'paragraphs': paragraphs
    }

    return render(request, 'lections/lection_content.html', context)


def get_lection_content_for_changing(request, lection_slug):

    paragraphs = get_content(lection_slug=lection_slug)
    replace_url = reverse('replace_content', args=[lection_slug])
    context = {
        'replace_url': replace_url,
        'paragraphs': paragraphs
    }

    return render(request, 'lections/lection_content_change.html', context)


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


def get_lection_content_for_deleting(request, lection_slug):
    pass

def delete_paragraph(request):
    pass

def delete_lection(request):
    pass


# добавить абзац с картинками и аудиозаписями
# добавить картинки к абзацу
# добавить аудиозаписи к абзацу
# добавить новый абзац
