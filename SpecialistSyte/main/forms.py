from .models import Users, Anketa, Soft_categori, Lang_categori
from django import forms
from django.core.exceptions import ValidationError
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

class AnketaForm(forms.ModelForm):
    Lang_cat = forms.ModelChoiceField(queryset=Lang_categori.objects.all())
    Soft_cat = forms.ModelChoiceField(queryset=Soft_categori.objects.all())
    Author = forms.ModelChoiceField(queryset=Users.objects.all())
    class Meta:
        model = Anketa
        fields = ["Tittle","Text","Photo","Lang_cat","Soft_cat","Author","Place","Price","Time"]
        widgets = {
            "Tittle": TextInput(attrs={
                'class': 'vvod',
                'type': 'text',
                'placeholder': 'Введите название анкеты',
                'id': 'anketa_tittle',
                'autocomplete': 'anketa_tittle'
            }),
            "Text": Textarea(attrs={
                'class': 'vvod',
                'type': 'text',
                'placeholder': 'Введите текст анкеты',
                'id': 'anketa_text',
                'autocomplete': 'anketa_text'
            }),
            "Photo": ClearableFileInput(attrs={
                'type': 'file',
                'name': "Photo",
                'id': 'anketa_photo',
                'accept': "image/*",
                'required': "",
            }),
            "Place": TextInput(attrs={
                'class': 'vvod',
                'type': 'text',
                'placeholder': 'Введите место выполнения',
                'id': 'anketa_place',
                'autocomplete': 'anketa_place'
            }),
            "Price": TextInput(attrs={
                'class': 'vvod',
                'type': 'text',
                'placeholder': 'Введите плату за выполнение',
                'id': 'anketa_price',
                'autocomplete': 'anketa_price'
            }),
            "Time": TextInput(attrs={
                'class': 'vvod',
                'type': 'text',
                'placeholder': 'Введите сроки выполнения',
                'id': 'anketa_price',
                'autocomplete': 'anketa_price'
            })
        }

