from django.shortcuts import render # type: ignore
from django.http import HttpResponse # type: ignore

def index(request):
    return render(request, 'firstpage/firstpage.html')

def about(request):
    return render(request, 'firstpage/about.html')