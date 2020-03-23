from django.shortcuts import render
from .models import Blog
# Create your views here.

def list(request):
    data = {'Blogs': Blog.objects.all().order_by('-date')}
    return render(request, 'blog/blog.html', data)

def post(request, id):
    post = Blog.objects.get(id=id)
    return render(request, 'blog/post.html', {'post': post})
