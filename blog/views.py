from django.shortcuts import render
from .models import Post

posts = [
    {
        'author': "Benedict Gutierrez",
        'title': "Blog Post 1",
        'content': "First post content",
        'date_posted': "100BC",
    },
    {
        'author': "bdgdek",
        'title': "Blog Post 2",
        'content': "Second post content",
        'date_posted': "100BC",
    }
]

def home(request):
    context = {
        "posts": Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {"title": "About"})
