from django.conf.urls import url, include
from shopify_auth import urls as shopify_auth_urls

from . import views

urlpatterns = [
    url(r'^login/', include(shopify_auth_urls)),
    url(r'^$', views.index, name='index_page'),
]
