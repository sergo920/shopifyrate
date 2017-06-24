from django.shortcuts import render
from shopify_auth.decorators import login_required


@login_required
def index(request):
    return render(request, 'index.html', context={'user_email': request.user.email})

