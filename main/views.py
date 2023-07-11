from django.shortcuts import render
from sehitler.models import Sehit
from donations.models import Bagis
from news.models import New
from temmuz15gecesi.models import Temmuz15
from teskilat.models import Ilce
from teskilat.models import Il
# Create your views here.



def homePage(request):
   
    sehit_objects = Sehit.objects.all()
    donation_objects = Bagis.objects.all()[0:3]
    new_objects = New.objects.all()[0:3]
    temmuz15_objects = Temmuz15.objects.all()[0:4]
    data = {'sehitler' : sehit_objects , 
            'donations' : donation_objects,
            'news' : new_objects , 
            'temmuz15' : temmuz15_objects}


    return render(request , 'home.html',data)

def contactPage(request):
    return render(request , 'iletisim.html')
