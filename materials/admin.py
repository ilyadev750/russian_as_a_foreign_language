from django.contrib import admin
from .models import LectionAudio, LectionImage, Audio, Image


admin.site.register(Audio)
admin.site.register(Image)
admin.site.register(LectionImage)
admin.site.register(LectionAudio)