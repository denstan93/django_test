from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from test2.models import *
from django.contrib.auth import authenticate, login

def index(request):
    contex= {'username': request.user.username,
             'flag': request.user.username == ""}
    return render_to_response(
        'main_page.html',
        contex
    )

def barbershop(request):
    s = ''
    for x in BarberShop.objects.filter():
        s = s + x.name+' '
    return HttpResponse(s)

def index2(request):
    return render_to_response(
        'index.html'
    )

def login_user(request):
    user = authenticate(
        username=request.POST['username'],
        password=request.POST['password']
    )
    if user is None:
        return render_to_response('error.html',{})
    else:
        login(request, user)
        return HttpResponseRedirect('main_page')