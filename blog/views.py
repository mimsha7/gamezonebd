from django.shortcuts import render
from blog.models import Blog
from games.models import Review
from gamewarrior.config import pagination
from django.db.models import Q

# Create your views here.
def blog(request):
    blogs = Blog.objects.all()
    latest_blog = Blog.objects.order_by('-date')[:3]
    recent = Review.objects.order_by('-release_date')[:1]
    data = Review.objects.order_by('-review_int')

    pages = pagination(request, blogs, 6)
    context = {
        'latest_blog': latest_blog,
        'recent': recent,
        'data': data,
        'blogs': pages[0],
        'page_range': pages[1]
    }
    return render(request, 'blog/categories.html', context)


def search(request):
    latest_blog = Blog.objects.order_by('-date')[:3]
    recent = Review.objects.order_by('-release_date')[:1]
    data = Review.objects.order_by('-review_int')

    query = request.GET.get('src')
    if query:
        results = Blog.objects.filter(Q(name__icontains=query) | Q(category__category_name__icontains=query))
    else:
        results = Blog.objects.order_by('-date')

    pages = pagination(request, results, num=5)

    context = {
        'blogs': pages[0],
        'page_range': pages[1],
        'query':  query,
        'latest_blog': latest_blog,
        'recent': recent,
        'data': data,
    }
    return render(request, 'blog/categories.html', context)
