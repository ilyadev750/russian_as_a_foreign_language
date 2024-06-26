from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms.widgets import TextInput, Select


class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Необходимое поле')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Имя пользователя",
                               max_length=40,
                               widget=TextInput(attrs={'class': 'login-field',
                                                       'placeholder': 'Имя пользователя'}))
    password = forms.CharField(label="Пароль",
                               widget=forms.PasswordInput(attrs={'class': 'login-field',
                                                                 'placeholder': 'Пароль'}))


class EmailForm(forms.Form):
    email = forms.EmailField(max_length=200, help_text='Необходимое поле')
