from django.shortcuts import render,get_object_or_404,redirect
from .models import Post
from .forms import formulaire


def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blog/post_list.html', {'posts': posts})

def ajout_post(request):
	if request.method == "POST":
		form=formulaire(request.POST)
		if form.is_valid():
			form.save()

			return redirect('post_list')
	else:
		form=formulaire()
	return render(request,'blog/forms.html',{'form':form})


def post_detail(request,id):
    post=get_object_or_404(Post,id=id)
    print("#==="*40)
    print(post)
    print("#==="*40)
    return render(request, 'blog/post_detail.html', {'post': post})


def index(request):
    return render(request, 'blog/index.html')

def blog(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blog/blog.html', {'posts': posts})


# Create your views here.
