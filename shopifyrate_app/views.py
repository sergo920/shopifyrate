import os
import logging
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from shopify_auth.decorators import login_required


@login_required
def index(request):
    # return render(request, 'index.html')
    path = os.path.join(settings.REACT_APP_DIR, 'build', 'index.html')
    try:
        print('before read index')
        with open(path) as f:
            # return JsonResponse({'dfsdfsf': 'fdsfdsfdsf'}, safe=False)
            print('trying read index')
            return HttpResponse(f.read())
    except FileNotFoundError as e:
        logging.exception('Production build of app not found')
        return HttpResponse(
            str(e) + '  ######' + path,
            status=501,
        )
