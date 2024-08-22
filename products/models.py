from django.db import models


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    # author = models.ForeignKey()   #게시물 직성자를 확인하는 key
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="images/", blank=True) #blank 너가 값을 넣지 않아도 유효성 검사 통과시켜줄게


    def __str__(self):
        return self.title
    

class Comment(models.Model):
    article = models.ForeignKey(Product, on_delete=models.CASCADE, related_name = "comments")
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content