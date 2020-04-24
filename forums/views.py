from django.shortcuts import render,redirect
from .models import Forum
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from blog.models import Blog

def forum(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            forum = Forum(
                name=request.POST['user_name'],
                post=request.POST['post'],
                avatar=request.POST['avatar'],
            )
            forum.save()
            messages.success(request, 'Your Post Successfully Posted')
            return redirect('forum')
        else:
            messages.error(request,'If You Want to Post Some Things Then Login First')
            return redirect('login')

    else:
        member = User.objects.all()
        member_no = len(member)


        posts = Forum.objects.order_by('-date')
        total_post = len(posts)
        paginator = Paginator(posts,7)
        pages = request.GET.get('page')
        post_page = paginator.get_page(pages)
        latest_blog = Blog.objects.order_by('-date')[:3]
        context = {
            'posts':post_page,
            'member_no':member_no,
            'total_post':total_post,
            'latest_blog': latest_blog,
        }
        return render(request, 'forums/community.html',context)
