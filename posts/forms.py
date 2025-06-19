from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Post, Category

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['category', 'title', 'content', 'image', 'file']
        widgets = {
            'content': SummernoteWidget(),
        }
        # 이 labels 설정을 추가하여 필드 이름을 한글로 변경합니다.
        labels = {
            'category': '카테고리',
            'title': '제목',
            'content': '내용',
            'image': '이미지 첨부',
            'file': '파일 첨부',
        }