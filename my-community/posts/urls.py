from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # 대문 페이지
    path('category/<int:category_id>/', views.category_post_list, name='post_list_by_category'),  # 카테고리별 글 목록

    # 나머지 기존 주소들 (post_detail은 구분을 위해 post/를 앞에 붙여줍니다)
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_create, name='post_create'),  # 글쓰기 URL 추가
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),  # 글 수정 URL 추가
    path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),  # 글 삭제 URL 추가
]
