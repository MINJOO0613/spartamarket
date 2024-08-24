from django.urls import path
from . import views


app_name = "users"
urlpatterns = [
    path('profile/<str:username>/', views.profile_view, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
]