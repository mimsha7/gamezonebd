from django.shortcuts import render
from .models import Contact
from blog.models import Blog
# Create your views here.

def contact(request):
    latest_blog = Blog.objects.order_by('-date')[:3]
    context = {
        'latest_blog': latest_blog,
    }
    if request.method == 'POST':
        cnt = Contact(
            name=request.POST['name'],
            email=request.POST['email'],
            subject=request.POST['subject'],
            message=request.POST['message'],
        )
        cnt.save()
        return render(request, 'contact/contact.html')
    return render(request, 'contact/contact.html', context)



