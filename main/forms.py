from django import forms
from django.contrib.auth.models import User
from main.models import *

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    your_name = forms.CharField(label='Your name', max_length=100)
    class Meta:
        model = UserProfile
        fields = ('firstName', 'lastName', 'regularEmail', 'interests', 'university', 'degree', 'about', 'picture', 'birthday')