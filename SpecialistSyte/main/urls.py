from django.urls import path
from . import views

urlpatterns = [
    path('',views.mainsheet),
    path('registration/',views.registration),
]
