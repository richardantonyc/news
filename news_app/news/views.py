from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as dj_login
from django.contrib.auth import logout as dj_logout
from django.contrib import messages
from .forms import RegisterForm,LoginForm
from django.views.generic import ListView
#from .models import news
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse



# Create your views here.

def home(request):
    return render(request,'home.html')

def search(request):
    if request.method == "GET":
        #news=request.GET.get('search')
    #else:
        return render(request,'search.html',{})


def register(request):
    if request.method == 'GET':
        form=RegisterForm()
        return render(request,'register.html',{'form':form})
    
    if request.method == 'POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.username=user.username.lower()
            user.save()
            dj_login(request,user)
            messages.success(request,f'You have Registered Successfully')
            return redirect('home')
        else:
            messages.error(request,f'Retry or Try again later')
            return render(request,'register.html',{'form':form})
        
    #return render(request,'login.html')
def login(request):
    
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('illusion')
        
        form=LoginForm()
        return render(request,'login.html',{'form':form})
    
    elif request.method == 'POST':
        form=LoginForm(request.POST)

        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(request,username=username,password=password)
            if user:
                dj_login(request,user)
                messages.success(request,f'Hi {username},welcome back!')
                return redirect('home')
        
        messages.error(request,f'Invalid username or password')
        return render(request,'login.html',{'form':form})
    #return render(request,'login.html')

def logout(request):
    dj_logout(request)
    messages.success(request,f'you have been logged out.')
    return redirect('home')

def about(request):
    return render(request,'about.html')

def newsletter(request):
    return render(request,'newsletter.html')

def event(request):
    return render(request,'news/event.html')
 
def place(request):
    return render(request,'news/place.html')

def color(request):
    return render(request,'news/color.html')

def illusion(request):
    return render(request,'news/illusion.html')
