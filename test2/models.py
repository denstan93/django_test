from django.db import models
from django.contrib.auth.models import User

class BarberShop(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    addres = models.CharField(max_length=100)
    time_work = models.CharField(max_length=100)
    raiting = models.IntegerField(default=0)
class Master(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    work_place = models.CharField(max_length=100)
    raiting = models.IntegerField(default=0)
    experience = models.IntegerField(default=0)
    portfolio = models.CharField(max_length=100)

class Client(models.Model):
    address = models.CharField('Address', max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

