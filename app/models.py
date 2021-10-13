from django.db import models
import datetime as dt
from django.urls import reverse
from django.db.models.deletion import CASCADE
from django.shortcuts import get_object_or_404,render,HttpResponseRedirect
from cloudinary.models import CloudinaryField

# Create your models here.

class Location(models.Model):
    location=models.CharField(max_length=30)

    def __str__(self):
        return self.location

class Category(models.Model):
    category=models.CharField(max_length=30)

    def __str__(self):
        return self.category

class Image(models.Model):
    image = CloudinaryField('image')
    image_name = models.CharField(max_length = 60)
    description = models.TextField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)
    pub_date = models.DateTimeField(auto_now_add=True)

    def save_image(self):
        return self.save()

    def delete_image(self):
        return self.delete()
    
    def update_image(self, image_name):
        return self.objects.filter(image_name=image_name).update()

    def get_image_by_id(self, id):
        return self.objects.filter(id=id)
    @classmethod
    def search_image(cls,category):
        categoriesfound=cls.objects.filter(category__name__icontains=category)
        return categoriesfound

    def filter_by_location(self,location):
        return self.objects.filter(location=location)

    @classmethod
    def show_images(cls):
        images = cls.objects.all()
        return images

    def after_delete():
        return reverse('homepage')

