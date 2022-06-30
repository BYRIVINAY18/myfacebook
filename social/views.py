from django.shortcuts import render,redirect

from django.contrib.auth import authenticate,login,logout

from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required

from .models import userpost

# Create your views here.

def index(request):

    if request.user.is_anonymous:
        if request.method=='POST':
            username = request.POST['username']
            pwd      = request.POST['password']
            user     = authenticate(username=username,password=pwd)
            if user is not None:
                login(request,user)
                return redirect('home')
    else:
        return redirect('home')
    return render(request,'index.html')

@login_required(login_url='index')
def home(request):
    return render(request,'home.html')

@login_required(login_url='index')
def profile(request):
    return render(request,'profile.html')

def signout(request):
    logout(request)
    return redirect('index')\

def register(request):
    if request.method=='POST':
        username = request.POST['username']
        pwd = request.POST['password']
        user = User.objects.create(username=username)
        user.set_password(pwd)
        user.save()
        return redirect('index')
    return redirect('index')

def update(request):
    if request.method=='POST':
        userprofile = request.user.userprofile
        status = request.POST['status']
        location = request.POST['location']
        if len(status)==0 and len(location)>0:
            userprofile.loc = location
        elif len(status)>0 and len(location)==0:
            userprofile.bio = status
        elif len(status)>0 and len(location)>0:
            userprofile.loc = location
            userprofile.bio = status
        userprofile.save()
    return redirect('profile')

def create_post(request):
    if request.method=='POST':
        post = request.POST['content']

        userpost=userpost.objects.create(user=request.user,post=post)
        userpost.save()
    return redirect('home')




