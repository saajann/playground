from django import forms
from .models import TrisGame

class MoveForm(forms.Form):
    row = forms.IntegerField(min_value=1, max_value=3)
    col = forms.IntegerField(min_value=1, max_value=3)
