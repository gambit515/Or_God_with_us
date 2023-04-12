from django.shortcuts import render, redirect
from .models import Anketa
from .forms import TaskForm


def createanketas(request):
    return render(request, 'main/createanketas.html')


def mainsheet(request):
    anketas =  Anketa.objects.all()
    return render(request, 'main/mainsheet.html',{'anketas':anketas})


def registration(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
        else:
            error = 'Форма была неверной'
    form = TaskForm
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/registeration.html',context)


def startsheet(request):
    return render(request, 'main/startsheet.html')