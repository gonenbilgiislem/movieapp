from django.shortcuts import render

kategori_listele = ["macera", "romantik", "dram", "komedi"]
# Create your views here.
film_liste = [
    {
        "film_adi": "film 1",
        "aciklama": "film 1 açıklama",
        "resim": "1.jpeg",
        "anasayfa": True
    },
    {
        "film_adi": "film 2",
        "aciklama": "film 2 açıklama",
        "resim": "2.jpeg",
"anasayfa": True
    },
    {
        "film_adi": "film 3",
        "aciklama": "film 3 açıklama",
        "resim": "3.jpeg",
        "anasayfa": False
    },
    {
        "film_adi": "film 4",
        "aciklama": "film 4 açıklama",
        "resim": "4.jpeg",
        "anasayfa": False
    }
]
def home(request):
    data = {
    "kategoriler": kategori_listele,
    "filmler": film_liste,
    "title": "Ana Sayfa"
    }
    return render(
        request, 'index.html',data)

def movies(request):

    data = {
    "kategoriler": kategori_listele,
    "filmler": film_liste,
    "title"  : "Filmler"
    }
    return render(request,"movies.html" ,data)
