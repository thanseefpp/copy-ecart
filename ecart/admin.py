from django.contrib import admin
from .models import product
# Register your models here.

class productadmin(admin.ModelAdmin):
    list_display = ('category','name','newprice','oldprice')

admin.site.register(product)
