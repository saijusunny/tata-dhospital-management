
from django.db import models
from django.contrib.auth.models import User

class section(models.Model):
    Section_name = models.CharField(max_length=225)
    room_no = models.IntegerField()

class staff(models.Model):
    name=models.CharField(max_length=255)
    username=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    number = models.IntegerField()
    section = models.ForeignKey(section, on_delete=models.CASCADE, null=True)
    mail = models.EmailField(max_length=255)
    item = models.ImageField(upload_to='propic/items',null=True,blank=True)
    


    
class patient(models.Model):
    name=models.CharField(max_length=255)
    address=models.CharField(max_length=255)
    mobile=models.IntegerField()
    email=models.EmailField(max_length=255)
    age=models.IntegerField()
    section=models.ForeignKey(section, on_delete=models.CASCADE, null=True)

class doctor(models.Model):
    name=models.CharField(max_length=255)
    username=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    number = models.IntegerField()
    section = models.ForeignKey(section, on_delete=models.CASCADE, null=True)
    mail = models.EmailField(max_length=255)
    items = models.ImageField(upload_to='propic/items',null=True,blank=True)
    
# Create your models here.
class userlogin(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name=models.CharField(max_length=255)
    username=models.CharField(max_length=255)
    password=models.IntegerField()
    repassword=models.IntegerField()
    image=models.ImageField(upload_to="image/", null=True)
    email=models.CharField(max_length=255)
