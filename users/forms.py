from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import *
from captcha.fields import CaptchaField

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'custom-input',
            'placeholder': 'Username',
            'style': (
                'background-color: transparent; '
                'border: none; '
                'border-bottom: 1px solid white; '
                'color: white; '
                'padding: 10px; '
                'font-size: 16px; '
                'width: 100%; '
                'box-sizing: border-box; '
                'outline: none; '
            )
        })
    )

    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={
            'class': 'custom-input',
            'placeholder': 'Password',
            'style': (
                'background-color: transparent; '
                'border: none; '
                'border-bottom: 1px solid white; '
                'color: white; '
                'padding: 10px; '
                'font-size: 16px; '
                'width: 100%; '
                'box-sizing: border-box; '
                'outline: none; '
            )
        })
    )

    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={
            'class': 'custom-input',
            'placeholder': 'Confirm Password',
            'style': (
                'background-color: transparent; '
                'border: none; '
                'border-bottom: 1px solid white; '
                'color: white; '
                'padding: 10px; '
                'font-size: 16px; '
                'width: 100%; '
                'box-sizing: border-box; '
                'outline: none; '
            )
        })
    )

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class UserLoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'custom-input',
            'placeholder': 'Username',
            'style': (
                'background-color: transparent; '
                'border: none; '
                'border-bottom: 1px solid white; '
                'color: white; '
                'padding: 10px; '
                'font-size: 16px; '
                'width: 100%; '
                'box-sizing: border-box; '
                'outline: none; '
            )
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'custom-input',
            'placeholder': 'Password',
            'style': (
                'background-color: transparent; '
                'border: none; '
                'border-bottom: 1px solid white; '
                'color: white; '
                'padding: 10px; '
                'font-size: 16px; '
                'width: 100%; '
                'box-sizing: border-box; '
                'outline: none; '
            )
        })
    )

class UserEditForm(forms.ModelForm):
    first_name = forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=150)
    email = forms.EmailField(max_length=150)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = ProfileUser
        fields = ['birth', 'photo', 'hobby', 'city', 'phone', 'info']

class GalleryForm(forms.Form):
    images = forms.ImageField(widget=forms.ClearableFileInput(attrs={'allow multiple selected': True}), required=False)
    videos = forms.FileField(widget=forms.ClearableFileInput(attrs={'allow multiple selected': True}), required=False)


class MessageForm(forms.ModelForm):
    class Meta:
        model = MessageUser
        fields = ['content']




