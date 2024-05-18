from django.contrib import admin
from django.urls import path, include
from materials.views import (add_image,
                             add_audio,
                             delete_image,
                             delete_audio)
from .views import (get_profile_lections,
                    add_lection_content,
                    create_new_lection,
                    lection_editor_menu,
                    get_lection_content,
                    get_lection_content_for_changing,
                    get_lection_content_for_deleting,
                    insert_paragraph_in_the_middle,
                    replace_content,
                    delete_lection,
                    delete_paragraph)

urlpatterns = [
    path('create-new-lection/', create_new_lection, name='create_new_lection'),
    path('<slug:profile_slug>/', get_profile_lections, name='get_profile_lections'),
    path('<slug:lection_slug>/content/', get_lection_content, name='get_lection_content'),
    path('<slug:lection_slug>/content-change/', get_lection_content_for_changing, name='get_lection_content_for_changing'),
    path('<slug:lection_slug>/content-delete/', get_lection_content_for_deleting, name='get_lection_content_for_deleting'),
    path('<slug:lection_slug>/editor/', lection_editor_menu, name='open_lection_editor'),
    path('<slug:lection_slug>/add/', add_lection_content, name='add_lection_content'),
    path('<slug:lection_slug>/insert/', insert_paragraph_in_the_middle, name='insert_paragraph_in_the_middle'),
    path('<slug:lection_slug>/replace/', replace_content, name='replace_content'),
    path('<slug:lection_slug>/add_image/', add_image, name='add_image'),          
    path('<slug:lection_slug>/add_audio/', add_audio, name='add_audio'),    
    path('<slug:lection_slug>/delete_image/', delete_image, name='delete_image'),  
    path('<slug:lection_slug>/delete_audio/', delete_audio, name='delete_audio'),
    path('<slug:lection_slug>/delete_paragraph/', delete_paragraph, name='delete_paragraph'),
    path('<slug:lection_slug>/delete_lection/', delete_lection, name='delete_lection'), 
]
