from django import forms
from .models import Profile


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class ProfileForm(forms.Form):
    class Meta:
        model = Profile
        fields = ('intro', 'portrait')
