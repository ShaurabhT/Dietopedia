from django.db import models
from Login.models import Customers
from django.contrib.auth.models import User,auth

# Create your models here.

class Calculations(models.Model):
    BMR=models.FloatField(default=None,null=True)
    date=models.DateTimeField(auto_now_add=True, blank=True)
    fieldname=models.CharField(max_length=20)
    user=models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    BDI=models.FloatField(default=None,null=True)
    Exerciselvl=models.IntegerField(default=1)