# re: regular expression (deal with urls)
import re
from django.conf import settings
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.urls import reverse

# some random comments

# a list contains compiled version of regular expression in urls
EXEMPT_URLS = [re.compile(settings.LOGIN_URL.lstrip('/'))]
if hasattr(settings,'LOGIN_EXEMPT_URLS'):
    EXEMPT_URLS += [re.compile(url) for url in settings.LOGIN_EXEMPT_URLS]

class LoginRequiredMiddleware:
    def __init__(self, get_response):
       self.get_response = get_response
    
    def __call__(self, request):
        response = self.get_response(request)
        return response

    # This function will run first when django is about to call any view
    # view_func represents the view that is going to be called
    def process_view(self, request, view_func, view_args, view_kwargs):
        assert hasattr(request,'user')
        path = request.path_info.lstrip('/')
        
        #if not request.user.is_authenticated():
            #if not any(url.match(path) for url in EXEMPT_URLS):
                #return redirect(settings.LOGIN_URL)
        
        url_is_exempt = any(url.match(path) for url in EXEMPT_URLS)

        # reverse gives us the path with forward slash at the begining of the logout url
        # "accounts:" is the namespace defined in root url.py; it specifies the specific app
        # And there should be no space ' ' after "accounts:"
        if path == reverse('accounts:logout').lstrip('/'):
            logout(request)
        
        if request.user.is_authenticated() and url_is_exempt:
            # after user is logged out, he will be redirect to home page
            return redirect(settings.LOGIN_REDIRECT_URL)
        elif request.user.is_authenticated() or url_is_exempt:
            return None
        else:
            return redirect(settings.LOGIN_URL)


