from django.db import models
from django.conf import settings
# from datetime import datetime, timedelta
from django.utils import timezone
# from django.db.models import F

# Create your models here.
class Product(models.Model):
    
    CATEGORY_CHOICES = [
        ('Top', 'Top'),
        ('Bottom', 'Bottom'),
        ('Acc', 'Acc'),
        ('Outer', 'Outer'),
        ('Bag', 'Bag'),
    ]
    
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="images/", blank=True) #blank 너가 값을 넣지 않아도 유효성 검사 통과시켜줄게
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="products"
    )
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="liked_products")
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='Top')  # 기본값을 'Top'으로 설정
    price = models.IntegerField(default=0)
    views = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.title
    
    @property
    def total_likes(self):
        return self.like_users.count()
    

    def time_dif(self):
        time = timezone.now() - self.created_at
        day = time.days
        second = time.seconds
        if day > 0:
            if day < 7:
                print(day)
                return f'{day}일 전'
            elif day < 30:
                return f'{day//7}주 전'
            elif day < 365:
                return f'{day//30}달 전'
            else:
                return f'{day//365}년 전'
        elif second > 3599:
            return f'{second//3600}시간 전'
        elif second > 59:
            return f'{second//60}분 전'
        else:
            return f'{second}초 전'

    

class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name = "comments", blank=True, null=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="comments", blank=True, null=True
    )
    content = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.content