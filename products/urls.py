# products/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index'),  # 루트 URL의 순환 참조 방지
]