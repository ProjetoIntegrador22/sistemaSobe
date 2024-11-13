from django.db.models.signals import post_save, pre_save
from django.contrib.auth.models import Group, User
from gerenciamento_estudantes.models import Escola

def cria_alerta(sender, instance, created=True, **kwargs):
    if instance.pk is None:
        print('Escola adicionada com sucesso!')
    else:
        print('Escola Atualizada')   

pre_save.connect(cria_alerta, sender=Escola)