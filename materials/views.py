from django.shortcuts import render, redirect
from .forms import AddImageForm, ImageForm, AddImageFormset, AddAudioFormset
from .models import Image, LectionImage, Audio
from lections.models import Paragraph, Lection


def load_images_to_db(request, lection_slug):

    if request.method == 'POST':
        formset = AddImageFormset(request.POST, request.FILES)
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
    
    formset = AddImageFormset(queryset=Image.objects.none())
    context = {
        'formset': formset,
        'lection_slug': lection_slug,
    }

    return render(request, 'materials/add_images_in_db.html', context)


def load_audio_to_db(request, lection_slug):

    if request.method == 'POST':
        formset = AddAudioFormset(request.POST, request.FILES)
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
    
    formset = AddAudioFormset(queryset=Audio.objects.none())
    context = {
        'formset': formset,
        'lection_slug': lection_slug,
    }

    return render(request, 'materials/add_audio_in_db.html', context)


def add_image_to_paragraph(request, lection_slug):
    paragraph_number = int(request.GET.get('paragraph_number'))
    lection = Lection.objects.get(slug=lection_slug)
    paragraph = Paragraph.objects.get(lection_id=lection, paragraph_number=paragraph_number)

    if request.method == 'POST':
        pass

    form = ImageForm()
    form.fields["paragraph_id"].queryset = Paragraph.objects.filter(lection_id=lection, paragraph_number=paragraph_number)

    context = {
        'form': form,
        'lection_slug': lection_slug,
    }

    return render(request, 'materials/add_image_in_lection.html', context)
        # if 'add_image' in request.POST:
        #     form = AddImageForm(request.POST)

        #     if form.is_valid():

        #         new_image = Image()
        #         new_image.image = form.cleaned_data['image']
        #         new_image.image_name = form.cleaned_data['image_name']
        #         new_image.save()

        #         image_paragraph = LectionImage()
        #         image_paragraph.paragraph_id = paragraph
        #         image_paragraph.image_id = new_image
        #         image_paragraph.save()


def add_audio(request):
    pass


def delete_image(request):
    pass


def delete_audio(request):
    pass

