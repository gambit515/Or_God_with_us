from django.urls import path
from . import views
from .views import StartPageView, CreatePostView, TestView, AnketaView

urlpatterns = [
    path('',StartPageView.as_view(), name = 'start'),
    path('main/',views.mainsheet, name = 'main'),
    path('createanketas/',AnketaView.as_view(), name = 'anket'),
    #path('post/', CreatePostView.as_view(), name='add_post') # new
    path('registration/',CreatePostView.as_view(), name='reg'),
    path('test/',TestView.as_view(), name='test'),
]
