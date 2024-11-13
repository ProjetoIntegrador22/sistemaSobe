from django.contrib import admin
from gerenciamento_estudantes.models import Escola, AdminEscola, Professores, Alunos, Responsavel, Turmas, Materias, Avaliacoes, Notas, Frequencia

# Register your models here.

admin.site.register(Escola)
admin.site.register(AdminEscola)
admin.site.register(Professores)
admin.site.register(Alunos)
admin.site.register(Responsavel)
admin.site.register(Turmas)
admin.site.register(Materias)
admin.site.register(Avaliacoes)
admin.site.register(Notas)
admin.site.register(Frequencia)