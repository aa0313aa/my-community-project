from django.shortcuts import render, get_object_or_404
from .models import Category, Post
from .forms import PostForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def index(request):
    categories = Category.objects.all()
    category_post_list = {}
    for category in categories:
        posts_in_category = Post.objects.filter(category=category).order_by('-created_at')[:5]
        category_post_list[category] = posts_in_category
    return render(request, 'posts/index.html', {
        'category_post_list': category_post_list,
    })

def category_post_list(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    posts = Post.objects.filter(category=category).order_by('-created_at')
    categories = Category.objects.all()
    return render(request, 'posts/category_list.html', {
        'category': category,
        'posts': posts,
        'categories': categories,
    })

@login_required(login_url='login')
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return HttpResponseRedirect(reverse('post_detail', args=[post.pk]))
    else:
        form = PostForm()
    return render(request, 'posts/post_form.html', {'form': form})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'posts/post_detail.html', {'post': post})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('post_detail', args=[post.pk]))
    else:
        form = PostForm(instance=post)
    return render(request, 'posts/post_form.html', {'form': form, 'post': post})

def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return HttpResponseRedirect(reverse('board_index'))
    return render(request, 'posts/post_confirm_delete.html', {'post': post})