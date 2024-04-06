from django.contrib import admin
from django.urls import path, include
from .views import get_profile_lections, get_lection_content

urlpatterns = [
    path('<slug:profile_slug>/', get_profile_lections, name='get_profile_lections'),
    path('<slug:slug>/<int:page>/', get_lection_content, name='get_lection_content'),
]
