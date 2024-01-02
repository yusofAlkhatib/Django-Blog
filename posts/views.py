from django.shortcuts import render
from .models import Post 

# Create your views here.
def post_list(request):
    data = Post.objects.all() 
    return render(request,'posts_list.html',{'posts':data})