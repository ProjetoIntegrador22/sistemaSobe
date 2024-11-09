from django.http import HttpResponse
from django.shortcuts import render

def LoginPage(request):
    return render(request, 'login_page.html')