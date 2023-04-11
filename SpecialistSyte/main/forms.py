from .models import Users
from django.forms import ModelForm, TextInput


class TaskForm(ModelForm):
    class Meta:
        model = Users
        fields = ["Login","Password","Email","SerName","Name"]
        widgets = {
            "Login":TextInput(attrs={
                'class': 'vvod',
                'type': 'text',
                'placeholder': 'Введите псевдоним пользователя',
                'id': 'user_psevdomin',
                'autocomplete': 'user_psevdomin'
            }),
            "Password": TextInput(attrs={
                'class': 'vvod1',
                'type': 'password',
                'placeholder': 'Введите пароль',
                'id': 'password',
                'autocomplete': 'current-password'
            }),
            "Email": TextInput(attrs={
                'class': 'vvod3',
                'type': 'email',
                'placeholder': 'Введите электронную почту',
                'id': 'mail',
                'autocomplete': 'email'
            }),
            "SerName": TextInput(attrs={
                'class': 'vvod',
                'type': 'text',
                'placeholder': 'Введите вашу фамилию',
                'id': 'userfamily',
                'autocomplete': 'userfamily'
            }),
            "Name": TextInput(attrs={
                'class': 'vvod',
                'type': 'text',
                'placeholder': 'Введите ваше имя',
                'id': 'username',
                'autocomplete': 'username'
            }),
        }