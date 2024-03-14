from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('HOME 1')

def about(request):
    return HttpResponse('About')

def contact(request):
    return HttpResponse('contact')

# Create your views here.
