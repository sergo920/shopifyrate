import os
from django.conf import settings
from django.shortcuts import render
from shopify_auth.decorators import login_required
from django.template.loader import get_template
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.http import HttpResponse


@login_required
def index(request):
    path = static('build/index.html')
    with open(path) as f:
        return HttpResponse(f.read())

    return HttpResponse(url)
    return render(request, get_template('index.html'))
