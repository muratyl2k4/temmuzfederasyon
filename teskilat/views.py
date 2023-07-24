from django.shortcuts import render
from .models import *
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
def citiesPage(request):
    cities = Il.objects.all()
    data = { 
        'cities' : cities
    }
    return render(request , 'cities.html' , data)

def cityPage(request , city):
    management_of_city = Il_Baskanligi.objects.filter(Yonetici_Il = Il.objects.get(Sehir_Ismi = city))
    youngers_of_city = Il_Genclik_Kollari.objects.filter(Yonetici_Il = Il.objects.get(Sehir_Ismi = city))
    womans_of_city = Il_Kadin_Kollari.objects.filter(Yonetici_Il = Il.objects.get(Sehir_Ismi = city))
    districts = Ilce.objects.filter(Ilce_Sehir = Il.objects.get(Sehir_Ismi = city))

    management_of_city = management_of_city.order_by('Yonetici_Durumu')
    data = {
        'management' : management_of_city, 
        'youngers' : youngers_of_city, 
        'womans' : womans_of_city, 
        'city' : city ,
        'districts' : districts
    }
    return render(request , 'city.html' , data)

def districtPage(request , city , district): 
    district = Ilce.objects.get(Ilce_Sehir = Il.objects.get(Sehir_Ismi = city) , Ilce_Ismi = district)

    district_management = Ilce_Baskanligi.objects.filter(Yonetici_Il = district).order_by(
            'Yonetici_Durumu'
    )
    district_womans = Ilce_Kadin_Kollari.objects.filter(Yonetici_Il = district).order_by(
            'Yonetici_Durumu'
    )
    district_youngers = Ilce_Genclik_Kollari.objects.filter(Yonetici_Il = district).order_by(
            'Yonetici_Durumu'
    )
    #management_of_district = management_of_district.order_by('Yonetici_Durumu')
    data = { 

        'management' : district_management, 
        'womans' : district_womans, 
        'youngers' : district_youngers, 
        'districtt' : district

    }
    return render(request , 'districts.html' , data)

def managerPage(request , district_or_city ,id):
    try:
        Ilce.objects.get(Ilce_Ismi = district_or_city)
        manager = Ilce_Baskanligi.objects.get(id=id)
    except ObjectDoesNotExist:
        manager = Il_Baskanligi.objects.get(id = id)
    
    data = {
        'manager' : manager , 
    }
    return render(request , 'managerr.html' , data)