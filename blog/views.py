from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm
from datetime import datetime
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import NewUserForm
from django.contrib.auth.forms import AuthenticationForm


def post_list(request, itag=None):
    if itag is not None and itag != "all posts":
        posts = Post.objects.filter(tag=itag)
    else:
        posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_filter(request, inputtag):
    return post_list(request=request, itag=inputtag)


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def edit_user(request):
    if request.user.is_authenticated:
        user = request.user
        if request.method == 'POST':
            form = NewUserForm(request.POST, instance=user)
            if form.is_valid():
                form.save()
                login(request, user)
                messages.success(request, 'Account updated')
            return redirect('post_list')
        else:
            form = NewUserForm(instance=user)
            return render(request, 'blog/edit_user.html', context={"register_form": form})
    else:
        return redirect("post_list")


def edit_post(request, id):
    post = Post.objects.get(pk=id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('post_detail', post.pk)
    else:
        form = PostForm(instance=post, user=request.user)
    return render(request, 'blog/edit_post.html', {'post_form': form})


def create_post(request):
    if request.method == "POST":
        post_form = PostForm(request.POST, request.FILES, user=request.user)
        if post_form.is_valid():
            post_form.save()
            messages.success(request, ('Your post was successfully added!'))
        else:
            pass
        return redirect("post_list")
    post_form = PostForm(user=request.user)
    return render(request=request, template_name="blog/create_post.html", context={'post_form': post_form})


def delete_post(request, id=None):
    Post.objects.filter(pk=id).delete()
    return redirect("post_list")


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("post_list")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="blog/register.html", context={"register_form": form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('post_list')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="blog/login.html",
                  context={"login_form": form})


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("post_list")


def timeout_request(request):
    return render(request, 'error_out.html')


def error_404_view(request, exception):
    return render(request, '404.html')
