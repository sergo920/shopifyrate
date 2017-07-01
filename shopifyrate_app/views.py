from django.shortcuts import render
from shopify_auth.decorators import login_required
from django.template.loader import get_template


@login_required
def index(request):
    return render(request, get_template('index.html'))
