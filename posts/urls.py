# posts/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # /board/ -> 게시판 포털 메인
    path('', views.index, name='board_index'),
    
    # /board/category/1/ -> 카테고리별 글 목록
    path('category/<int:category_id>/', views.category_post_list, name='post_list_by_category'),
    
    # /board/post/new/ -> 새 글 작성
    path('post/new/', views.post_create, name='post_create'),
    
    # /board/post/1/ -> 글 상세 보기
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    
    # /board/post/1/edit/ -> 글 수정
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    
    # /board/post/1/delete/ -> 글 삭제
    path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),
]