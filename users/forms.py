from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Необходимое поле')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class EmailForm(forms.Form):
    email = forms.EmailField(max_length=200, help_text='Необходимое поле')
