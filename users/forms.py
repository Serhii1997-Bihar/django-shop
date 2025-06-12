from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import *
from captcha.fields import CaptchaField

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
    captcha = CaptchaField(label='Уведіть код', error_messages={'invalid': 'Не правильно!'})

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




