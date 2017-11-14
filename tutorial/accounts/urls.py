from django.conf.urls import url
from . import views
from django.contrib.auth.views import login

urlpatterns = [
    url(r'^$',views.home),
    # args: defined url, which view, html template to use
    url(r'^login/$', login,{'template_name': 'accounts/login.html'})
]