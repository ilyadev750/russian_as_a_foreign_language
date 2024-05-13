from django.contrib import admin
from django.urls import path, include
from .views import (get_profile_lections,
                    add_lection_content,
                    create_new_lection,
                    get_lection_content,
                    insert_paragraph_in_the_middle,
                    replace_existing_paragraph)

urlpatterns = [
    path('create-new-lection/', create_new_lection, name='create_new_lection'),
    path('<slug:profile_slug>/', get_profile_lections, name='get_profile_lections'),
    path('<slug:lection_slug>/add/', add_lection_content, name='add_lection_content'),
    path('<slug:lection_slug>/1', get_lection_content, name='get_lection_content'),
    path('<slug:lection_slug>/insert/', insert_paragraph_in_the_middle, name='insert_paragraph'),
]
