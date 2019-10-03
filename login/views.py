from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
# Create your views here.
def home(request):
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['password']
        user = auth.authenticate(username=name,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid Credentials")
            return redirect('/login')
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

