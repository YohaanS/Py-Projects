from django import forms
from .models import login

class PersonForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = login
        fields = ['username', 'password', 'first_name', "last_name", "description"]