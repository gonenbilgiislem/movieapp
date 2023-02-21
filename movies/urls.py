from django.urls import path
from . import views
# http://127.0.0.1:8000/
# http://127.0.0.1:8000/movies
# http://127.0.0.1:8000/3
# http://127.0.0.1:8000/walking-dead

urlpatterns = [
    path('', views.home, name='index'),
    path('home', views.home, name='index'),
    path('movies', views.movies, name='movies')
]
