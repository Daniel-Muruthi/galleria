from django.contrib import admin
from .models import Image, Location, Category
from django.contrib.admin import AdminSite
# Register your models here.

class ImageAdmin(admin.ModelAdmin):
    filter_horizontal =('category',)

admin.site.register(Location)
admin.site.register(Image, ImageAdmin)
admin.site.register(Category)
admin.site.index_template='index.html'

