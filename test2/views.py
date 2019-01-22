from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from test2.models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from test2.models import Client

def index(request):
    contex= {'username': request.user.username,
             'anonim': request.user.username == ""}
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

def do_logout(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect('/')
    else:
        return HttpResponse('egc')
def register(request):
    user = User.objects.create_user(
        request.POST['login'],
        password=request.POST['password'],
        first_name='aaaa',
        last_name='bbbb',
        email='a@b.c'
    )
    client = Client(user=user, address='Minsk')
    client.save()
    return HttpResponse('OK')

