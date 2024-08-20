from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_http_methods

# Create your views here.
def index(request):
    return render(request, "products/index.html")