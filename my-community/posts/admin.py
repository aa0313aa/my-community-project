from django.contrib import admin
from .models import Post # models.py 파일에서 Post 모델을 가져옵니다.

# Register your models here.
admin.site.register(Post) # 관리자 페이지에 Post 모델을 등록합니다.
