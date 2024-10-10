from django import forms
from .models import ToDo

class LoginForm(forms.Form):
    username = forms.CharField(max_length = 35)
    password = forms.CharField(widget = forms.PasswordInput())

    def save():
        pass

class ToDoForm(forms.ModelForm):
    class Meta:
        model = ToDo
        fields = ('name', 'details', 'deadline')