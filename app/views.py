from django.shortcuts import render
from django.http import HttpResponse

#My views

def welcome(request):
    return render(request, 'base.html')

def home(request):
    return render(request, 'index.html')
