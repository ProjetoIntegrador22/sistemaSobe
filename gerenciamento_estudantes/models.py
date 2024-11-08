from django.db import models

# Create your models here.

class Admin(models.Model):
    id=models.AutoField(primary_key=True)
    nome=models.CharField(max_length=255)
    email=models.EmailField(unique=True)
    senha=models.CharField(max_length=255)
    criado_em=models.DateTimeField(auto_now_add=True)
    atualizado_em=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

class Funcionarios(models.Model):
    id=models.AutoField(primary_key=True)
    nome=models.CharField(max_length=255)
    email=models.EmailField(unique=True)
    senha=models.CharField(max_length=255)
    endereco=models.TextField()
    criado_em=models.DateTimeField(auto_now_add=True)
    atualizado_em=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()


class Cursos(models.Model):
    id=models.AutoField(primary_key=True)
    nome_curso=models.CharField(max_length=255)
    criado_em=models.DateTimeField(auto_now_add=True)
    atualizado_em=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

class Materias(models.Model):
    id=models.AutoField(primary_key=True)
    nome_materia=models.CharField(max_length=255)
    curso_id=models.ForeignKey(Cursos, on_delete=models.CASCADE)
    funcionario_id=models.ForeignKey(Funcionarios, on_delete=models.CASCADE)
    criado_em=models.DateTimeField(auto_now_add=True)
    atualizado_em=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()


class Estudantes(models.Model):
    id=models.AutoField(primary_key=True)
    nome=models.CharField(max_length=255)
    responsavel=models.CharField(max_length=255)
    email=models.EmailField(unique=True)
    senha=models.CharField(max_length=255)
    genero=models.CharField(max_length=255)
    foto_perfil=models.FileField()
    endereco=models.TextField()
    curso_id=models.ForeignKey(Cursos, on_delete=models.DO_NOTHING)
    criado_em=models.DateTimeField(auto_now_add=True)
    atualizado_em=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

class Frequencia(models.Model):
    id=models.AutoField(primary_key=True)
    materia_id=models.ForeignKey(Materias, on_delete=models.DO_NOTHING)
    fequencia_data=models.DateTimeField(auto_now_add=True)
    curso_id=models.ForeignKey(Cursos, on_delete=models.DO_NOTHING)
    criado_em=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

class RelatorioFrequencia(models.Model):
    id=models.AutoField(primary_key=True)
    estudante_id=models.ForeignKey(Estudantes, on_delete=models.DO_NOTHING)
    frequencia_id=models.ForeignKey(Frequencia, on_delete=models.CASCADE)
    status=models.BooleanField(default=False)
    criado_em=models.DateTimeField(auto_now_add=True)
    atualizado_em=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

class RelatorioAusenciaEstudante(models.Model):
    id=models.AutoField(primary_key=True)
    estudante_id=models.ForeignKey(Estudantes, on_delete=models.CASCADE)
    ausencia_data=models.CharField(max_length=255)
    ausencia_mensagem=models.TextField()
    ausencia_status=models.BooleanField(default=False)
    criado_em=models.DateTimeField(auto_now_add=True)
    atualizado_em=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

class RelatorioAusenciaFuncionario(models.Model):
    id=models.AutoField(primary_key=True)
    funcionario_id=models.ForeignKey(Funcionarios, on_delete=models.CASCADE)
    ausencia_data=models.CharField(max_length=255)
    ausencia_mensagem=models.TextField()
    ausencia_status=models.BooleanField(default=False)
    criado_em=models.DateTimeField(auto_now_add=True)
    atualizado_em=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

class FeedbackEstudante(models.Model):
    id=models.AutoField(primary_key=True)
    estudante_id=models.ForeignKey(Estudantes, on_delete=models.CASCADE)
    feedback=models.TextField()
    feedback_resposta=models.TextField()
    criado_em=models.DateTimeField(auto_now_add=True)
    atualizado_em=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

class FeedbackFuncionario(models.Model):
    id=models.AutoField(primary_key=True)
    funcionario_id=models.ForeignKey(Funcionarios, on_delete=models.CASCADE)
    feedback=models.TextField()
    feedback_resposta=models.TextField()
    criado_em=models.DateTimeField(auto_now_add=True)
    atualizado_em=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

class NotificacoesEstudante(models.Model):
    id=models.AutoField(primary_key=True)
    estudante_id=models.ForeignKey(Estudantes, on_delete=models.CASCADE)
    mensagem=models.TextField()
    criado_em=models.DateTimeField(auto_now_add=True)
    atualizado_em=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

class NotificacoesFuncionario(models.Model):
    id=models.AutoField(primary_key=True)
    funcionario_id=models.ForeignKey(Funcionarios, on_delete=models.CASCADE)
    mensagem=models.TextField()
    criado_em=models.DateTimeField(auto_now_add=True)
    atualizado_em=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()




