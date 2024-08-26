from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_http_methods
from django.http import HttpResponse
from datetime import datetime, timedelta


def index(request):
    # products = Product.objects.all().order_by('-pk')  # 나중에 정렬 바꿔
    # context = {
    #     "products": products
    # }
    # return render(request, "products/index.html", context)
    sort_by = request.GET.get('sort', 'created')
    
    if sort_by == 'likes':
        products = sorted(Product.objects.all(), key=lambda product: product.total_likes, reverse=True)
    else:
        products = Product.objects.all().order_by('-id')  # 기본적으로 생성순 정렬

    total_likes = sum(product.total_likes for product in Product.objects.all())
    context = {
        'total_likes': total_likes,
        "products": products
    }

    return render(request, "products/index.html", context)


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    # comment_form은 나중에 할고임

    cookie_name = f'product_'
    if cookie_name not in request.COOKIES:
        expire_date, now = datetime.now(), datetime.now()
        expire_date += timedelta(days=1)
        expire_date = expire_date.replace(hour=0, minute=0, second=0, microsecond=0)
        expire_date -= now
        max_age = expire_date.total_seconds()

        response =  render(request, 'detail.html' ,{'data' : product_detail, 'comments' : comments, 're_comments' : re_comments, 'form':form})


        if f'_{id}_' not in cookie_value:
            cookie_value += f'{id}_'
            response.set_cookie('hitblog', value=cookie_value, max_age=max_age, httponly=True)
            product_detail.hits += 1
            product_detail.save()
        return response

    context = {
        "product": product,
        # 'watched': watched,
        }
    return render(request, "products/product_detail.html", context)


@login_required
def create(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.author = request.user
            product.save()
            return redirect("products:product_detail", product.pk)
    else:
        form = ProductForm()

    context = {"form": form}
    return render(request, "products/create.html", context)


@login_required
@require_http_methods(["GET", "POST"])
def update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if product.author == request.user:  # 게시물을 등록한 유저가 일치한지 확인
        if request.method == "POST":
            form = ProductForm(request.POST, instance=product)
            if form.is_valid():
                product = form.save()
                return redirect("products:product_detail", product.pk)
        else:
            form = ProductForm(instance=product)

    else:
        return redirect("products:product_detail", product.pk)

    context = {
        "form": form,
        "product": product,
    }
    return render(request, "products/update.html", context)


@require_POST
def delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if product.author == request.user:
        product.delete()
    return redirect("index")


@require_POST
def like(request, pk):
    if request.user.is_authenticated:
        product = get_object_or_404(Product, pk=pk)
        if product.like_users.filter(pk=request.user.pk).exists():
            product.like_users.remove(request.user)
        else:
            product.like_users.add(request.user)
        return redirect(request.META.get('HTTP_REFERER', 'products:index'))
    return redirect("accounts:login")