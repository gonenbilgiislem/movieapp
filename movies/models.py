from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
class Movie(models.Model):
    film_adi = models.CharField(max_length=100)
    aciklama = models.TextField()
    resim = models.TextField(max_length=100)
    anasayfa =  models.BooleanField(default=False)
    kayit_tarihi = models.DateTimeField(auto_now_add=True)