from django.http import HttpResponse
from django.shortcuts import render, redirect

def redirect_to_login(request):
    return redirect('/accounts/login')

def profile(request):
    return render(request, 'profile.html')

def contato(request):
    return render(request, 'contato.html')

def sobre(request):
    return render(request, 'sobre.html')

def test(request):
    if request.user.groups.filter(name='admin').exists():
        # User is an admin
        context = {'is_admin': True}
    else:
        # User is not an admin
        context = {'is_admin': False}
    return render(request, 'my_template.html', context)
