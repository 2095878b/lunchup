from django import forms
from main.models import *
from django.forms import extras

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    firstName = forms.CharField(label='First name', max_length=64, required=False)
    lastName = forms.CharField(label='Last name', max_length=64, required=False)
    publicEmail = forms.EmailField(label='Public email', required=False)

    about = forms.CharField(label='About me', help_text="", widget=forms.Textarea(attrs={'cols': 45, 'rows': 5}, ), required=False)
    picture = forms.ImageField(label='Profile picture', required=False)

    years = [i for i in range(1900, 2002, 1)]
    birthday = forms.DateField(label='Date of birth', widget=extras.SelectDateWidget(years=years), required=False)

    class Meta:
        model = UserProfile
        exclude = ('user', 'university', 'interests')