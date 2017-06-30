import os
import logging
from django.conf import settings
from django.http import HttpResponse
from shopify_auth.decorators import login_required
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.contrib.staticfiles.storage import staticfiles_storage



@login_required
def index(request):
    path = os.path.join(settings.BASE_DIR, 'frontend', 'build', 'index.html')
    try:
        with open(path) as f:
            return HttpResponse(f.read())
    except FileNotFoundError as e:
        logging.exception('Production build of app not found')
        return HttpResponse(
            path,

            status=501,
        )
