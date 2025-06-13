from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        widgets = {
            'content': SummernoteWidget(), # content 필드에 Summernote 에디터 적용
        }
