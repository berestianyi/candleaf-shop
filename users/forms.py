from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

from users.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "Enter your username"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': "Enter your password"}))

    class Meta:
        model = User
        fields = ('username', 'password')


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "Enter your username"}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "Enter your First name"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "Enter your Last name"}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': "Enter your email"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': "Create password"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': "Repeat password"}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')


class UserProfileForm(UserChangeForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'readonly': True, 'class': 'read'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'readonly': True, 'class': 'read'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={
        'class': 'photo-change-button-input', 'value': 'Change photo', 'type': 'file', 'id': 'file-upload'
    }), required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'image')
