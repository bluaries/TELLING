from django import forms
from login.models import UserProfileInfo
from .models import AppUser

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = AppUser
        fields = ('username','password','email')