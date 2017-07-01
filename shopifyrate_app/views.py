import os
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from shopify_auth.decorators import login_required


@login_required
def index(request):
    path = os.path.join(settings.REACT_APP_DIR, 'build', 'index.html')
    return render(request, path)
    with open(os.path.join(settings.REACT_APP_DIR, 'build', 'index.html')) as f:
        return HttpResponse(f.read())
