from django.shortcuts import render
from .models import Anketa
from .forms import TaskForm


def createanketas(request):
    return render(request, 'main/createanketas.html')


def mainsheet(request):
    anketas =  Anketa.objects.all()
    return render(request, 'main/mainsheet.html',{'anketas':anketas})


def registration(request):
    form = TaskForm
    context = {
        'form': form
    }
    return render(request, 'main/registeration.html',context)


def startsheet(request):
    return render(request, 'main/startsheet.html')