from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    aciklama = models.TextField()
    resim = models.ImageField(upload_to='images/')
    category = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title