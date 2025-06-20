from django import forms
from .models import HangmanWord

class LetterForm(forms.Form):
    letter = forms.CharField(max_length=1, required=True)

    def clean_letter(self):
        letter = self.cleaned_data['letter'].lower()
        if not letter.isalpha():
            raise forms.ValidationError("Insert only letters.")
        return letter
    
class AddWordForm(forms.ModelForm):
    text = forms.CharField(required=True)
    class Meta:
        model = HangmanWord
        fields = ['text']

class EditWordForm(forms.ModelForm):
    class Meta:
        model = HangmanWord
        fields = ['text']

class CSVUploadForm(forms.Form):
    file = forms.FileField(label='Upload CSV file')