from django.shortcuts import render
from blog.models import Blog
from games.models import Review

# Create your views here.
def blog(request):
    blogs = Blog.objects.all()
    latest_blog = Blog.objects.order_by('-date')[:3]
    recent = Review.objects.order_by('-release_date')[:1]
    data = Review.objects.order_by('-review_int')
    context = {
        'blogs': blogs,
        'latest_blog': latest_blog,
        'recent': recent,
        'data': data,
    }
    return render(request, 'blog/categories.html', context)



