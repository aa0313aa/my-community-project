from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['category', 'title', 'content'] # 'category'를 fields 리스트의 맨 앞에 추가
        widgets = {
            'content': SummernoteWidget(), # content 필드에 Summernote 에디터 적용
        }
