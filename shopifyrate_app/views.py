import os
import shopify
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from shopify_auth.decorators import login_required


@login_required
def index(request):
    with open(os.path.join(settings.REACT_APP_DIR, 'build', 'index.html')) as f:
        return HttpResponse(f.read())


@login_required
def shopify_products(request):
    """
    view func returns all user products
    :param request:
    :return:
    """
    data = []
    fields = request.GET.get('fields', request.POST.get('fields', []))
    with request.user.session:
        page = 1
        while True:
            products = shopify.Product.find(page=page, limit=250, fields=fields)
            if products:
                data += products
                page += 1
            else:
                break
    return JsonResponse(data, safe=False)
