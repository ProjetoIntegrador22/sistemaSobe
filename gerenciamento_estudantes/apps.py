from django.apps import AppConfig


class GerenciamentoEstudantesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'gerenciamento_estudantes'

    def ready(self):
        import gerenciamento_estudantes.signals
