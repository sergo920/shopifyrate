import os
import logging
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from shopify_auth.decorators import login_required


@login_required
def index(request):
    return render(request, 'index.html')
    try:
        with open(os.path.join(settings.REACT_APP_DIR, 'build', 'index.html')) as f:
            return JsonResponse({'dfsdfsf': 'fdsfdsfdsf'}, safe=False)
            return HttpResponse(f.read())
    except FileNotFoundError:
        logging.exception('Production build of app not found')
        return HttpResponse(
            """
            This URL is only used when you have built the production
            version of the app. Visit http://localhost:3000/ instead, or
            run `yarn run build` to test the production version.
            """,
            status=501,
        )
