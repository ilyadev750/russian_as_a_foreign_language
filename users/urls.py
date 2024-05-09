from django.urls import path
from .views import signup, activate, login_user, logout_user


urlpatterns = [
    path('signup/', signup, name='signup'),
    path('activate/<uidb64>/<token>/', activate, name='activate'),
    path('login/', login_user, name="login_user"),
    path('logout/', logout_user, name="logout_user")
]