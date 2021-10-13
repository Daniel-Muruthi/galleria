from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic import DeleteView
from .models import Image, Location, Category
from django.views.generic import DeleteView
from django.shortcuts import get_object_or_404,render,HttpResponseRedirect
from django.shortcuts import redirect
#My views

def search(request):
    images = Image.show_images()
    if 'search' in request.GET and request.GET["search"]:
        category = request.GET.get('search')
        images=Image.search_image(category)
        return render(request, 'results.html', {"images":images})
    else:
        return render(request, 'index.html', {"images":images})

def home(request):
    images = Image.show_images()
    
    return render(request, 'index.html', {"images":images})
    # if request.method == 'POST':
    #     searchform = request.POST
    #     if categoryquery==Image.category:
    #     else:
    #         return render(request, 'notfound.html')
    # else:
    #     return render(request, 'index.html', {"images":images})

def post_delete(request, id):
    images = Image.show_images()
    delimage= get_object_or_404(Image, pk=id).delete()

    return render(request, 'index.html', {"images":images})



class DeleteImage(DeleteView):
    models=Image
    template_name='delete.html'
    success_url=reverse_lazy('homepage')

    

# def delete_image(request, id):
#     delimage = get_object_or_404(Image, id=id)
#     if request.method =="POST":
#         delimage.delete()
#         return HttpResponseRedirect('homepage')
#     return render(request, 'delete.html')
