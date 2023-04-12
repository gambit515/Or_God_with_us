from django.urls import path
from . import views
from .views import StartPageView, CreatePostView

urlpatterns = [
    path('',StartPageView.as_view(), name = 'start'),
    path('main/',views.mainsheet, name = 'main'),
    path('createanketas/',views.createanketas, name = 'anket'),
    #path('post/', CreatePostView.as_view(), name='add_post') # new
    path('registration/',CreatePostView.as_view(), name='reg'),
]
