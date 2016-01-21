from django.shortcuts import render_to_response, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.conf import settings
import shopify

def _return_address(request):
    return request.session.get('return_to') or reverse('root_path')


def authenticate(request):
    shop = request.REQUEST.get('shop')
    if shop:
        scope = settings.SHOPIFY_API_SCOPE
        redirect_uri = request.build_absolute_uri(reverse('shopify_auth.views.finalize'))
        permission_url = shopify.Session(shop.strip()).create_permission_url(scope, redirect_uri)
        return render(request, 'shopify_auth/oauth_redirect.html',
            { 'permission_url': permission_url })

    return redirect(_return_address(request))

def finalize(request):
    shop_url = request.REQUEST.get('shop')
    try:
        shopify_session = shopify.Session(shop_url)
        request.session['shopify'] = {
            "shop_url": shop_url,
            "access_token": shopify_session.request_token(request.REQUEST)
        }

    except Exception:
        messages.error(request, "Could not log in to Shopify store.")
        return redirect(reverse('shopify_auth.views.login'))

    messages.info(request, "Logged in to shopify store.")

    response = redirect(_return_address(request))
    request.session.pop('return_to', None)
    return response

def logout(request):
    request.session.pop('shopify', None)
    messages.info(request, "Successfully logged out.")

    return redirect(reverse('shopify_auth.views.login'))
