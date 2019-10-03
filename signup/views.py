from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.
def home(request):
    if request.method == "POST":
        username = request.POST['name']
        password = request.POST['password']
        email = request.POST['email']
        if User.objects.filter(username = username).exists():
            messages.info(request,"Username Taken")
            return redirect('/signup')
        else:
            user = User.objects.create_user(username=username,password=password,email=email)
            user.save()
        return redirect('/')
    else:
        return render(request,'signin.html')
