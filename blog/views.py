from django.shortcuts import render
from .models import Post
from django.http import HttpResponse

# def home(request):
#     return HttpResponse('<h1>Blog Home</h1>')

# posts=[{
#         'author': 'CoreyMS',
#         'title': 'Blog Post 1',
#         'content': 'First post content',
#         'date_posted': 'August 27, 2018'
#     },
#     {
#         'author': 'Jane Doe',
#         'title': 'Blog Post 2',
#         'content': 'Second post content',
#         'date_posted': 'August 28, 2018'
#     }
# ]

def home(request):
    context={
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html',context)

# def about(request):
#     return render(request, 'blog/about.html')

def about(request):
    return render(request, 'blog/about.html',{'title': 'About'})
