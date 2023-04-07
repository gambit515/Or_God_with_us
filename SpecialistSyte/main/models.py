from django.db import models

# Create your models here.
class Users(models.Model):
    Login = models.CharField(max_length=50)
    Password = models.CharField(max_length=50)
    Email = models.EmailField(max_length=254)
    SerName = models.CharField(max_length=50)
    Name = models.CharField(max_length=50)
    Patronymic = models.CharField(max_length=50)
    UserType = models.CharField(max_length=50)
    Photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    Time_create = models.DateTimeField(auto_now_add=True)


