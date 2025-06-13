from django import forms
from django.contrib.auth.models import User

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput)
    #email = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)