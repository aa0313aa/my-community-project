from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
# LoginView, LogoutView는 urls.py에서 바로 사용하므로 import 불필요

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list') # 회원가입 성공 시, 게시판 목록 페이지로 이동
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})
# 로그인/로그아웃은 Django 기본 뷰 사용 (urls.py에서 처리)
