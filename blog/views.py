from django.shortcuts import render,get_object_or_404
from .models import Post


def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request,id):
    post=get_object_or_404(Post,id=id)
    print("#==="*40)
    print(post)
    print("#==="*40)
    return render(request, 'blog/post_detail.html', {'post': post})


def index(request):
    return render(request, 'blog/index.html')

def blog(request):
    return render(request, 'blog/blog.html')


# Create your views here.
