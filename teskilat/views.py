from django.shortcuts import render
from .models import Il_Baskanligi , Il
# Create your views here.
def citiesPage(request):
    cities = Il.objects.all()
    data = { 
        'cities' : cities
    }
    return render(request , 'cities.html' , data)

def cityPage(request , city):
    management_of_city = Il_Baskanligi.objects.filter(Yonetici_Il = Il.objects.get(Sehir_Ismi = city))
    management_of_city = management_of_city.order_by('Yonetici_Durumu')
    data = {
        'management' : management_of_city
    }
    return render(request , 'city.html' , data)