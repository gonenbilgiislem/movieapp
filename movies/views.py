from django.shortcuts import render

kategoriler = ["macera", "romantik", "dram"]
# Create your views here.

def home(request):
    data = {
    "kategori": kategoriler
    }
    return render(
        request, 'index.html',data
    )

def movies(request):
    return render(request, 'movies.html',
                  {'title': 'Filmler',
                   'message': 'Filmler Sayfasına Hoş Geldiniz.'}
                  )
