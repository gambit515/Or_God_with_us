from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import Anketa, Users
from .forms import PostForm

class StartPageView(ListView):
    model = Users
    template_name = 'main/startsheet.html'

class CreatePostView(CreateView): # new
    model = Users
    form_class = PostForm
    template_name = 'main/registeration.html'
    success_url = reverse_lazy('main')

def createanketas(request):
    return render(request, 'main/createanketas.html')


def mainsheet(request):
    anketas =  Anketa.objects.all()
    return render(request, 'main/mainsheet.html',{'anketas':anketas})


def startsheet(request):
    return render(request, 'main/startsheet.html')