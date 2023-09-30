from django.urls import path
from . import views
from .views import *



urlpatterns = [
    path('',StartPageView.as_view(), name = 'start'),
    path('main/',MainView, name = 'main'),
    path('index/',views.index, name = 'index'),
    path('otklikform/<int:anket_id>/',otklikform, name = 'otklikform'),
    path('profile/',ProfileView.as_view(), name = 'prof'),
    path('login/',MyprojectLoginView.as_view(), name = 'log'),
    path('createanketas/',AnketaView.as_view(), name = 'anket'),
    path('registration/',CreatePostView.as_view(), name='reg'),
    path('test/',TestView.as_view(), name='test'),
    path('ankets/<int:anket_id>/', show_anket, name='ankets'),
    path('lang_cat/<int:lang_cat_id>/', show_lang_cat, name='lang_cat'),
    path('logout',Logout.as_view(),name='logout'),
    path('about_us/',About_us_View.as_view(), name='about'),
    path('form2/',views.form2,name='form2')
]
