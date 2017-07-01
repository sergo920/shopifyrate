import os
import shopify
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from shopify_auth.decorators import login_required
from facebookads.api import FacebookAdsApi
from facebookads.adobjects.advideo import AdVideo
from facebookads.adobjects.adaccount import AdAccount


@login_required
def index(_):
    with open(os.path.join(settings.REACT_APP_DIR, 'build', 'index.html')) as f:
        return HttpResponse(f.read())


@login_required
def get_shopify_products(request):
    """
    view func returns all Shopify user products
    :param request:
    :return:
    """
    images = []
    categories = set()
    fields = ['id', 'title', 'images', 'variants', 'product_type']
    with request.user.session:
        page = 1
        while True:
            products = shopify.Product.find(page=page, limit=250, fields=fields)
            if products:
                for product in products:
                    if product.images:
                        product_type = product.product_type
                        if product_type:
                            categories.add(product_type)
                        for image in product.images:
                            images.append({'original': image.src, 'thumbnail': image.src})
                page += 1
            else:
                break
    return JsonResponse({'images': images}, safe=False)


@login_required
def create_video(request):
    FacebookAdsApi.init(account_id=settings.FACEBOOK_MAIN_AD_ACCOUNT, access_token=settings.FACEBOOK_TEST_TOKEN)
    ad_video = AdAccount(fbid=settings.FACEBOOK_MAIN_AD_ACCOUNT).create_ad_video(params={
        AdVideo.Field.slideshow_spec: {
            'images_urls': [
                'https://www.downtownrochestermn.com/_files/images/sbs15tkssblue[1].png',
                'http://d3sdoylwcs36el.cloudfront.net/VEN-virtual-enterprise-network-business-opportunities-small-fish_id799929_size485.jpg',
                'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQmvDxaUoi9wsAm2H0qvdaCn8ISnkqOPSBDojx7WznZLoAMhvW_mjI7Pw'
            ]
        }
    })
    return JsonResponse(ad_video.export_all_data(), safe=False)
