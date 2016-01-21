from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.conf import settings
from views import authenticate


def shop_login_required(func):
    def wrapper(request, *args, **kwargs):
        if not hasattr(request, 'session') or 'shopify' not in request.session:
            request.session['return_to'] = request.get_full_path()
            return authenticate(request)
        return func(request, *args, **kwargs)
    wrapper.__name__ = func.__name__
    return wrapper
