from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index_page'),
    url(r'^login/', include('shopify_auth.urls')),
]
