from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Category
from .forms import PostForm
from django.contrib.auth.decorators import login_required

# 포털 메인 페이지를 위한 View
def index(request):
    categories = Category.objects.all()
    category_post_list = {}
    for category in categories:
        # 각 카테고리별 최신 글 5개를 가져옵니다.
        posts = Post.objects.filter(category=category).order_by('-created_at')[:5]
        category_post_list[category] = posts

    context = {
        'category_post_list': category_post_list,
    }
    return render(request, 'posts/index.html', context)

# 카테고리별 전체 글 목록을 보여주는 View
def category_post_list(request, category_id):
    target_category = get_object_or_404(Category, id=category_id)
    posts = Post.objects.filter(category=target_category).order_by('-created_at')
    categories = Category.objects.all()

    context = {
        'target_category': target_category,
        'posts': posts,
        'categories': categories,
    }
    return render(request, 'posts/category_list.html', context)

# 게시글 상세
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'posts/post_detail.html', {'post': post})

# 글쓰기
@login_required(login_url='login')
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'posts/post_form.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'posts/post_form.html', {'form': form, 'is_edit': True})

def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')
    return render(request, 'posts/post_confirm_delete.html', {'post': post})
