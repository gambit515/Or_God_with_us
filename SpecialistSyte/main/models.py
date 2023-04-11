from django.db import models

# Create your models here.
class Users(models.Model):
    Login = models.CharField('Логин',max_length=50)
    Password = models.CharField('Пароль',max_length=50)
    Email = models.EmailField('Почта',max_length=254)
    SerName = models.CharField('Фамилия',max_length=50)
    Name = models.CharField('Имя',max_length=50)
    Patronymic = models.CharField('Отчество',max_length=50)
    UserType = models.CharField('Тип пользователя',max_length=50)
    Photo = models.ImageField('Фотография',upload_to="photos/%Y/%m/%d/")
    Time_create = models.DateTimeField('Время создания',auto_now_add=True)

    def __str__(self):
        return self.Login
    class Meta:
        verbose_name = "Пользователи сайта"
        verbose_name_plural = "Пользователи сайта"
        ordering = ['Login']

