from django.shortcuts import render


def mainsheet(request):
    return render(request, 'main/mainsheet.html')

def registration(request):
    return render(request, 'main/registeration.html')