from django.shortcuts import render
from .models import Review
from blog.models import Blog
# Create your views here.

def games(request):
    data = Review.objects.order_by('-review_int')
    recent = Review.objects.order_by('-release_date')[:4]
    latest_blog = Blog.objects.order_by('-date')[:3]
    context = {
        'data': data,
        'recent': recent,
        'latest_blog': latest_blog,
    }
    return render(request,'games/review.html', context)

def single_review(request,game_id):
    single = Review.objects.filter(pk=game_id)
    latest_blog = Blog.objects.order_by('-date')[:3]
    context = {
        'single': single,
        'latest_blog': latest_blog,
    }
    return render(request, 'games/single_review.html', context)