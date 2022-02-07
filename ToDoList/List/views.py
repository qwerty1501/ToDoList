from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm
from .models import Post
from .forms import PostForm


def index(request):
    post_list = Post.objects.filter(author__username=request.user)
    if request.method == "POST":
        form = PostForm(request.POST)
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        return redirect('/')

    else:
        form = PostForm()
    return render(request, 'List/index.html', {'post_list': post_list, 'form': form})


@login_required()
def author(request, username):
    author_list = Post.objects.filter(author__username=username)
    return render(request, 'List/author.html', {'author_list': author_list, 'username': username})


@login_required()
def detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'List/detail.html', {'post': post})


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username}, аккаунт успешно зарегестрирован!')
            return redirect('/')
    else:
        form = UserRegisterForm()

    return render(request, 'List/register.html', {'form': form})


@login_required()
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('/', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'List/post_edit.html', {'form': form})


@login_required()
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('/')


@login_required()
def post_delete_all(request):
    post = Post.objects.all()
    post.delete()
    return redirect('/')


@login_required()
def post_done(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.make_it_done()
    post.save()
    return redirect('/')


@login_required()
def post_not_done(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.make_it_undone()
    post.save()
    return redirect('/')