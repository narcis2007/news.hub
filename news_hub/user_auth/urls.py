__author__ = 'narcis'
from django.conf.urls import url

from . import views

urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^login$',views.login_view,name='login'),
    url(r'^auth$',views.auth_view,name='auth'),
    url(r'^invalid$',views.invalid,name='invalid'),
    url(r'^logged$',views.logged,name='logged'),
    url(r'^logged_out$',views.logged_out,name='logged_out'),
    url(r'^sign_up$',views.register_user,name='sign_up'),
    url(r'^register$',views.register_user,name='register_user'),
    url(r'^registered$',views.registered,name='registered'),
    url(r'^forgot_pass$',views.forgot_pass,name='forgot_pass'),
    url(r'^forgot_pass/send$',views.send_reset_pass_link,name='forgot_pass'),


    url(r'^accounts/password/reset/$', 'django.contrib.auth.views.password_reset', {'post_reset_redirect' : '/accounts/password/reset/done/'}),
    url(r'^accounts/password/reset/done/$', 'django.contrib.auth.views.password_reset_done'),
    url(r'^accounts/password/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm', {'post_reset_redirect' : '/accounts/password/done/'}),
    url(r'^accounts/password/done/$', 'django.contrib.auth.views.password_reset_complete'),
]