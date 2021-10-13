from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from .views import DeleteImage
from . import views
from django.urls import path

urlpatterns=[
    path('', views.home, name='homepage'),
    path('search/', views.search, name='searchresults'),
    # path('delete/', DeleteImage.as_view(), name="delete"),
    url(r'^(?P<id>\d+)/delete/$', views.post_delete, name= 'delete'),

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)