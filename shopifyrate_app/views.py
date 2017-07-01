import os
from django.conf import settings
from django.shortcuts import render
from shopify_auth.decorators import login_required
from django.template.loader import get_template
from django.contrib.staticfiles.storage import staticfiles_storage
from django.http import HttpResponse, JsonResponse


@login_required
def index(request):
    dire = []
    list_dirs = os.walk(settings.BASE_DIR)
    for root, dirs, files in list_dirs:
        for d in dirs:
            dire.append(os.path.join(root, d))


    return JsonResponse(dire, safe=False)

    # path = staticfiles_storage.url('build/index.html')
    with open('/app/static/build/index.html') as f:
        return HttpResponse(f.read())

    return HttpResponse(url)
    return render(request, get_template('index.html'))
