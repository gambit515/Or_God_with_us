from .models import Anketa, Soft_categori, Lang_categori
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import ModelForm, TextInput, EmailInput, Textarea, ClearableFileInput, PasswordInput

class PostForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
                'class': 'vvod1',
                'type': 'password',
                'placeholder': 'Введите пароль',
                'id': 'password',
                'autocomplete': 'current-password'
            }),)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput(attrs={
                'class': 'vvod1',
                'type': 'password',
                'placeholder': 'Введите пароль',
                'id': 'password',
                'autocomplete': 'current-password'
            }),)
    class Meta:
        model = User
        fields = ['username', 'first_name','last_name', 'email']
        widgets = {
            "username": TextInput(attrs={
                'class': 'vvod',
                'type': 'text',
                'placeholder': 'Введите псевдоним пользователя',
                'id': 'user_psevdomin',
                'autocomplete': 'user_psevdomin'
            }),
            "first_name": TextInput(attrs={
                'class': 'vvod',
                'type': 'text',
                'placeholder': 'Введите ФИО',
                'id': 'user_psevdomin',
                'autocomplete': 'user_FIO'
            }),
            "email": EmailInput(attrs={
                'class': 'vvod3',
                'type': 'email',
                'placeholder': 'Введите электронную почту',
                'id': 'mail',
                'autocomplete': 'email'
            }),
            "last_name": TextInput(attrs={
                'class': 'vvod',
                'type': 'text',
                'placeholder': 'Введите краткое описание',
                'id': 'notes',
                'autocomplete': 'notes'
            }),
        }
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']
class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name','last_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']
class AnketaForm(forms.ModelForm):
    Lang_cat = forms.ModelChoiceField(queryset=Lang_categori.objects.all())
    Soft_cat = forms.ModelChoiceField(queryset=Soft_categori.objects.all())
    Author = forms.ModelChoiceField(queryset=User.objects.all())
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

