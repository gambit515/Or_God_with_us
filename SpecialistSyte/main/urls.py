from django.urls import path
from . import views

urlpatterns = [
    path('',views.mainsheet, name = 'home'),
    path('registration/',views.registration, name = 'reg'),
]
