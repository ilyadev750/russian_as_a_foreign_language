from django.shortcuts import render
from .forms import AddImageForm, ChooseImageForm
from .models import Image, LectionImage
from lections.models import Paragraph, Lection


def add_image(request, lection_slug):
    paragraph_number = int(request.GET.get('paragraph_number'))
    lection = Lection.objects.get(slug=lection_slug)
    paragraph = Paragraph.objects.get(lection_id=lection, paragraph_number=paragraph_number)

    if request.method == 'POST':
        if 'add_image' in request.POST:
            form = AddImageForm(request.POST)

            if form.is_valid():

                new_image = Image()
                new_image.image = form.cleaned_data['image']
                new_image.image_name = form.cleaned_data['image_name']
                new_image.save()

                image_paragraph = LectionImage()
                image_paragraph.paragraph_id = paragraph
                image_paragraph.image_id = new_image
                image_paragraph.save()

                


def add_audio(request):
    pass


def delete_image(request):
    pass


def delete_audio(request):
    pass

