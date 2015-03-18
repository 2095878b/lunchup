from django import forms
from django.contrib.auth.models import User
from main.models import *
from django.forms import extras

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    firstName = forms.CharField(label='First name', max_length=64)
    lastName = forms.CharField(label='Last name', max_length=64)
    regularEmail = forms.EmailField(label='Public email')

    degree = forms.CharField(label='Degree title', max_length=64)
    about = forms.CharField(label='About me', help_text="", widget=forms.Textarea(attrs={'cols': 45, 'rows': 5}, ))
    picture = forms.ImageField(label='Profile picture')
    birthday = forms.DateField(label='Date of birth', widget=extras.SelectDateWidget)
    class Meta:
        model = UserProfile
        exclude = ('user', )