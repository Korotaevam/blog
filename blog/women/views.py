from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404


# Create your views here.

def index(request):
    return HttpResponse('Page aplication WOMAN ')


def categories(request, catid):
    if request.GET:
        print(request.GET)

    return HttpResponse(f'<h1> Articles by categories </h1><p>{catid}</p>')


def archive(request, year):
    if int(year) > 2020:
        return redirect('home', permanent=True)
    return HttpResponse(f"<h1>Архив по годам</h1>{year}</p>")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page not Found</h1>')
