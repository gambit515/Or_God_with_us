from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import Anketa, Users, Soft_categori, Lang_categori
from .forms import PostForm, AnketaForm

class StartPageView(ListView):
    model = Users
    template_name = 'main/startsheet.html'

class CreatePostView(CreateView): # new
    model = Users
    form_class = PostForm
    template_name = 'main/registeration.html'
    success_url = reverse_lazy('main')

class AnketaView(CreateView): # new
    model = Anketa
    form_class = AnketaForm
    template_name = 'main/createanketas.html'
    success_url = reverse_lazy('main')

class TestView(CreateView): # new
    model = Anketa
    form_class = AnketaForm
    template_name = 'main/test.html'
    success_url = reverse_lazy('main')

def createanketas(request):
    return render(request, 'main/createanketas.html')


def mainsheet(request):
    anketas =  Anketa.objects.all()
    soft_cat = Soft_categori.objects.all()
    lang_cat = Lang_categori.objects.all()
    context = {
        'anketas':anketas,
        'soft_cat':soft_cat,
        'lang_cat':lang_cat,
        'cat_selected': 0,
    }
    return render(request, 'main/mainsheet.html',context)


def startsheet(request):
    return render(request, 'main/startsheet.html')


def show_anket(request,anket_id):
    return  HttpResponse(f"Оображение анкет с id ={anket_id}")

def index(request):
    ankets = Anketa.objects.all()
    context = {
        'ankets' :ankets
    }
    return render(request,'main/index.html',context=context)

def show_soft_cat(request,soft_cat_id):
    anketas = Anketa.objects.filter(Soft_cat_id=soft_cat_id)
    soft_cat = Soft_categori.objects.all()
    lang_cat = Lang_categori.objects.all()
    context = {
        'anketas': anketas,
        'soft_cat': soft_cat,
        'lang_cat': lang_cat,
        'cat_selected': 1,
    }

    return render(request, 'main/mainsheet.html', context)

def show_lang_cat(request,lang_cat_id):
    anketas = Anketa.objects.filter(Lang_cat_id=lang_cat_id)
    soft_cat = Soft_categori.objects.all()
    lang_cat = Lang_categori.objects.all()
    context = {
        'anketas': anketas,
        'soft_cat': soft_cat,
        'lang_cat': lang_cat,
        'cat_selected': 1,
    }

    return render(request, 'main/mainsheet.html', context)