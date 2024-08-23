from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_http_methods