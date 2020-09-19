from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,),
    path('login',views.login,name='login'),
    path('adminhome',views.adminhome,name='adminhome'),
    path('register',views.register,name='register'),
    path('adminlogin',views.adminlogin,name='adminlogin'),
    path('adminout',views.adminout, name='adminout'),
]