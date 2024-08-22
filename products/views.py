from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_http_methods
from .forms import ProductForm, CommentForm
from .models import Product

# Create your views here.
def index(request):
    products = Product.objects.all().order_by('-pk')  #나중에 정렬 바꿔
    context = {"products":products}
    return render(request, "products/index.html", context)

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    # comment_form은 나중에 할고임
    context = {
        "product":product,
    }
    return render(request, "products/product_detail.html", context)


@login_required
def create(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save()
            return redirect("products:product_detail", product.pk)
    else:
        form = ProductForm()

    context = {"form":form}
    return render(request, "products/create.html", context)


def update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            product = form.save()
            return redirect("products:product_detail", product.pk)
    else:
        form = ProductForm(instance=product)
    context = {
        "form": form,
        "product": product,
    }
    return render(request, "products/update.html", context)


@require_POST
def delete(request, pk):
    if request.user.is_authenticated:
        product = get_object_or_404(Product, pk=pk)
        product.delete()
    return redirect("index")