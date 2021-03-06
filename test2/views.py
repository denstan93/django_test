from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from test2.models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from test2.models import Client


def index(request):
    contex = {'username': request.user.username,
              'anonim': request.user.username == ""}
    return render_to_response(
        'main_page.html',
        contex
    )


def barbershop(request):
    s = ''
    for x in BarberShop.objects.filter():
        s = s + x.name + ' '
    return HttpResponse(s)


def index2(request):
    contex = {'username': request.user.username,
              'anonim': request.user.username == ""}
    return render_to_response(
        'index.html',
        contex
    )

def users(request):
    contex = {'username': request.user.username,
              'anonim': request.user.username == ""}
    return render_to_response(
        'users.html',
        contex
    )

def login_user(request):
    user = authenticate(
        username=request.POST['username'],
        password=request.POST['password']
    )
    if user is None:
        return render_to_response('error.html', {})
    else:
        login(request, user)
        return HttpResponseRedirect('/')


def do_logout(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect('/')
    else:
        return HttpResponse('404')


def register(request):
    contex = {'username': request.user.username,
              'anonim': request.user.username == ""}
    return render_to_response('register.html', contex)


def registration(request):
    user = User.objects.create_user(
        username=request.POST['username'],
        password=request.POST['password'],
        email=request.POST['email']
    )

    name_barber_shop = request.POST['name_barber_shop']
    addres = request.POST['addres']
    time_work = request.POST['time_work']
    barber_shop = BarberShop(user=user, name=name_barber_shop, addres=addres, time_work=time_work)
    barber_shop.save()

    name_master = request.POST['name_master']
    work_place = request.POST['work_place']
    experience = request.POST['experience']
    master = Master(user=user, name=name_master, work_place=work_place, experience=experience)
    master.save()

    name_client = request.POST['name_client']
    client = Client(user=user, name=name_client)
    client.save()
    return HttpResponseRedirect('/')


def ajax_path(request):
    response = {
        'message': request.POST['a'] + ' world'
    }
    return JsonResponse(response)


#
# name2 = request.POST['name_master'],
# work_place = request.POST['work_place'],
# experience = request.POST['experience']
