from django.shortcuts import render, redirect
from .forms import LectionAudioForm, LectionImageForm, AddImageFormsetDb, AddAudioFormsetDb
from .models import Image, LectionImage, Audio, LectionAudio
from lections.models import Paragraph, Lection


def load_images_to_db(request, lection_slug):

    if request.method == 'POST':
        formset = AddImageFormsetDb(request.POST, request.FILES)
        if formset.is_valid():
            for form in formset:
                try:
                    image = Image()
                    image.image_name = form.cleaned_data['image_name']
                    image.image = form.cleaned_data['image']
                    image.save()
                except KeyError:
                    break

            return redirect('load_images_to_db', lection_slug)
    
    formset = AddImageFormsetDb(queryset=Image.objects.none())
    context = {
        'formset': formset,
        'lection_slug': lection_slug,
    }

    return render(request, 'materials/add_images_in_db.html', context)


def load_audio_to_db(request, lection_slug):

    if request.method == 'POST':
        formset = AddAudioFormsetDb(request.POST, request.FILES)
        if formset.is_valid():
            for form in formset:
                try:
                    audio = Audio()
                    audio.audio_name = form.cleaned_data['audio_name']
                    audio.audio = form.cleaned_data['audio']
                    audio.save()
                except KeyError:
                    break

            return redirect('load_audio_to_db', lection_slug)
    
    formset = AddAudioFormsetDb(queryset=Audio.objects.none())
    context = {
        'formset': formset,
        'lection_slug': lection_slug,
    }

    return render(request, 'materials/add_audio_in_db.html', context)


def add_image_to_paragraph(request, lection_slug):
    paragraph_number = int(request.GET.get('paragraph_number'))
    lection = Lection.objects.get(slug=lection_slug)

    if request.method == 'POST':
        form = LectionImageForm(request.POST, request.FILES)
        if form.is_valid():
            paragraph_image = LectionImage()
            paragraph_image.lection_id = lection
            paragraph_image.image_id = form.cleaned_data['image_id']
            paragraph_image.position = paragraph_number
            paragraph_image.save()
            return redirect('get_lection_content_for_changing', lection_slug=lection.slug)

    form = LectionImageForm()

    context = {
        'form': form,
        'lection_slug': lection_slug,
    }

    return render(request, 'materials/add_image_in_lection.html', context)


def add_audio_to_paragraph(request, lection_slug):
    paragraph_number = int(request.GET.get('paragraph_number'))
    lection = Lection.objects.get(slug=lection_slug)

    if request.method == 'POST':
        form = LectionAudioForm(request.POST, request.FILES)
        if form.is_valid():
            paragraph_audio = LectionAudio()
            paragraph_audio.lection_id = lection
            paragraph_audio.audio_id = form.cleaned_data['audio_id']
            paragraph_audio.position = paragraph_number
            paragraph_audio.save()
            return redirect('get_lection_content_for_changing', lection_slug=lection.slug)

    form = LectionAudioForm()

    context = {
        'form': form,
        'lection_slug': lection_slug,
    }

    return render(request, 'materials/add_audio_in_lection.html', context)


def delete_image_from_paragraph(request, lection_slug):
    paragraph_number = int(request.GET.get('paragraph_number'))
    image_id = int(request.GET.get('image_id'))
    lection = Lection.objects.get(slug=lection_slug)

    image = LectionImage.objects.get(lection_id=lection,
                                     position=paragraph_number,
                                     image_id=image_id)
    image.delete()

    return redirect('get_lection_content_for_deleting', lection_slug=lection.slug)


def delete_audio_from_pararaph(request, lection_slug):
    paragraph_number = int(request.GET.get('paragraph_number'))
    audio_id = int(request.GET.get('audio_id'))
    lection = Lection.objects.get(slug=lection_slug)

    audio = LectionAudio.objects.get(lection_id=lection,
                                     position=paragraph_number,
                                     audio_id=audio_id)
    audio.delete()

    return redirect('get_lection_content_for_deleting', lection_slug=lection.slug)


def add_audio(request):
    pass


def delete_image(request):
    pass


def delete_audio(request):
    pass

