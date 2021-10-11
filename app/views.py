from django.shortcuts import render
from django.http import HttpResponse

#My views

def welcome(request):
    return HttpResponse('This is my first django app')
