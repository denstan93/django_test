from django.urls import path
from test2.views import *

urlpatterns = [
    path('main_page', index),
    path('BarberShop', barbershop),
    path('',index2)
]