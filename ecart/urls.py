from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,),
    path('login/',views.login,name='login'),
    path('register',views.register,name='register'),
    path('admin/',views.adminlogin,name='adminlogin'),
    path('admin/adminout',views.adminout),
    path('logout',views.logout),
    path('product',views.product,name='product')
     # path('adminhome',views.adminhome,name='adminhome'),
]