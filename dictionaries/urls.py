from django.contrib import admin
from django.urls import path
from .views import (get_lection_dictionary,
                    create_new_dictionary,
                    delete_dictionary_item,
                    get_lection_dictionary_for_delete)

urlpatterns = [
    path('<slug:lection_slug>/create-dictionary/',
          create_new_dictionary,
          name='create_new_dictionary'),
    path('<slug:lection_slug>/dictionary/',
         get_lection_dictionary,
         name='get_lection_dictionary'),
     path('<slug:lection_slug>/dictionary-edit/',
         get_lection_dictionary_for_delete,
         name='get_lection_dictionary_for_delete'),
    path('<slug:lection_slug>/dictionary/delete/',
         delete_dictionary_item,
         name='delete_dictionary_item')

]
