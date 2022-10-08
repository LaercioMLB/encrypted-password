from django import forms

class PasswordForm(forms.Form):
    senha = forms.CharField(max_length=255)
    username = forms.CharField(max_length=255, required=False)
    descricao = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 6, 'cols': 40}))
    url = forms.CharField(max_length=255)
