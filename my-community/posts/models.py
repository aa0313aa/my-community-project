from django.db import models
from django.contrib.auth.models import User # 나중을 위해 미리 import

# 새로 추가된 '게시판 종류' 모델
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

# 기존 '게시글' 모델 수정
class Post(models.Model):
    # 어떤 카테고리에 속하는지 연결해주는 '꼬리표' (ForeignKey)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    # 기존 필드들은 그대로 둡니다.
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    # author 필드는 나중에 회원가입 기능과 연동할 때 추가할 예정입니다.
    # author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
