from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from . import urls

def index(request):
    return HttpResponse("Hello, you're at the stocks index.")