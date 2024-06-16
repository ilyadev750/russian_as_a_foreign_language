from django.contrib import admin
from django.urls import path, include
from rki import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
    path("__debug__/", include("debug_toolbar.urls")),
    path("", include('users.urls')),
    path("", include('main.urls')),
    path("lections/", include('lections.urls')),
    path("", include('dictionaries.urls')),
    path("materials/", include('materials.urls')),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)