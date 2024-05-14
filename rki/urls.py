from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("__debug__/", include("debug_toolbar.urls")),
    path("", include('users.urls')),
    path("", include('main.urls')),
    path("lections/", include('lections.urls')),
    path("", include('dictionaries.urls')),
]
