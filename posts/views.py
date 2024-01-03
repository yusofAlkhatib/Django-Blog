from django.shortcuts import render
from .models import Post 
from .forms import PostForm 

# Create your views here.
def post_list(request):
    data = Post.objects.all() 
    return render(request,'posts_list.html',{'posts':data})


def post_detail(request,id):
    data = Post.objects.get(id=id)
    return render(request,'post_detail.html',{'post':data})


def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()

    else:
        form = PostForm()


    return render(request,'new_post.html',{'form':form})