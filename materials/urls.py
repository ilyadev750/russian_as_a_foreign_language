from .views import load_images_to_db, load_audio_to_db, add_image_to_paragraph, add_audio_to_paragraph
from django.urls import path


urlpatterns = [
    path('<slug:lection_slug>/load-images-to-db/', load_images_to_db, name='load_images_to_db'),
    path('<slug:lection_slug>/load-audio-to-db/', load_audio_to_db, name='load_audio_to_db'),
    path('<slug:lection_slug>/add-image-to-lection/', add_image_to_paragraph, name='add_image_to_paragraph'),
    path('<slug:lection_slug>/add-audio-to-lection/', add_audio_to_paragraph, name='add_audio_to_paragraph')
]