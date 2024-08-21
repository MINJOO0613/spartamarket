from django.urls import path
from . import views


#다음 분 crud 만드세요^~^
app_name = "products"
urlpatterns = [
    path("index/", views.index, name="index"),
    
]
