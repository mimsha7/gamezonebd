from django.urls import path
from django.conf.urls import url
from blog.views import blog, search

urlpatterns= [
    path('blog',blog,name='blog'),
    url(r'^results/$', search, name="search"),
]