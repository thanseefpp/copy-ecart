from .models import product
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control

# Create your views here.

def index(request):
    productitems= product.objects.all()
    return render(request,'index.html',{'productitems':productitems})

def login(request):
    return render(request, 'login.html')

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def adminhome(request):
    if request.session.has_key('username'):
        username = request.session['username']
        return render(request, 'adminhome.html', {"username" : username})
    else:
        return render(request, 'adminlogin.html', {})


def register(request):
    return render(request,'register.html')

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def adminout(request):
    request.session.flush()
    return redirect(adminlogin)


def adminlogin(request):
    us = User.objects.all()
    if request.session.has_key('username'):
        username = request.session['username']
        return render(request, 'adminhome.html')

    elif request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']

        if username == 'thanseef' and password == '1234':
            request.session['username'] = username
            return render(request, 'adminhome.html')

        else:
            messages.error(request, '😢 Wrong username/password!')
            return redirect(adminlogin)
    else:
        return render(request,'adminlogin.html')