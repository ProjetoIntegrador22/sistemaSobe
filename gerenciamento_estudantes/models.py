from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Escola(models.Model):
    nome = models.CharField(max_length=150)
    inep = models.CharField(max_length=150)
    endereco = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    telefone = models.CharField(max_length=150)
    usuario = models.OneToOneField(User, on_delete=models.DO_NOTHING, default='', blank=True, null=True)

    def __str__(self):
        return self.nome + ' | ' + str(self.inep)

class AdminEscola(models.Model):
    nome = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    telefone = models.CharField(max_length=150)
    cpf = models.CharField(max_length=150)
    escola = models.ForeignKey(Escola, on_delete=models.DO_NOTHING)
    usuario = models.OneToOneField(User, on_delete=models.DO_NOTHING, default='', blank=True, null=True)

    def __str__(self):
        return self.nome

class Professores(models.Model):
    nome = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    telefone = models.CharField(max_length=150)
    cpf = models.CharField(max_length=150)
    escola = models.ForeignKey(Escola, on_delete=models.DO_NOTHING)
    usuario = models.OneToOneField(User, on_delete=models.DO_NOTHING, default='', blank=True, null=True)

    def __str__(self):
        return self.nome

class Turmas(models.Model):
    nome = models.CharField(max_length=150)
    data = models.DateField(blank=True, null=True)
    data_final = models.DateField(blank=True, null=True)
    escola = models.ForeignKey(Escola, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.nome

class Responsavel(models.Model):
    nome = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    telefone = models.CharField(max_length=150)
    cpf = models.CharField(max_length=150)

    def __str__(self):
        return self.nome + ' | ' + str(self.cpf)

class Alunos(models.Model):
    nome = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    telefone = models.CharField(max_length=150)
    rg = models.CharField(max_length=150)
    ra = models.CharField(max_length=150)
    responsavel = models.OneToOneField(Responsavel, on_delete=models.DO_NOTHING, default='', blank=True, null=True)
    escola = models.ForeignKey(Escola, on_delete=models.DO_NOTHING)
    turma = models.ForeignKey(Turmas, on_delete=models.DO_NOTHING, default='', blank=True, null=True)
    usuario = models.OneToOneField(User, on_delete=models.DO_NOTHING, default='', blank=True, null=True)

    def __str__(self):
        return self.nome + ' | ' + str(self.ra)

class Materias(models.Model):
    nome = models.CharField(max_length=150)
    turma = models.ManyToManyField(Turmas, related_name='materias')
    professores = models.ManyToManyField(Professores, related_name='materias')
    
    def __str__(self):
        return self.nome

class Avaliacoes(models.Model):
    nome = models.CharField(max_length=150)
    nota_max = models.DecimalField(max_digits=6, decimal_places=4)
    data = models.DateField(blank=True, null=True)
    materia = models.ForeignKey(Materias, on_delete=models.DO_NOTHING)
    professor = models.ForeignKey(Professores, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.nome + ' | ' + str(self.materia)

class Notas(models.Model):
    aluno = models.ForeignKey(Alunos, on_delete=models.DO_NOTHING)
    avaliacao = models.ForeignKey(Avaliacoes, on_delete=models.DO_NOTHING)
    data = models.DateField(blank=True, null=True)
    nota = models.DecimalField(max_digits=6, decimal_places=4)

    def __str__(self):
        return self.avaliacao + ' | ' + str(self.nota)

class Frequencia(models.Model):
    aluno = models.ForeignKey(Alunos, on_delete=models.DO_NOTHING)
    data = models.DateField()
    presenca = models.BooleanField(default=False)
    justificativa = models.TextField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.data + ' | ' + str(self.presenca)

















