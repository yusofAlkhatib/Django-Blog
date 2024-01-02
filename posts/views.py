from django.shortcuts import render
from .models import Post 

# Create your views here.
def post_list(request):
    data = Post.objects.all() 
    return render(request,'posts_list.html',{'posts':data})


def post_detail(request,id):
    data = post.objects.get(id=id)
    return render(request,'posts_detail.html',{'post':data})