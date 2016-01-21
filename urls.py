from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
        url(r'^authenticate/$', 'shopify_auth.views.authenticate'),
        url(r'^finalize/$', 'shopify_auth.views.finalize'),
        url(r'^logout/$', 'shopify_auth.views.logout'),
)
