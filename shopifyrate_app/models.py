from django.db import models
from shopify_auth.models import AbstractShopUser


class AuthAppShopUser(AbstractShopUser):
    myshopify_domain = models.CharField(max_length=255, unique=True)
    email = models.CharField(max_length=255, default=None, null=True)
    facebook_token = models.CharField(max_length=255, default=None, null=True)
    facebook_user_id = models.CharField(max_length=255, default=None, null=True)
