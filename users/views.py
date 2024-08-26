from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from products.models import Product
from .models import Profile, Follow
from .forms import ProfileForm
from django.views.decorators.http import require_POST, require_http_methods


@login_required
def profile_view(request, username):
    user = get_object_or_404(get_user_model(), username=username)
    return render(request, 'users/profile.html', {'user': user})


@login_required
@require_http_methods(["GET", "POST"])
def edit_profile(request, username):
    user = get_object_or_404(get_user_model(), username=username)

    if user != request.user:
        return redirect("index")

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('users:profile', username=request.user.username)
    else:
        form = ProfileForm(instance=request.user.profile)
    
    return render(request, 'users/edit_profile.html', {'form': form})


@login_required
def profile_view(request, username):
    user = get_object_or_404(get_user_model(), username=username)
    # is_following을 following_set으로 수정하여 제대로 참조
    is_following = Follow.objects.filter(follower=request.user.profile, followed=user.profile).exists()
    products = Product.objects.filter(author=user)
    
    if request.method == 'POST':
        tab = request.POST.get('tab')
        if tab == 'posts':
            products = Product.objects.filter(author=user)
        elif tab == 'likes':
            products = user.liked_products.all()
        else:
            products = Product.objects.filter(author=user)
    else:
        products = Product.objects.filter(author=user)
    
    return render(request, 'users/profile.html', {
        'user': user,
        'is_following': is_following,
        'products': products,
    })

@login_required
def follow_user(request, username):
    user_to_follow = get_object_or_404(get_user_model(), username=username)
    user_profile = request.user.profile

    if user_profile != user_to_follow.profile:
        Follow.objects.get_or_create(follower=user_profile, followed=user_to_follow.profile)

    return redirect('users:profile', username=username)

@login_required
def unfollow_user(request, username):
    user_to_unfollow = get_object_or_404(get_user_model(), username=username)
    user_profile = request.user.profile

    follow = Follow.objects.filter(follower=user_profile, followed=user_to_unfollow.profile)
    if follow.exists():
        follow.delete()

    return redirect('users:profile', username=username)