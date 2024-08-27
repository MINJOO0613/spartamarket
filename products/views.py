from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Comment
from .forms import ProductForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_http_methods
from django.http import HttpResponseRedirect
from django.db.models import Count
from datetime import timedelta, datetime


def index(request):
    sort_by = request.GET.get('sort', 'created')
    
    # Top_products = Product.objects.filter(category='Top')
    # Bottom_products = Product.objects.filter(category='Bottom')
    # Acc_products = Product.objects.filter(category='Acc')
    # Outer_products = Product.objects.filter(category='Outer')
    # Bag_products = Product.objects.filter(category='Bag')
    
    categories = ['Top', 'Bottom', 'Acc', 'Outer', 'Bag']
    categorized_products = {
        category: Product.objects.filter(category=category) for category in categories
    }
    
    if sort_by == 'likes':
        products = sorted(Product.objects.all(), key=lambda product: product.total_likes, reverse=True)
    else:
        products = Product.objects.all().order_by('-id')  # 기본적으로 생성순 정렬

    total_likes = sum(product.total_likes for product in Product.objects.all())
    latest_products = Product.objects.all().order_by('-id')[:4]
    popular_products = Product.objects.annotate(like_count=Count('like_users')).order_by('-like_count', '-created_at')[:4] # like_users의 수를 새고 like_count로 정렬 후 그 값이 같으면 created_at으로 정렬
    
    
    context = {
        'products':products,
        'total_likes':total_likes,
        'latest_products': latest_products,
        'popular_products': popular_products,
        # 'Top_products': Top_products,
        # 'Bottom_products': Bottom_products,
        # 'Acc_products': Acc_products,
        # 'Outer_products': Outer_products,
        # 'Bag_products': Bag_products,
        'categories':categories,
        'categorized_products': categorized_products,
    }
    return render(request, "products/index.html", context)


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    comment_form = CommentForm()
    comments = product.comments.all().order_by("-pk")
    # product.save()

    if product.author == request.user:
        # naive_dt = datetime.datetime(2024, 4, 11)
        # aware_dt = naive_dt.replace(tzinfo=datetime.timezone.utc)
        # time_difference = aware_dt - last_view_time 
        # last_view_time = product.last_view_time
        # now = datetime.now()
        # time_difference = now - last_view_time
        # if time_difference >= timedelta(days=1):
        #     # 24시간 이상 조회하지 않았음 -> 조회수 증가
            # product.views += 1
            # product.last_view_time = now
            # product.save()
        # else:
        #     # 24시간 이내에 조회했음 -> 추가 조회수 증가 방지
        pass
    else:
        product.views += 1
        product.save()


    context = {
        "product": product,
        "comment_form": comment_form,
        "comments": comments,
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
            form = ProductForm(request.POST, request .FILES, instance=product)
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
def comment_create(request, pk):
    product = get_object_or_404(Product, pk=pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.product = product
        comment.user = request.user
        comment.save()
        return redirect("products:product_detail", product.pk)


@require_POST
def comment_delete(request, pk, comment_pk):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, pk=comment_pk)
        if comment.user == request.user:
            comment.delete()
    return redirect("products:product_detail", pk)


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

    
def product_list_by_category(request, category):
    products = Product.objects.filter(category=category)

    # 모든 카테고리 가져오기
    categories = Product.objects.values_list('category', flat=True).distinct()
    
    sort_by = request.GET.get('sort', 'created')
    
    # Top_products = Product.objects.filter(category='Top')
    # Bottom_products = Product.objects.filter(category='Bottom')
    # Acc_products = Product.objects.filter(category='Acc')
    # Outer_products = Product.objects.filter(category='Outer')
    # Bag_products = Product.objects.filter(category='Bag')
    

    total_likes = sum(product.total_likes for product in Product.objects.all())
    latest_products = Product.objects.all().order_by('-id')[:4]
    popular_products = Product.objects.annotate(like_count=Count('like_users')).order_by('-like_count', '-created_at')[:4] # like_users의 수를 새고 like_count로 정렬 후 그 값이 같으면 created_at으로 정렬
    
    
    context = {
        'products': products,
        'categories': categories,
        'selected_category': category,
    }

    return render(request, 'products/product_list.html', context)
