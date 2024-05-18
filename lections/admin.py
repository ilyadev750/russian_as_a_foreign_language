from django.contrib import admin
from .models import Specialization, Lection, Paragraph, AdminLectionAction

admin.site.register(Specialization)


@admin.register(AdminLectionAction)
class LectionAction(admin.ModelAdmin):
    list_display = ('action_name', 'number')

    def get_ordering(self, request):
        return ['number']


@admin.register(Lection)
class LectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'lection_name', 'profile_id', 'in_production')


@admin.register(Paragraph)
class ParagraphAdmin(admin.ModelAdmin):
    list_display = ('lection_id', 'paragraph_number')

    def get_ordering(self, request):
        return ['lection_id', 'paragraph_number']

        