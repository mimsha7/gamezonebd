from django.shortcuts import render
from games.models import Review
from blog.models import Blog
# Create your views here.
def home(request):
        blogs = Blog.objects.all()
        recent = Review.objects.order_by('-release_date')[:4]
        data = Review.objects.order_by('-review_int')
        latest_blog = Blog.objects.order_by('-date')[:3]
        context = {
              'recent': recent,
              'latest_blog': latest_blog,
              'blogs': blogs,
               'data': data,
        }
        return render(request,'home/index.html', context)
