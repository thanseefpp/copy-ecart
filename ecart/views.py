from django.shortcuts import render
from .models import product

# Create your views here.

def index(request):
    productitems= product.objects.all()
    return render(request,'index.html',{'productitems':productitems})

def login(request):
    return render(request, 'login.html')

