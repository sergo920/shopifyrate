from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from shopifyrate_app import urls as shopifyrate_app_urls

from . import views

urlpatterns = [
    url(r'^healthcheck$', views.health_check),
    url(r'^', include(shopifyrate_app_urls)),
]
