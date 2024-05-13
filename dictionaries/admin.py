from django.contrib import admin
from .models import Dictionary, AdminDictionaryAction


admin.site.register(Dictionary)


@admin.register(AdminDictionaryAction)
class DictionaryAction(admin.ModelAdmin):
    list_display = ('action_name', 'number')

