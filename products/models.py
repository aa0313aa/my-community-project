from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/', blank=True, null=True)

class Post(models.Model):
    title = models.CharField(max_length=200)      # 글 제목
    content = models.TextField()                  # 글 내용
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products_posts_written')  # 글쓴이
    created_at = models.DateTimeField(auto_now_add=True)        # 작성 시간
