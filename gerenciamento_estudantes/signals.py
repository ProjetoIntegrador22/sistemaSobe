from django.db.models.signals import post_save, pre_save
from django.contrib.auth.models import Group, User
from gerenciamento_estudantes.models import Escola, AdminEscola, Professores, Alunos

# Exemplo de teste simples

""" def cria_alerta(sender, instance, created=True, **kwargs):
    if instance.pk is None:
        print('Escola adicionada com sucesso!')
    else:
        print('Escola Atualizada!')   

post_save.connect(cria_alerta, sender=Escola) """

#Cria primeiro Usuário Admin da escola e o adiciona ao grupo 'Administraco Escola'

def criar_admin_grupo_escola(sender, instance, created=True, **kwargs):
        if instance.pk is None:  # Check if it's a new instance
            user = User.objects.create_user(
                username=instance.inep,
                email=instance.email,
                password=instance.inep,
            )
            instance.usuario = user

            # Assign the user to the 'student' group
            grupo_admin = Group.objects.get_or_create(name='Administracao Escola')[0]
            user.groups.add(grupo_admin)
            print('Usuário criado e adicionado ao grupo Administração Escola')
        
        else:
            print('Escola Atualizada!')

pre_save.connect(criar_admin_grupo_escola, sender=Escola)

#Cria novo Usuário: Admin e o adiciona ao grupo 'Administraco Escola'

def criar_admin(sender, instance, created=True, **kwargs):
        if instance.pk is None:  # Check if it's a new instance
            user = User.objects.create_user(
                username=instance.email,
                email=instance.email,
                password=instance.cpf,
            )
            instance.usuario = user

            # Assign the user to the 'student' group
            grupo_admin = Group.objects.get_or_create(name='Administracao Escola')[0]
            user.groups.add(grupo_admin)
            print('Usuário criado e adicionado ao grupo Administração Escola')
        
        else:
            print('Admin Atualizado(a)!')

pre_save.connect(criar_admin, sender=AdminEscola)

#Cria novo Usuário: Professor e o adiciona ao grupo 'Professores'

def criar_professor(sender, instance, created=True, **kwargs):
        if instance.pk is None:  # Check if it's a new instance
            user = User.objects.create_user(
                username=instance.email,
                email=instance.email,
                password=instance.cpf,
            )
            instance.usuario = user

            # Assign the user to the 'student' group
            grupo_professor = Group.objects.get_or_create(name='Professores')[0]
            user.groups.add(grupo_professor)
            print('Usuário criado e adicionado ao grupo Professores')
        
        else:
            print('Professor Atualizado(a)!')

pre_save.connect(criar_professor, sender=Professores)

#Cria novo Usuário: Aluno e o adiciona ao grupo 'Alunos'

def criar_aluno(sender, instance, created=True, **kwargs):
        if instance.pk is None:  # Check if it's a new instance
            user = User.objects.create_user(
                username=instance.email,
                email=instance.email,
                password=instance.ra,
            )
            instance.usuario = user

            # Assign the user to the 'student' group
            grupo_alunos = Group.objects.get_or_create(name='Alunos')[0]
            user.groups.add(grupo_alunos)
            print('Usuário criado e adicionado ao grupo Alunos')
        
        else:
            print('Aluno Atualizado(a)!')

pre_save.connect(criar_aluno, sender=Alunos)

# testadmin@test.com 41585865232
# professor@test.com 41585151523
# aluno@test.com 3545689