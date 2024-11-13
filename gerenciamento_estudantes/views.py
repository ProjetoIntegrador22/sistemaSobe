from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from gerenciamento_estudantes.models import AdminEscola, Alunos, Professores

def redirect_to_login(request):
    return redirect('/accounts/login')

def profile(request, ):
    if request.user.is_superuser:
        context = {'usuario': 'superuser', 'nome': 'Diogo'}
    elif request.user.groups.filter(name='Administracao Escola').exists():
        # Usuário é um admin
        usuario_atual = AdminEscola.objects.get(usuario=request.user)
        context = {'profile': usuario_atual}
    elif request.user.groups.filter(name='Professores').exists():
        # Usuário é um professor
        context = {'usuario': 'professor'}
    else:
        # Usuário é um estudante
        context = {'usuario': 'aluno'}
    return render(request, 'profile.html', context)

def contato(request):
    return render(request, 'contato.html')

def sobre(request):
    return render(request, 'sobre.html')

def test(request):
    if request.user.is_superuser:
        context = {'usuario': 'superuser'}
    elif request.user.groups.filter(name='Administracao Escola').exists():
        # Usuário é um admin
        context = {'usuario': 'admin'}
    elif request.user.groups.filter(name='Professores').exists():
        # Usuário é um professor
        context = {'usuario': 'professor'}
    else:
        # Usuário é um estudante
        context = {'usuario': 'aluno'}
    return render(request, 'test.html', context)


#Class Based views 

class AlunosView(ListView):
    model = Alunos
    template_name = 'lista-alunos.html'

class ProfessoresView(ListView):
    model = Professores
    template_name = 'lista-professores.html'
