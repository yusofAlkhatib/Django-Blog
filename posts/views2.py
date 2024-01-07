
from django.shortcuts import render , redirect
from .models import Post 





def post_list(request):
    data = Post.objects.all() 
    return render(request,'posts_list.html',{'posts':data})


from django.views.generic import ListView , DetailView , CreateView , UpdateView , DeleteView

class PostList(ListView):
    model = Post 

class PostDetail(DetailView):
    model = Post

class PostCreate(CreateView):
    model = Post 
    fields = '__all__'
    success_url = '/blog/'

class PostEdit(UpdateView):
    model = Post 
    fields = '__all__'
    success_url = '/blog/'
    template_name = 'posts/edit_post.html'

class PostDelete(DeleteView) :
    model = Post
    success_url = '/blog/'