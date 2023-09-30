from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.
#class Users(models.Model):
#   Login = models.CharField('Логин',max_length=50)
#   Password = models.CharField('Пароль',max_length=50)
#   Email = models.EmailField('Почта',max_length=254)
#   SerName = models.CharField('Фамилия',max_length=50)
#   Name = models.CharField('Имя',max_length=50)
#   Patronymic = models.CharField('Отчество', max_length=50)
#   UserType = models.CharField('Тип пользователя',max_length=50)
#   Photo = models.ImageField('Фотография',upload_to="photos/%Y/%m/%d/",null=True)
#   Time_create = models.DateTimeField('Время создания',auto_now_add=True)
#   Notes = models.TextField('Краткое описание',max_length = 500,null=True)

#  def __str__(self):
#       return self.Login

#   class Meta:
#       verbose_name = "Пользователи сайта"
#       verbose_name_plural = "Пользователи сайта"
#       ordering = ['Login']
class Otkl(models.Model):
    Anketa = models.ForeignKey('Anketa', on_delete=models.CASCADE, blank=True, verbose_name="Анкета")
    Otkl_User = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, verbose_name="Откликнувшийся пользователь")
    def __str__(self):
        return self.Anketa
    class Meta:
        verbose_name = "Откликания на анкеты"
        verbose_name_plural = "Откликания на анкеты"
        ordering = ['Anketa','Otkl_User']

class Anketa(models.Model):
    Tittle = models.CharField('Название анкеты',max_length=100)
    Text = models.TextField('Текст анкеты',max_length=1000)
    Photo = models.ImageField('Фотография',upload_to="photos/%Y/%m/%d/")
    Lang_cat = models.ForeignKey('Lang_categori',on_delete=models.CASCADE,verbose_name="Специальность")
    #Soft_cat = models.ForeignKey('Soft_categori', on_delete=models.CASCADE, verbose_name="Категория софта")
    Author = models.ForeignKey(User, on_delete=models.CASCADE,blank=True, verbose_name="Автор анкеты",null=True)
    Price = models.CharField('Зарплата',max_length=100,null=True)
    Text2 = models.TextField('Проф пометки',max_length=1000)

    def get_absolute_url(self):
       return reverse('anket', kwargs = {'anket_id': self.pk})

    def __str__(self):
        return self.Tittle
    class Meta:
        verbose_name = "Анкеты пользователей"
        verbose_name_plural = "Анкеты пользователей"
        ordering = ['Tittle']

class Lang_categori(models.Model):
    Tittle = models.CharField('Специальность',max_length=150)
    #MainCategory = models.CharField('Главная категория', max_length=50)
    MainCategory = models.ForeignKey('Main_categori', on_delete=models.CASCADE, verbose_name="Категория софта")

    def __str__(self):
        return self.Tittle

    def get_absolute_url(self):
       return reverse('lang_cat', kwargs = {'lang_cat_id': self.pk})

    class Meta:
        verbose_name = "Специальности"
        verbose_name_plural = "Специальности"
        ordering = ['Tittle']


class Soft_categori(models.Model):
    Tittle = models.CharField('Категории софта',max_length=50)

    def __str__(self):
        return self.Tittle

    def get_absolute_url(self):
       return reverse('soft_cat', kwargs = {'soft_cat_id': self.pk})

    class Meta:
        verbose_name = "Категории софта"
        verbose_name_plural = "Категории софта"
        ordering = ['Tittle']


class Main_categori(models.Model):
    Tittle = models.CharField('Основные категория',max_length=150)

    def __str__(self):
        return self.Tittle

    def get_absolute_url(self):
       return reverse('main_cat', kwargs = {'main_cat': self.pk})

    class Meta:
        verbose_name = "Основные категория"
        verbose_name_plural = "Основные категория"
        ordering = ['Tittle']