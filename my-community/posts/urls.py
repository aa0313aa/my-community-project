from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('new/', views.post_create, name='post_create'),  # 글쓰기 URL 추가
    path('<int:pk>/', views.post_detail, name='post_detail'),
    path('<int:pk>/edit/', views.post_edit, name='post_edit'),  # 글 수정
    path('<int:pk>/delete/', views.post_delete, name='post_delete'),  # 글 삭제
]
