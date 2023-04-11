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
class Anketa(models.Model):
    Tittle = models.CharField('Название анкеты',max_length=50)
    Text = models.CharField('Текст анкеты',max_length=50)
    Status = models.CharField('Статус',max_length=50)
    Photo = models.ImageField('Фотография',upload_to="photos/%Y/%m/%d/")
    Lang_cat = models.ForeignKey('Lang_categori',on_delete=models.PROTECT,verbose_name="Язык программирования")
    Soft_cat = models.ForeignKey('Soft_categori', on_delete=models.PROTECT, verbose_name="Категория софта")
    Author = models.ForeignKey('Users', on_delete=models.PROTECT, verbose_name="Автор анкеты")

    def __str__(self):
        return self.Tittle
    class Meta:
        verbose_name = "Анкеты пользователей"
        verbose_name_plural = "Анкеты пользователей"
        ordering = ['Tittle']

class Lang_categori(models.Model):
    Tittle = models.CharField('Язык программирования',max_length=50)

    def __str__(self):
        return self.Tittle
    class Meta:
        verbose_name = "Языки программирования"
        verbose_name_plural = "Языки программирования"
        ordering = ['Tittle']


class Soft_categori(models.Model):
    Tittle = models.CharField('Категории софта',max_length=50)

    def __str__(self):
        return self.Tittle
    class Meta:
        verbose_name = "Категории софта"
        verbose_name_plural = "Категории софта"
        ordering = ['Tittle']