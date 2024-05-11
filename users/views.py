from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import SignupForm, EmailForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.sites.shortcuts import get_current_site
from django.core.exceptions import ObjectDoesNotExist
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import send_mail
from dotenv import load_dotenv
import os


load_dotenv()


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            mail_subject = 'Активируйте ваш аккаунт!'
            message = render_to_string('users/activation_email.html', {
                'user': user,
                'domain': 'localhost:8000',
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            status = send_mail(
                subject=mail_subject,
                message=mail_subject,
                from_email=os.getenv('EMAIL_HOST_USER'),
                recipient_list=[to_email],
                html_message=message,
            )
            print(status)
            context = {
                'activation': 'Пожалуйста, подвтердите вашу электронную почту для завершения регистрации!'
                }
            return render(request, 'users/send_activation_link.html', context=context)
    else:
        form = SignupForm()
    return render(request, 'users/signup.html', {'form': form})


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        context = {
            'success_activation': 'Спасибо за активацию почты. Теперь Вы можете зайти в личный кабинет!' 
            }
        return render(request, 'users/activation_successfull.html', context=context)
    else:
        return HttpResponse('Неверная ссылка!')


def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            form = AuthenticationForm()
            context = {
                "form": form,
                "error": 'Неверный пользователь или пароль!'
                }
            return render(request, "users/login.html", context)
    else:
        form = AuthenticationForm()
        error = ''
    return render(request, "users/login.html", {"form": form, "error": error})


def logout_user(request):
    logout(request)
    return redirect("home")


def get_activation_link(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            try:
                user = User.objects.get(email=form.cleaned_data['email'])
            except ObjectDoesNotExist:
                context = {
                    'form': EmailForm(),
                    'error': 'Данного пользователя не существует!'
                }
                return render(request, 'users/send_activation_link_again.html', context)
            if user.is_active:
                context = {
                    'form': EmailForm(),
                    'error': 'Данный пользователь уже активирован!'
                }
                return render(request, 'users/send_activation_link_again.html', context)
            else:
                mail_subject = 'Активируйте ваш аккаунт!'
                message = render_to_string('users/activation_email.html', {
                    'user': user,
                    'domain': 'localhost:8000',
                    'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                    'token':account_activation_token.make_token(user),
                })
                to_email = form.cleaned_data.get('email')
                status = send_mail(
                    subject=mail_subject,
                    message=mail_subject,
                    from_email=os.getenv('EMAIL_HOST_USER'),
                    recipient_list=[to_email],
                    html_message=message,
                )
                print(status)
                context = {
                    'activation': 'Пожалуйста, подвтердите вашу электронную почту для завершения регистрации!'
                    }
                return render(request, 'users/send_activation_link.html', context=context)
    context = {
        'form': EmailForm(),
        'error': ''
    }
    return render(request, 'users/send_activation_link_again.html', context=context)


# добавить реализацию изменения пароля

