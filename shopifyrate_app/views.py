from django.shortcuts import render
from shopify_auth.decorators import login_required


@login_required
def index(request, *args, **kwargs):
    return render(request, "index.html")

