from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView, TemplateView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import Anketa, Soft_categori, Lang_categori
from .forms import PostForm, AnketaForm, AuthUserForm
from django.contrib.auth.mixins import LoginRequiredMixin

class StartPageView(ListView):
    model = User
    template_name = 'main/startsheet.html'

class CreatePostView(CreateView): #Класс регистрации
    model = User
    form_class = PostForm
    template_name = 'main/registeration.html'
    success_url = reverse_lazy('main')

    def form_valid(self, form):
        form_valid = super().form_valid(form)
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        aut_user = authenticate(username=username,password=password)
        login(self.request, aut_user)
        return form_valid

class AnketaView(LoginRequiredMixin,CreateView): # new
    model = Anketa
    form_class = AnketaForm
    template_name = 'main/createanketas.html'
    success_url = reverse_lazy('main')
    login_url = reverse_lazy('log')

    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.Author = self.request.user
        self.object.save()
        return super().form_valid(form)

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
        'soft_cat_selected': 0,
        'lang_cat_selected': 0,
    }
    return render(request, 'main/mainsheet.html',context)

def startsheet(request):
    return render(request, 'main/startsheet.html')
#def login(request):
#   return render(request, 'main/login-form.html')


def show_anket(request,anket_id):
    return  HttpResponse(f"Оображение анкет с id ={anket_id}")

def index(request):
    ankets = Anketa.objects.all()
    context = {
        'ankets' :ankets
    }
    return render(request,'main/index.html',context=context)

class ProfileView(LoginRequiredMixin,TemplateView): # new
    template_name = 'main/profile.html'
    login_url = reverse_lazy('log')


def show_soft_cat(request,soft_cat_id):
    anketas = Anketa.objects.filter(Soft_cat_id=soft_cat_id)
    soft_cat = Soft_categori.objects.all()
    lang_cat = Lang_categori.objects.all()
    context = {
        'anketas': anketas,
        'soft_cat': soft_cat,
        'lang_cat': lang_cat,
        'soft_cat_selected': soft_cat_id,
        'lang_cat_selected': 0,
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
        'soft_cat_selected': 0,
        'lang_cat_selected': lang_cat_id,
    }

    return render(request, 'main/mainsheet.html', context)

class MyprojectLoginView(LoginView):
    template_name = 'main/login-form.html'
    form_class = AuthUserForm
    success_url = reverse_lazy('main')
    def get_success_url(self):
        return self.success_url

class Logout(LogoutView):
    next_page = reverse_lazy('main')