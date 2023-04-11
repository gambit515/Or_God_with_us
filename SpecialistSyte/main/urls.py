from django.urls import path
from . import views

urlpatterns = [
    path('',views.startsheet, name = 'start'),
    path('registration/',views.registration, name = 'reg'),
    path('main/',views.mainsheet, name = 'main'),
    path('createanketas/',views.createanketas, name = 'anket'),
]
