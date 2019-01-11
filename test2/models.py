from django.db import models

class BarberShop(models.Model):
    name = models.CharField(max_length=100)
    addres = models.CharField(max_length=100)
    time_work = models.CharField(max_length=100)
    raiting = models.IntegerField(default=0)
class Master(models.Model):
    name = models.CharField(max_length=100)
    work_place = models.ForeignKey(BarberShop, on_delete=models.CASCADE)
    raiting = models.IntegerField(default=0)
    experience = models.IntegerField(default=0)
    portfolio = models.CharField(max_length=100)

