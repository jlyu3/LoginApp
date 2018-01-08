from django.conf.urls import url
from . import views
from django.contrib.auth.views import (
    login, logout, password_reset, password_reset_done,
    password_reset_confirm, password_reset_complete
)

# defining a name for url can avoid hard coding url address by using the reverse function
urlpatterns = [
    url(r'^$',views.home),
    # args: defined url, which view in django to overwirte, html template to use
    url(r'^login/$', login,{'template_name': 'accounts/login.html'}, name = 'login'),
    url(r'^logout/$', logout,{'template_name': 'accounts/logout.html'}, name = 'logout'),
    url(r'^register/$', views.register, name = 'register'),
    # show the user info
    # if user wants to edit his info, may need to write another form.py
    url(r'^profile/$', views.view_profile, name = 'view_profile'),
    # a page that the user can edit his profile info
    url(r'^profile/edit/$', views.edit_profile, name = 'edit_profile'),
    # a page that allows the user change his password
    url(r'^change-password/$', views.change_password, name = 'change_password'),

    # below 4 urls call each other automatically when an action has been made
    url(r'^reset-password/$', password_reset,{'template_name': 
    # need to overwrite the 'post_reset_redirect' in the django built-in template,
    # otherwise the page doesn't work
    'accounts/reset_password.html', 
    'post_reset_redirect':'accounts:password_reset_done',
    'email_template_name':'accounts/reset_password_email.html'} ,name = "reset_password"),
    
    url(r'^reset-password/done/$', password_reset_done, 
    {'template_name': 'accounts/reset_password_done.html'}, name = "password_reset_done"),

    url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', 
    password_reset_confirm, {'template_name': 
    'accounts/reset_password_confirm.html', 'post_reset_redirect':
    'accounts:password_reset_complete'}, name = "password_reset_confirm"),

    url(r'^reset-password/complete/$', 
    password_reset_complete, {'template_name': 
    'accounts/reset_password_complete.html'}, name = "password_reset_complete"),
]