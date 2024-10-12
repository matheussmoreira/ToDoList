from django import forms
from django.contrib.auth.models import User  
from django.contrib.auth.forms import UserCreationForm  
from django.core.exceptions import ValidationError
from .models import ToDo

class RegisterForm(UserCreationForm):  
    username = forms.CharField(label='Usuário', min_length=5, max_length=35)
    password1 = forms.CharField(label='Senha', widget=forms.PasswordInput)  
    password2 = forms.CharField(label='Repita a senha', widget=forms.PasswordInput)  
  
    def username_clean(self):  
        username = self.cleaned_data['username'].lower()  
        new = User.objects.filter(username = username)  
        if new.count():  
            raise ValidationError("Usuário já cadastrado!")  
        return self.username  
  
    def clean_password2(self):  
        password1 = self.cleaned_data['password1']  
        password2 = self.cleaned_data['password2']  
        if password1 and password2 and password1 != password2:  
            raise ValidationError("Senhas diferentes!")  
        return password2  
  
    def save(self, commit=True):  
        user = User.objects.create_user(  
            self.cleaned_data['username'],   
            self.cleaned_data['password1']  
        )  
        return user
    
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]

class LoginForm(forms.Form):
    username = forms.CharField(label='Usuário', max_length=35)
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)

    def save(self):
        pass

class ToDoForm(forms.ModelForm):
    class Meta:
        model = ToDo
        fields = ('name', 'details', 'deadline')