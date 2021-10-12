from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
# from .views import DeleteImage
from . import views

urlpatterns=[
    url(r'^$', views.home, name='homepage'),
    # url(r'^delete/', DeleteImage.as_view(), name="delete")

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)