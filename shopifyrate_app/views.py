import os
import logging
from django.conf import settings
from django.http import HttpResponse
from shopify_auth.decorators import login_required


@login_required
def index(request):
    path = os.path.join(settings.REACT_APP_DIR, 'build', 'index.html')
    try:
        with open(path) as f:
            return HttpResponse(f.read())
    except FileNotFoundError as e:
        logging.exception('Production build of app not found')
        return HttpResponse(
            [os.path.join(settings.ROOT_PATH, o) for o in os.listdir(settings.ROOT_PATH)
             if os.path.isdir(os.path.join(settings.ROOT_PATH, o))],

            status=501,
        )
