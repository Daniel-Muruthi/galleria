from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DeleteView
from .models import Image, Location, Category
from django.views.generic import DeleteView
from django.shortcuts import (get_object_or_404,render,HttpResponseRedirect)
#My views

def home(request):
    images = Image.show_images()
    return render(request, 'index.html', {"images":images})

# class DeleteImage(DeleteView):
#     models=Image
#     template_name='delete.html'

    

# def delete_image(request, id):
#     delimage = get_object_or_404(Image, id=id)
#     if request.method =="POST":
#         delimage.delete()
#         return HttpResponseRedirect('homepage')
#     return render(request, 'delete.html')
