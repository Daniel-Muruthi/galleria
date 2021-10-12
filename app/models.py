from django.db import models
import datetime as dt

from django.db.models.deletion import CASCADE

# Create your models here.

class Location(models.Model):
    location=models.CharField(max_length=30)

    def __str__(self):
        return self.location

class Category(models.Model):
    category=models.CharField(max_length=30)

class Image(models.Model):
    image = models.ImageField()
    image_name = models.CharField(max_length = 60)
    description = models.TextField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()
    
    def update_image(self, image_name):
        self.objects.filter(image_name=image_name).update()

    def get_image_by_id(self, id):
        self.objects.filter(id=id)

    def search_image(self,category):
        self.objects.filter(category=category)

    def filter_by_location(self,location):
        self.objects.filter(location=location)

