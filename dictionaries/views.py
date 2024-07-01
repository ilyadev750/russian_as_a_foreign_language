from django.shortcuts import render, redirect
from django.utils.safestring import mark_safe
from .models import Dictionary
from django.urls import reverse
from lections.models import Lection
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseNotFound
from .forms import DictionaryFormset


def get_lection_dictionary(request, lection_slug):
    action = request.GET.get('action')
    try:
        lection = Lection.objects.get(slug=lection_slug)
    except ObjectDoesNotExist:
        return HttpResponseNotFound("<h1>Страница не найдена!</h1>")
    
    values = Dictionary.objects.filter(lection_id=lection).order_by('termin_in_rus')

    # red = '(1)STYLESTYleSTYLE(1)(1)STYLESTYleSTYLE(1)(1)STYLESTYleSTYLE(1)'
    # pattern_1 = "(\D1\D\w+\D1\D)"
    # red = re.sub(pattern_1, '<span id="red">\\1</span>', red)
    # red = mark_safe(red)

    context = {
        'values': values,
        'lection': lection,
        # 'red': red,
    }
    return render(request, 'dictionaries/dictionary.html', context)


def get_lection_dictionary_for_delete(request, lection_slug):

    try:
        lection = Lection.objects.get(slug=lection_slug)
    except ObjectDoesNotExist:
        return HttpResponseNotFound("<h1>Страница не найдена!</h1>")
    
    values = Dictionary.objects.filter(lection_id=lection).order_by('termin_in_rus')
    delete_url = reverse('delete_dictionary_item', args=[lection_slug])

    context = {
        'values': values,
        'lection': lection,
        'delete_url': delete_url
    }
    return render(request, 'dictionaries/dictionary_edit.html', context)


def create_new_dictionary(request, lection_slug):

    if request.method == 'POST':
        formset = DictionaryFormset(request.POST)
        if formset.is_valid():
            lection_id = Lection.objects.get(slug=lection_slug)
            for form in formset:
                try:
                    dictionary_obj = Dictionary(
                        termin_in_rus=form.cleaned_data['termin_in_rus'],
                        termin_in_eng=form.cleaned_data['termin_in_eng'],
                        lection_id=lection_id
                    )
                    dictionary_obj.save()
                except KeyError:
                    break
            context = {
                'formset': DictionaryFormset(queryset=Dictionary.objects.none()),
                'lection_slug': lection_slug,
                'success_message': 'Новые термины добавлены!'
            }
            return render(request, 'dictionaries/create_new_dictionary.html', context)

    context = {
        'formset': DictionaryFormset(queryset=Dictionary.objects.none()),
        'lection_slug': lection_slug
    }
    return render(request, 'dictionaries/create_new_dictionary.html', context)


def delete_dictionary_item(request, lection_slug):
    if request.user.is_superuser:
        termin_id = int(request.GET.get('termin_id'))
        dictionary = Dictionary.objects.get(pk=termin_id)
        dictionary.delete()
        return redirect('get_lection_dictionary_for_delete', lection_slug)