from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User



def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request, 'You are now logged in')
            return render(request,'home/index.html')
        else:
            messages.error(request, 'Invalid user')
            return redirect('login')
    else:
        return render(request,'account/login.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request,'That username is taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,'That email is being used')
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
                    user.save()

                    messages.success(request,'You are now registered and can log in')
                    return redirect('login')
        else:
            messages.error(request, 'Password do not match')
            return redirect('register')
    else:
        return render(request,'account/register.html')


def logout(request):
    if User.is_authenticated:
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return render(request, 'home/index.html')




