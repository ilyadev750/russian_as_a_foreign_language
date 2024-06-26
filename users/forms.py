from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm
from django.contrib.auth.models import User
from django.forms.widgets import TextInput, Select, PasswordInput


class SignupForm(UserCreationForm):
    first_name = forms.CharField(max_length=100,
                               widget=TextInput(
                                   attrs={'class': 'signup-field', 'placeholder': 'Имя'})
                                   )
    last_name = forms.CharField(max_length=100,
                               widget=TextInput(
                                   attrs={'class': 'signup-field', 'placeholder': 'Фамилия'})
                                   )
    # username = forms.CharField(max_length=50,
    #                            widget=TextInput(
    #                                attrs={'class': 'signup-field', 'placeholder': 'Имя пользователя'})
    #                                )
    email = forms.EmailField(max_length=200,
                             help_text='Необходимое поле',
                             widget=TextInput(
                                 attrs={'class': 'signup-field', 'placeholder': 'Электронная почта'})
                                 )
    password1 = forms.CharField(widget=PasswordInput(
        attrs={'class': 'signup-field', 'placeholder': 'Пароль'})
        )
    password2 = forms.CharField(widget=PasswordInput(
        attrs={'class': 'signup-field', 'placeholder': 'Повторите пароль'})
        )
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2')


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


class UserPasswordResetForm(PasswordResetForm):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'reset-field',
                'autocomplete': 'off',
                'placeholder': 'Электронная почта'
            })
