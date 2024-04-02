from django.contrib import admin
from django.urls import path, include
from .views import get_profile_lections

urlpatterns = [
    path('<str:profile>/', get_profile_lections, name='get_profile_lections'),
]
