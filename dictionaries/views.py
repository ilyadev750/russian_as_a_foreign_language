from django.shortcuts import render, redirect
from django.utils.safestring import mark_safe
from .models import Dictionary
from django.urls import reverse
from lections.models import Lection
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseNotFound
from .forms import DictionaryFormset



def get_lection_dictionary(request, lection_slug):

    try:
        lection = Lection.objects.get(slug=lection_slug)
    except ObjectDoesNotExist:
        return HttpResponseNotFound("<h1>Page not found</h1>")
    
    values = Dictionary.objects.filter(lection_id=lection)

    # red = '(1)STYLESTYleSTYLE(1)(1)STYLESTYleSTYLE(1)(1)STYLESTYleSTYLE(1)'
    # pattern_1 = "(\D1\D\w+\D1\D)"
    # red = re.sub(pattern_1, '<span id="red">\\1</span>', red)
    # red = mark_safe(red)
    if request.user.is_superuser:
        delete_dict_item_url = reverse('delete_dictionary_item', args=[lection_slug])
    else:
        delete_dict_item_url = ''
    context = {
        'values': values,
        'lection': lection,
        'delete_dict_item_url': delete_dict_item_url,
        # 'red': red,
    }
    
    return render(request, 'dictionaries/dictionary.html', context)


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
            return redirect('home')
    context = {
        'formset': DictionaryFormset(queryset=Dictionary.objects.none())
    }
    return render(request, 'dictionaries/create_new_dictionary.html', context)


def delete_dictionary_item(request, lection_slug):
    if request.user.is_superuser:
        pk = request.GET.get('pk')
        dictionary = Dictionary.objects.get(pk=int(pk))
        dictionary.delete()
        return redirect('get_lection_dictionary', lection_slug)