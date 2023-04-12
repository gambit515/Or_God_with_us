from .models import Users
from django import forms
from django.forms import ModelForm, TextInput, EmailInput, Textarea, ClearableFileInput, ImageField

class PostForm(forms.ModelForm):

    class Meta:
        model = Users
        fields = ["Login","Password","Email","SerName","Name","Photo","Notes","Patronymic","UserType"]
        widgets = {
            "Login": TextInput(attrs={
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
            "Email": EmailInput(attrs={
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
            "UserType": TextInput(attrs={
                'class': 'vvod',
                'type': 'text',
                'placeholder': 'Введите 1 или 2',
                'id': 'usertype',
                'autocomplete': 'usertype'
            }),
            "Patronymic": TextInput(attrs={
                'class': 'vvod',
                'type': 'text',
                'placeholder': 'Введите ваше отчество',
                'id': 'otchestvoname',
                'autocomplete': 'otchestvoname'
            }),
            "Photo": ClearableFileInput(attrs={
                'type': 'file',
                'name': "Photo",
                'id': 'id_Photo',
                'accept': "image/*",
                'required': "",
            }),
            "Notes": Textarea(attrs={
                'class': 'vvod',
                'type': 'text',
                'placeholder': 'Введите описание',
                'id': 'textar',
                'autocomplete': 'textar'
            }),
        }