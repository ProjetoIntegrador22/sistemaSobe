from django.http import HttpResponse
from django.shortcuts import render, redirect

def redirect_to_login(request):
    return redirect('/accounts/login')

def test(request):
    return render(request, 'test.html')

def profile(request):
    return render(request, 'profile.html')

def contato(request):
    return render(request, 'contato.html')

def sobre(request):
    return render(request, 'sobre.html')