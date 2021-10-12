from django.shortcuts import render
from django.http import HttpResponse
from .models import Image, Location, Category
#My views

def home(request):
    return render(request, 'index.html')
