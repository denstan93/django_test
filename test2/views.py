from django.shortcuts import render_to_response
from django.http import HttpResponse
from test2.models import *

def index(request):
    return HttpResponse("Это главная страница!")

def barbershop(request):
    s = ''
    for x in BarberShop.objects.filter():
        s = s + x.name+' '
    return HttpResponse(s)

def index2(request):
    return render_to_response(
        'index.html'
    )