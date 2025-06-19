from django.urls import path
from django.contrib.auth import views as auth_views # Django의 내장 auth 앱의 view들을 가져옴
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='post_list'), name='logout'),  # next_page 지정
]
