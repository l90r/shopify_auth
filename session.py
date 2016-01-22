def get_shopify_context(request):
	return request.session.get('shopify')

