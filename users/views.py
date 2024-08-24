from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
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

    form = None

    if user.username == request.user:
        if request.method == "POST":
            form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
            if form.is_valid():
                form.save()
                return redirect('profile', username=request.user.username)
        else:
            form = ProfileForm(instance=request.user.profile)

    return render(request, 'users/edit_profile.html', {'form': form})
    
    # if request.method == 'POST':
    #     form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('profile', username=request.user.username)
    # else:
    #     form = ProfileForm(instance=request.user.profile)
    # return render(request, 'users/edit_profile.html', {'form': form})
