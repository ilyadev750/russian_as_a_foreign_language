from django.contrib import admin
from django.urls import path
from .views import get_lection_dictionary, create_new_dictionary

urlpatterns = [
    path('<slug:lection_slug>/create-dictionary', create_new_dictionary, name='create_new_dictionary'),
    path('<slug:lection_slug>/dictionary', get_lection_dictionary, name='get_lection_dictionary'),

]
