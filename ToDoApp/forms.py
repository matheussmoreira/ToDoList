from django import forms
from django.contrib.auth.forms import UserCreationForm  
from .models import *

class RegisterForm(UserCreationForm):  
    username = forms.CharField(label='Usuário', min_length=5, max_length=35)
    password1 = forms.CharField(label='Senha', widget=forms.PasswordInput)  
    password2 = forms.CharField(label='Repita a senha', widget=forms.PasswordInput)
    
    class Meta:
        model = CustomUser
        fields = ["username", "password1", "password2"]

class LoginForm(forms.Form):
    username = forms.CharField(label='Usuário', max_length=35)
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['username','password']

class ToDoForm(forms.ModelForm):
    class Meta:
        model = ToDo
        fields = ('name',)