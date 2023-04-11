from .models import Users
from django.forms import ModelForm


class TaskForm(ModelForm):
    class Meta:
        model = Users
        fields = ["Login,Password,Email,SerName,Name,Patronymic,UserType,Photo"]