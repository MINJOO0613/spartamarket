from django.urls import path
# from .views import popup_view
from . import views


app_name = "products"
urlpatterns = [
    path("index/", views.index, name="index"),
    path('create/', views.create, name='create'),
    path("<int:pk>/", views.product_detail, name="product_detail"),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/update/', views.update, name='update')
    # path('popup/', popup_view, name='popup_view'),
]

#나도 기여할래..