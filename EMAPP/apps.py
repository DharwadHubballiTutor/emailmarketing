from django.apps import AppConfig


class EmappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'EMAPP'

    def ready(self):
        from .tasks import start
        start()
