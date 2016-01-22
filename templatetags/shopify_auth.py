import datetime
from django import template
from django.conf import settings

register = template.Library()

@register.inclusion_tag('shopify_auth/shopify_header.html', takes_context=True)
def shopify_header(context):
    shopify_context = context.get('shopify_context')
    if shopify_context:
    	shop = shopify_context.get('shop_url', None)
    else:
    	shop = None
    result = {
        'api_key': settings.SHOPIFY_API_KEY,
        'shop_url': shop
    }
    return result

