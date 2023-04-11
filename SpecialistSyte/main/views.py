from django.shortcuts import render
from .models import Anketa

def mainsheet(request):
    anketas =  Anketa.objects.all()
    return render(request, 'main/mainsheet.html',{'anketas':anketas})

def registration(request):
    return render(request, 'main/registeration.html')

def startsheet(request):
    return render(request, 'main/startsheet.html')