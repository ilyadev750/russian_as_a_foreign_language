from django.urls import re_path, path
from .views import signup, activate


urlpatterns = [
    # re_path(r'^signup/$', signup, name='signup'),
    # re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    #     activate, name='activate'),
    path('signup/', signup, name='signup'),
    path('activate/<uidb64>/<token>/', activate, name='activate')
]