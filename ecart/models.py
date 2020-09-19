from django.db import models

# Create your models here.

class product(models.Model):
    category = models.CharField(max_length = 200)
    name = models.CharField(max_length = 200)
    newprice = models.IntegerField()
    oldprice = models.IntegerField()
    image = models.CharField(max_length = 2000)


