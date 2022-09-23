from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    return HttpResponse('Page aplication WOMAN ')


def categories(request, catid):
    return HttpResponse(f'<h1> Articles by categories </h1><p>{catid}</p>')
