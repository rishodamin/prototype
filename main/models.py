from django.db import models

# Create your models here.
class Works(models.Model):
    name = models.CharField(max_length=100)
    id = models.CharField(max_length=1000, primary_key=True)
    IntId = models.IntegerField()

class Details(models.Model):
    username = models.CharField(max_length=500)
    name = models.CharField(max_length=100)
    phonenum = models.CharField(max_length=100)

class PostJobs(models.Model):
    strId = models.CharField(max_length=10000)
    username = models.CharField(max_length=500)
    name = models.CharField(max_length=1000)
    category = models.CharField(max_length=500)
    date = models.DateField()
    time = models.TimeField()
    strength = models.IntegerField()
    menWage = models.IntegerField()
    womenWage = models.IntegerField()
    phonenum = models.CharField(max_length=50)
    town = models.CharField(max_length=100)
    address = models.CharField(max_length=1000)
    description = models.CharField(max_length=10000)



