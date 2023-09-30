from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User, Group
from django.contrib.auth.views import LoginView, LogoutView, TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import RequestContext
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import Anketa, Lang_categori, Otkl, Otklik
from .forms import PostForm, AnketaForm, AuthUserForm, OtklForm,OtklikForm
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
        self.object.groups.clear()
        self.object.groups.add(form.cleaned_data['groups'])
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
'''
class TestView(CreateView): # new
    model = Anketa
    form_class = AnketaForm
    template_name = 'main/test.html'
    success_url = reverse_lazy('main')
'''
def MainView(request):
    form_class = OtklForm  # Ваша форма (если есть)
    query = request.GET.get('q', '')
    lang_cat = Lang_categori.objects.all()
    results = Anketa.objects.filter(Tittle__icontains=query)
    context = {
        'anketas': results,  # Переименовали anketas в results, так как это результаты поиска
        'results': results,
        'lang_cat': lang_cat,
        'lang_cat_selected': 0,
        'query': query,
    }

    return render(request, 'main/mainsheet.html', context)

def startsheet(request):
    return render(request, 'main/startsheet.html')


def otklikform(request,anket_id):
    if request.method == 'POST':
        form = OtklikForm(request.POST)
        if form.is_valid():
            otklik = form.save(commit=False)
            otklik.Anketa_id = anket_id  # Устанавливаем значение поля Anketa_id
            otklik.save()
            return render(request, 'main/form2.html')
    else:
        form = OtklikForm()

    return render(request, 'main/form.html', {'form': form})


def show_anket(request,anket_id):

    context = {
        'anket_id': anket_id

    }
    anketas = Anketa.objects.all()
    if request.method == 'POST':
        form = OtklForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.Otkl_User = request.user
            instance.Anketa = Anketa.objects.get(id=anket_id)
            instance.save()
            return render(request, 'main/form2.html')
    else:
        form = OtklForm()
    return render(request,'main/fullInfoAnketa.html', {'form': form,'anket_id': anket_id,'anketas':anketas} )
    #return render(request,'main/form.html', {'form': form,'anket_id': anket_id} )
'''
def index(request):
    ankets = Anketa.objects.all()
    context = {
        'ankets' :ankets
    }
    return render(request,'main/index.html',context=context)
'''
def fullInfoSheet(request):
    ankets = Anketa.objects.all()
    context = {
        'ankets' :ankets
    }
    return render(request,'main/fullInfoAnketa.html',context=context)


class ProfileView(LoginRequiredMixin,TemplateView): # new
    template_name = 'main/profile.html'
    login_url = reverse_lazy('log')

    def get(self, request):
        otkl = Otklik.objects.all()
        context = {
            'otkl': otkl,
        }
        return render(request, 'main/profile.html', context)


def show_lang_cat(request,lang_cat_id):
    anketas = Anketa.objects.filter(Lang_cat_id=lang_cat_id)
    query = request.GET.get('q', '')
    results = anketas.filter(Tittle__icontains=query)  # Фильтруйте анкеты по полю Tittle
    lang_cat = Lang_categori.objects.all()
    context = {
        'anketas': anketas,
        'results': results,
        'lang_cat': lang_cat,
        'lang_cat_selected': lang_cat_id,
        'query': query,
    }

    return render(request, 'main/mainsheet.html', context)


class MyprojectLoginView(LoginView):
    model = User
    template_name = 'main/login-form.html'
    form_class = AuthUserForm
    success_url = reverse_lazy('main')
    def get_success_url(self):
        return self.success_url

class Logout(LogoutView):
    next_page = reverse_lazy('main')

class About_us_View(TemplateView):
    template_name = 'main/aboutUs.html'

def form2(request):
    return render(request, 'main/form2.html')