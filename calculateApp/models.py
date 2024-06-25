from django.db import models

class login(models.Model):
    username = models.CharField(max_length=55)
    password = models.CharField(max_length=75)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    description = models.TextField(null=False, blank=True)
    
