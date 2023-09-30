from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Anketa(models.Model):
    Tittle = models.CharField('Название вакансии',max_length=100)
    Text = models.TextField('Текст вакансии',max_length=1000)
    Photo = models.ImageField('Фотография',upload_to="photos/%Y/%m/%d/")
    Lang_cat = models.ForeignKey('Lang_categori',on_delete=models.CASCADE,verbose_name="Специальность")
    #Soft_cat = models.ForeignKey('Soft_categori', on_delete=models.CASCADE, verbose_name="Категория софта")
    Author = models.ForeignKey(User, on_delete=models.CASCADE,blank=True, verbose_name="Автор вакансии",null=True)
    Price = models.CharField('Зарплата',max_length=100,null=True)
    Text2 = models.TextField('Проф пометки',max_length=1000)

    def get_absolute_url(self):
       return reverse('anket', kwargs = {'anket_id': self.pk})

    def __str__(self):
        return self.Tittle
    class Meta:
        verbose_name = "Вакансии"
        verbose_name_plural = "Вакансии"
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



class Otklik(models.Model):
    FIO = models.CharField('ФИО',max_length=550)
    Anketa = models.ForeignKey('Anketa', on_delete=models.CASCADE, blank=True, verbose_name="Вакансия на которую откликнулись")
    BirthDate = models.CharField('Дата рождения', max_length=500)
    Email = models.EmailField('Почта', max_length=500)
    Phone = models.CharField('Телефон', max_length=100)
    Citizenship = models.CharField('Гражданство', max_length=300)
    Place = models.CharField('Место жительства', max_length=300)
    Portfolio = models.CharField('Ссылка на портфолио', max_length=500)
    Rezume = models.CharField('Резюме', max_length=500)
    DatePost = models.DateTimeField('Время отправки',auto_now_add=True)

    def __str__(self):
        return self.FIO

    def get_absolute_url(self):
       return reverse('otklik', kwargs = {'otklik': self.pk})

    class Meta:
        verbose_name = "Отклики"
        verbose_name_plural = "Отклики"
        ordering = ['DatePost']