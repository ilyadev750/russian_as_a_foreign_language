from django.apps import AppConfig


class LectionsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'lections'
    verbose_name = 'Лекции'

    def ready(self):
        import lections.signals