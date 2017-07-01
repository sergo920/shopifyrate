import os
from django.conf import settings
from django.shortcuts import render
from shopify_auth.decorators import login_required
from django.http import HttpResponse, JsonResponse


@login_required
def index(request):
    return render(request, 'index.html')
    with open('/app/frontend/build/index.html') as f:
        return HttpResponse(f.read())

    # return HttpResponse(url)
    # return render(request, get_template('index.html'))
