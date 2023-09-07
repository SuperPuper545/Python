import re
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import Offers


class NewsForm(forms.ModelForm):
    class Meta:
        model = Offers
        fields = ['organisation', 'name_SI']
        widgets = {
            'organisation': forms.TextInput(attrs={'class': 'form-control'}),
            'name_SI': forms.TextInput(attrs={'class': 'form-control', 'rows': 5}, ),
        }

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label="Имя пользователя", widget=forms.TextInput(attrs={'class': "form-control"})),
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={'class': "form-control"}))


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email', "password1", "password2")
