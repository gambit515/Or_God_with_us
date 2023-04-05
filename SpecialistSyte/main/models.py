from django.db import models

# Create your models here.
class User(models.Model):
    SerName = models.CharField(max_length=50)
    Name = models.CharField(max_length=50)
    Patronymic = models.CharField(max_length=50)
    UserType = models.CharField(max_length=50)
    Login = models.CharField(max_length=50)
    Email = models.EmailField(max_length=254)
    Password = models.EmailField(max_length=254)

