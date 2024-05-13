from django.contrib import admin
from .models import Specialization, Lection, Paragraph

admin.site.register(Specialization)


@admin.register(Lection)
class LectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'lection_name', 'profile_id', 'in_production')


@admin.register(Paragraph)
class ParagraphAdmin(admin.ModelAdmin):
    list_display = ('lection_id', 'paragraph_number')