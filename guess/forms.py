from django import forms
from .models import GuessGame

class GuessForm(forms.Form):
    number = forms.IntegerField(min_value=1, max_value=100)
