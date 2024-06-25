from django.db import models
from django import forms

class login(models.Model):
    username = models.CharField(max_length=55)
    password = models.CharField(max_length=75)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    description  = models.TextField(null=False, blank=True)

Operations = {
    ("Addition", "+"),
    ("Subtraction", "-"),
    ("Multiplication", "*"),
    ("Division", "/")
}

class Calculate(models.Model):
    operation = models.CharField(max_length=15,
    choices=Operations, 
    blank=False, 
    null=False)
    firstnumber = models.DecimalField(max_digits=30, decimal_places=25)
    secondnumber = models.DecimalField(max_digits=30, decimal_places=25)

Sodas = {
    ("Pepsi", "pepsi"),
    ("Mountain Dew", "mountain-dew"),
    ("Coca Cola", "coca-cola"),
    ("Limca", "limca"),
    ("Sprite", "sprite"),
    ("Fanta", "fanta")
}

class VendingMachine(models.Model):
    amount = models.IntegerField()
    soda = models.CharField(max_length=15, choices=Sodas)

