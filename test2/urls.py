from django.urls import path
from test2.views import *

urlpatterns = [
    path('main_page', index),
    path('BarberShop', barbershop),
    path('',index2),
    path('login',login_user),
    path('logout',do_logout),
    path('register',register),
    path('registration',registration),
    path('ajax_path',ajax_path)

]