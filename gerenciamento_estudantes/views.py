from django.http import HttpResponse
from django.shortcuts import render, redirect

def redirect_to_login(request):
    return redirect('/accounts/login')

def test(request):
    return render(request, 'test.html')