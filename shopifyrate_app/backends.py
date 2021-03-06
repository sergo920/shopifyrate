import shopify
from django.contrib.auth.backends import RemoteUserBackend


class ShopUserBackend(RemoteUserBackend):

    def authenticate(self, myshopify_domain=None, token=None, **kwargs):
        if not myshopify_domain or not token:
            return

        user = super(ShopUserBackend, self).authenticate(request=None, remote_user=myshopify_domain)
        if not user:
            return

        if user.email is None:
            with shopify.Session.temp(myshopify_domain, token):
                shop = shopify.Shop.current()
                user.email = shop.to_dict().get('email')
                user.token = token
                user.save(update_fields=['token', 'email'])
        else:
            user.token = token
            user.save(update_fields=['token'])

        return user
