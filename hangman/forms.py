from django import forms

class LetterForm(forms.Form):
    letter = forms.CharField(max_length=1, required=True)

    def clean_letter(self):
        letter = self.cleaned_data['letter'].lower()
        if not letter.isalpha():
            raise forms.ValidationError("Inserisci solo lettere alfabetiche.")
        return letter