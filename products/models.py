from django.db import models
from django.conf import settings


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="images/", blank=True) #blank 너가 값을 넣지 않아도 유효성 검사 통과시켜줄게
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="products"
    )
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="Like_products")

    def __str__(self):
        return self.title
    
    @property
    def total_likes(self):
        return self.like_users.count()
    

class Comment(models.Model):
    article = models.ForeignKey(Product, on_delete=models.CASCADE, related_name = "comments")
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content
    
    
# class Watched(models.Model):
#     watched = models.PositiveIntegerField(default=0)

#     def __str__(self):
#         return str(self.watched)
