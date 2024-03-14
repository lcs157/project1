from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request,'recipes/home.html', context={
        'name': 'Lucas'
    })

def about(request):
    return render(request, 'temp/temp.html')

def contact(request):
    return HttpResponse('contact')

# Create your views here.
