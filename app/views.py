from django.shortcuts import render
from django.http import HttpResponse
from .models import Image, Location, Category
#My views

def home(request):
    images = Image.show_images()
    return render(request, 'index.html', {"images":images})
